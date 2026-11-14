# Back and Forth Button Position Patch

Adds MCM controls for repositioning the Back and Forth buttons on the settings page.

## Requirements

- [Mod Configuration Menu - ravenascendant](https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu)
- [Back and Forth v0.5.1 - ser_nailus](https://www.moddb.com/mods/stalker-anomaly/addons/back-and-forth-buttons)

English/Russian string tables are supplied.

## Installation

Install the ZIP from [releases](https://github.com/SBDG-0/crispy_stalker_anomaly/releases) as a separate mod in MO2.

Enable it alongside Back and Forth in Mod Organizer 2.

It adds its own script and text files; no original file is replaced.

<img src="https://github.com/user-attachments/assets/3848a52b-f745-447b-8aae-19f334947130" alt="Back and Forth button position settings" width="900" />

## Features

- Adjust Horizontal offset and Vertical offset on this patch's MCM page, then Apply.
- Both use negative for left/up, positive for right/down and zero for native placement.
- Default slider ranges cover the entire normalized Anomaly UI canvas: X -1024..1024; Y -768..768.
- These UI coordinates apply to both 16:9 and 21:9.
- The actual allowed motion is calculated from the parent dialog's width/height and the full control group's dimensions, leaving a four-unit margin inside the window.
- Controls remain inside their clickable parent frame.
- Moving beyond that limit leaves the group at the window frame edge, so the slider number is the requested offset rather than necessarily the effective offset.
- Offsets are always relative to each layout's native geometry and never accumulate.

## Known issues

- Controls can still overlap other UI elements; this patch only prevents the closed controls from leaving their parent window.
- Expanded dropdown popup placement is managed by the engine.

## Reuse

This software is provided "as is", without warranty of any kind. It is free to use, modify, and distribute provided you credit the author (SavageBulldog) and include a link back to the original repository.

[Original repository](https://github.com/SBDG-0/crispy_stalker_anomaly)

---

[Back to all mods](../README.md)

made with ❤️ by SavageBulldogOG
