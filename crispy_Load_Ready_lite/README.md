# Load Ready Lite

**Version:** `1.0.0`

## Description

Plays one notification sound when the loading-screen key prompt appears, so you can hear when loading is ready.

## Preview

https://github.com/user-attachments/assets/ca429974-a2c6-40aa-8442-32b78e30d1e1

## Features and configuration

Uses the Modded Exes loading-screen callback and waits for precaching/audio muting to finish before playing the cue. Pending playback is cancelled when a new loading cycle or actor change resets the script. The audio wait ends after 60 seconds if precaching never completes.

No MCM page or state files. To customize, edit `SOUND` and `VOLUME` at the top of `gamedata/scripts/load_ready_lite.script`; volume defaults to **0.85** and is clamped to 0–1. The bundled cue is `gamedata/sounds/load_ready_lite/ready.ogg`.

## Requirements and compatibility

- [Modded Exes](https://github.com/themrdemonized/xray-monolith)

## Credits and provenance

- R1nk1: original [Load Ready Sound / by R1nk1](https://www.moddb.com/addons/load-ready-sound-by-r1nk1)
- Modded Exes contributors: loading-screen callback bridge.
- Anomaly developers / GSC Game World: game and audio systems.
- The bundled `ready.ogg` has no accompanying source/author record in this folder; its individual origin could not be verified. Do not assume repository authorship or blanket reuse rights for that audio.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
