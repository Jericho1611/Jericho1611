#!/usr/bin/env python3
"""Draw the section headings for the profile README as standalone SVGs.

Each heading is one word in JetBrains Mono SemiBold followed by a rule that
runs out to the right margin. The typeface is subset to only the characters
that heading draws and inlined as base64, so the file loads nothing from a
third party and cannot be rate limited or go dark.

Usage:
    python3 scripts/make_headings.py            # redraw every heading
    python3 scripts/make_headings.py about      # redraw one
"""

import base64
import io
import sys
from pathlib import Path

from fontTools.subset import Subsetter
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "scripts" / "fonts" / "JetBrainsMono-SemiBold.ttf"

HEADINGS = ["about", "competition", "projects", "stack"]

WIDTH = 620          # matches the image width the README asks for
HEIGHT = 26
FONT_SIZE = 16
ADVANCE = 0.600      # JetBrains Mono advances exactly 0.600 em per glyph
GAP = 18             # space between the word and the start of the rule
BASELINE = 18
RULE_Y = 12.5

# GitHub Primer colors, light theme then dark.
TEXT_LIGHT, RULE_LIGHT = "#424a53", "#d8dee4"
TEXT_DARK, RULE_DARK = "#f0f6fc", "#30363d"

FALLBACK = (
    "ui-monospace,SFMono-Regular,Menlo,Consolas,"
    "&apos;Liberation Mono&apos;,monospace"
)


def subset_font(text):
    """Return the font as base64 woff2, carrying only the glyphs in text."""
    font = TTFont(FONT)
    subsetter = Subsetter()
    subsetter.populate(text=text)
    subsetter.subset(font)
    font.flavor = "woff2"
    buffer = io.BytesIO()
    font.save(buffer)
    return base64.b64encode(buffer.getvalue()).decode("ascii")


def draw(word):
    """Write hd-<word>.svg and return its path."""
    rule_x = round(len(word) * FONT_SIZE * ADVANCE) + GAP
    font_data = subset_font(word)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" '
        f'height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none" '
        f'font-family="JBMono,{FALLBACK}">'
        "<style>"
        "@font-face{font-family:JBMono;font-style:normal;font-weight:600;"
        f"font-display:block;src:url(data:font/woff2;base64,{font_data}) "
        "format('woff2')}"
        f".t{{fill:{TEXT_LIGHT}}}.r{{stroke:{RULE_LIGHT}}}"
        "@media(prefers-color-scheme:dark){"
        f".t{{fill:{TEXT_DARK}}}.r{{stroke:{RULE_DARK}}}}}"
        "</style>"
        f'<text x="0" y="{BASELINE}" class="t" font-size="{FONT_SIZE}" '
        f'font-weight="600">{word}</text>'
        f'<line x1="{rule_x}" y1="{RULE_Y}" x2="{WIDTH}" y2="{RULE_Y}" '
        'class="r" stroke-width="1"/>'
        "</svg>"
    )

    path = ROOT / f"hd-{word}.svg"
    path.write_text(svg)
    return path


def main():
    words = sys.argv[1:] or HEADINGS
    for word in words:
        path = draw(word)
        print(f"{path.name}  {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
