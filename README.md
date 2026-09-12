<div align="center">

# Joshua Gottus

<samp>robotics and embedded software</samp>

[jr-cho.com](https://jr-cho.com) &nbsp;·&nbsp;
[linkedin](https://linkedin.com/in/jr-cho) &nbsp;·&nbsp;
[github](https://github.com/jr-cho)

</div>

<img src="./hd-about.svg" width="620" alt="about"/>

> C and C++ on microcontrollers, autonomy on top.<br>
> Small hardware that has to work on the first try.

Software Lead on Florida Polytechnic's IEEE SoutheastCon hardware<br>
team. Computer Science, Florida Polytechnic University.

<img src="./hd-competition.svg" width="620" alt="competition"/>

**[SECON27](https://github.com/jr-cho/SECON27)** &nbsp;·&nbsp; `docs` &nbsp;·&nbsp; <samp>current</samp><br>
Fully autonomous robot for the SoutheastCon 2027 stock car race.<br>
Three laps on a 4x8 ft oval, one pit stop to swap tires, a school<br>
flag raised on the last lap. Three minutes, no external control<br>
once the match starts. AprilTags mark the assigned pit spot.

**[SECON26](https://github.com/jr-cho/SECON26)** &nbsp;·&nbsp; `c` `c++` `python`<br>
Ground robot and micro UAV for the SoutheastCon 2026 lunar rescue.<br>
The robot runs embedded C on a Raspberry Pi through four antenna<br>
tasks. The 250 g ESP32 UAV reads their LED colors and sends them<br>
over an IR link to a photodiode ground station.

<details>
<summary><samp>system diagram</samp></summary>

```mermaid
flowchart TD
  A["ground robot<br>raspberry pi · embedded C"]
  B["four antenna tasks"]
  C["antenna LEDs"]
  D["micro UAV<br>250 g · ESP32"]
  E["photodiode<br>ground station"]

  A -->|motors and servos| B
  B --> C
  C -->|color read| D
  D -->|IR link| E
```

</details>

<img src="./hd-projects.svg" width="620" alt="projects"/>

**[PRNTSWRM](https://github.com/jr-cho/PRNTSWRM)** &nbsp;·&nbsp; `python` `javascript` `docker`<br>
Orchestrates print jobs across a mixed 3D printer fleet. Upload a<br>
sliced file, set a quantity, and a worker hands jobs to whichever<br>
printers are idle, whether they speak OctoPrint, Bambu, or SDCP.

**[cman](https://github.com/jr-cho/cman)** &nbsp;·&nbsp; `shell`<br>
C project manager and build orchestrator. Scaffolds a project,<br>
wires up the build, and drives it from one command instead of a<br>
pile of CMake invocations you retype every time.

<details>
<summary><samp>two smaller ones</samp></summary>

<br>

**[bump-arena-allocator](https://github.com/jr-cho/bump-arena-allocator)** &nbsp;·&nbsp; `c11` `cmake`<br>
Bump allocator in C11. An allocation is a pointer add and a bounds<br>
check. It moves one offset forward and never frees a single object.<br>
Reclaim the whole block at once with `arena_reset`.

**[CV-Color-Tracker](https://github.com/jr-cho/CV-Color-Tracker)** &nbsp;·&nbsp; `python`<br>
Tracks a color in a live camera feed. Built to try out ways of<br>
reading the LED indicators on the SoutheastCon 2026 antenna tasks<br>
before that code moved onto the robot.

</details>

<img src="./hd-stack.svg" width="620" alt="stack"/>

<samp>embedded &nbsp; c &nbsp; c++ &nbsp; esp32 &nbsp; raspberry pi</samp><br>
<samp>robotics &nbsp; motor and servo control &nbsp; i2c &nbsp; ardupilot &nbsp; px4 &nbsp; ir comms &nbsp; computer vision</samp><br>
<samp>systems &nbsp; linux &nbsp; cmake &nbsp; make &nbsp; docker &nbsp; podman &nbsp; git &nbsp; github runners</samp><br>
<samp>also &nbsp; python &nbsp; go &nbsp; typescript &nbsp; nix</samp><br>
<samp>editor &nbsp; neovim &nbsp; tmux</samp>
