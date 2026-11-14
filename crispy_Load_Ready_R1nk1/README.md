# Load Ready — R1nk1 / Crispy Clean

An edited version of R1nk1's Load Ready that signals when loading finishes, with configurable audio and a choice between waiting for player input and automatic entry.

https://github.com/user-attachments/assets/ca429974-a2c6-40aa-8442-32b78e30d1e1

## Functionality and settings

- MCM entry mode: wait for the player (default), or native automatic entry using `keypress_on_start`.
- Audio modes: voice/PDA conversations, PDA alerts, experimental radio, or custom OGG files. Defaults: enabled, voice mode, volume **0.85**.
- Voice selection extras and PDA alert selection; radio channel/playlist filters, playback limit and tail after entry.
- Custom sounds go in `gamedata/sounds/r1_load_ready/custom/`, including subfolders. Play one random file or all in alphabetical path order, once. Optionally stop custom playback on entry; radio tail/limit settings do not truncate custom playback.
- Optional jokes and a 1% sound-only screamer chance per loading screen; neither enables real emissions. Both default off.
- English/Russian MCM strings and optional debug logging (enabled by default).

MCM values override fallback defaults in `gamedata/configs/r1_load_ready.ltx`. The legacy `auto_delay` setting is retained for old data but ignored by this version. First-notification state uses Anomaly's existing global options store.

## Requirements and compatibility

Targets Anomaly **1.5.3** with full [Modded Exes](https://github.com/themrdemonized/xray-monolith) providing both loading-screen prompt/dismissed callbacks. Install MCM for the settings page. The script disables itself with a log message when the required engine bridge is absent.

The automatic-entry bridge repairs a missing dismissed callback on older Modded Exes builds after gameplay has begun. It does not simulate keys or use an external DLL. Do not enable this alongside Load Ready Lite or another installation of R1nk1 Load Ready. No vanilla script files are overridden.

## Credits and provenance

- R1nk1: original [Load Ready Sound / by R1nk1](https://www.moddb.com/addons/load-ready-sound-by-r1nk1).

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

---

[Back to all mods](../README.md)

made with ❤️ by SavageBulldogOG
