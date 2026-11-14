# Auto Wipe Mask in Intervals

Toggles repeated mask wiping at a configurable interval using Anomaly's existing mask-cleaning function.

<img src="https://github.com/user-attachments/assets/8fdb6c95-32d0-40cf-aa86-6789292daf8b" alt="Automatic mask wiping toggle" width="900" />

## Usage and settings

Open MCM's Mask Wiping page. Press **H** in game to toggle automatic wiping by default; a sound and message confirm the change. Automatic wiping starts disabled.

- Rebind the toggle key and optionally require Shift, Ctrl or Alt.
- Choose press, hold or double-tap activation. Hold mode activates the toggle; it is not a wipe-only-while-held mode.
- Set the interval from **2 to 60 seconds**, in one-second steps; the MCM default is **4 seconds**. The script's non-MCM fallback is 4.5 seconds, but MCM is required for supported configuration.
- English and Russian text files are included.

<img src="https://github.com/user-attachments/assets/38f52d4d-89e3-48a0-9f2e-feda9a6b4339" alt="Automatic mask wiping MCM settings" width="900" />

## Requirements and compatibility

Requires Anomaly and [Mod Configuration Menu by ravenascendant](https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu) with `key_bind`, modifier, hold and double-tap support. Calls `actor_effects.Hit_MaskCleaning()` without replacing `actor_effects.script`. It repeats while enabled rather than checking for rain or mask dirt itself; actual cleaning behavior comes from the installed actor-effects implementation. Avoid running another copy of the original `wiper_mask_mcm.script` alongside this version.

## Credits

- NewbieRus: original [Wipe the mask at intervals](https://www.moddb.com/mods/stalker-anomaly/addons/wipe-the-mask-at-intervals) addon on ModDB, the base addon for this edited version. Its page lists NewbieRus as uploader and describes the same key-toggle/MCM-interval functionality.
- SavageBulldog / SavageBulldogOG: repository edits, including the configurable key/modifier/activation-mode integration and localized MCM presentation in this version. An exact upstream diff is not included here.
- Anomaly developers: mask-cleaning function and game callbacks.
- ravenascendant and MCM contributors: settings/keybind framework.

The upstream addon is listed as Proprietary on ModDB; this repository's general reuse statement does not grant rights to the original author's work.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

---

[Back to all mods](../README.md)

made with ❤️ by SavageBulldogOG
