# Auto Wipe Mask in Intervals

**Version:** `1.0.0.0`

## Description

Toggles repeated mask wiping at a configurable interval using Anomaly's existing mask-cleaning function.

## Preview

<img src="https://github.com/user-attachments/assets/8fdb6c95-32d0-40cf-aa86-6789292daf8b" alt="Automatic mask wiping toggle" width="900" />

<img src="https://github.com/user-attachments/assets/38f52d4d-89e3-48a0-9f2e-feda9a6b4339" alt="Automatic mask wiping MCM settings" width="900" />

## Usage and settings

Open MCM's Mask Wiping page. Press **H** in game to toggle automatic wiping by default; a sound and message confirm the change. Automatic wiping starts disabled.

- Rebind the toggle key and optionally require Shift, Ctrl or Alt.
- Choose press, hold or double-tap activation. Hold mode activates the toggle; it is not a wipe-only-while-held mode.
- Set the interval from **2 to 60 seconds**, in one-second steps; the MCM default is **4 seconds**. The script's non-MCM fallback is 4.5 seconds, but MCM is required for supported configuration.
- English and Russian text files are included.

## Requirements

- [Mod Configuration Menu by ravenascendant](https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu)

## Credits

- NewbieRus: original [Wipe the mask at intervals](https://www.moddb.com/mods/stalker-anomaly/addons/wipe-the-mask-at-intervals) addon on ModDB, the base addon for this edited version.
- Anomaly developers: mask-cleaning function and game callbacks.
- ravenascendant and MCM contributors: settings/keybind framework.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, use the repository packaging workflow. ZIP roots contain only `meta.ini` and `gamedata/`; README files are excluded at every depth. Disable the mod in MO2 to remove its files.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
