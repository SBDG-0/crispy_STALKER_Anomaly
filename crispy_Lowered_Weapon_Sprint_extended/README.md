# Lowered Weapon Sprint Extended

**Version:** `1.0.0.0`

## Description

**Lowered Weapon Sprint Extended** combines automatic sprint lowering, adjustable weapon poses, and the wheel and keyboard controls from **Lowered Weapon Key Extended** for *S.T.A.L.K.E.R. Anomaly*.

Lower your weapon while sprinting, adjust its position, or control raised/lowered stance and holstering yourself. Both mods are included in one installation.

## Features

- Automatically lower eligible weapons during sprinting and restore their previous stance afterward.
- Raise, lower, or toggle stance using the mouse wheel or separate keyboard bindings.
- Holster the equipped item and draw the last remembered item with configurable wheel/key actions.
- Three independent visual profiles: lowered sprint, raised sprint, and lowered without sprinting.
- Adjust each profile's X/Y/Z position, pitch, and yaw with smooth transitions.
- Blacklist or whitelist weapons, optionally including their attachment variations.
- Preserve scope zoom, binocular magnification, and PDA/menu scrolling.
- Keep existing sprint and Scroll Stance MCM settings and the saved sprint blacklist.

## Requirements

- S.T.A.L.K.E.R. Anomaly with Modded Exes providing legacy `hud_adjust`, actor callbacks, and input callbacks.
- **MCM 1.6 or newer** for the configuration pages and rebindable keys. Built-in defaults are used without MCM.

## Installation

1. Install this folder as a mod in Mod Organizer 2, with `gamedata` at the mod's root.
2. Disable the separate **Lowered Weapon Key Extended / Scroll Stance**, previous **Lowered Weapon Sprint Extended / Sprint Weapon Suite**, **Lower Weapon Sprint Optimized**, and the earlier separate **Lowered Weapon Position** mod, if installed.
3. Enable this combined mod and restart the game.
4. Open MCM → **Lowered Weapon Sprint Extended**, then choose **Sprint and Position** or **Keys and Wheel**.

> [!IMPORTANT]
> Run only one copy of these scripts. One MCM menu contains two settings tabs. Existing settings from the former separate pages are copied into the new menu automatically when it first builds; settings already saved in the new menu take priority. MCM Reset continues to use the original defaults.

## Configuration

### Sprint and position profiles

| Setting | Default | Description |
| --- | --- | --- |
| Automatic sprint lowering | On | Lower eligible weapons while sprinting |
| Position profiles | On | Enable the three independent visual profiles |
| Profile offsets | All zero | Add to the weapon's existing pose; profiles do not stack |
| Position range | −100 to +100 cm | Adjust left/right, down/up, and backward/forward |
| Pitch and yaw range | −90° to +90° | Rotate the hands/weapon without changing the camera or aim |
| Transition time | 200 ms | Blend into and out of profile offsets; Instant disables blending |
| Blacklist shortcut | Shift+L | Add/remove the current weapon; supports press, double-tap, and hold |
| Reverse blacklist | Off | Treat the list as a whitelist instead |
| Match weapon variations | On | Group weapons by their parent section when available |

The blacklist affects automatic lowering only. Position profiles and manual controls remain independent. Turn automatic lowering off to use the normal sprint animation with the raised-sprint profile. Older saved slider values remain in effect; use MCM Reset if you want the all-zero defaults.

### Keys and wheel

| Setting | Default | Description |
| --- | --- | --- |
| Wheel actions | On | Replace wheel weapon switching with the configured actions |
| Scroll up / down | Raise / Lower | Choose None, Raise, Lower, Toggle stance, Holster/draw, Holster, or Draw |
| Invert directions | Off | Swap the wheel directions |
| Wheel delay | 0 ms | Optional 0–500 ms delay between wheel actions |
| Raise / lower / toggle keys | Unassigned | Independent stance bindings |
| Holster/draw key | On | Use the game's Lower/Raise Weapon key, normally B |
| Holster key behavior | Toggle holster/draw | Alternatively select Holster only or Draw only |
| Custom holster key | Unassigned | Select Custom key as the source before using this binding |

Click a key control and press a key; Escape clears it. Use distinct bindings. Duplicate custom keys run one action in this order: raise, lower, toggle, then holster. Disabling wheel actions restores wheel weapon switching; keyboard actions remain available. Selecting None consumes that wheel direction outside menus/zoom.

### Manual control during sprinting

A wheel/key stance command takes priority over automatic lowering for the current sprint. Raising keeps the weapon raised until sprinting ends or a fire/reload/aim action returns control to the sprint logic. Manually lowering makes the lowered stance persist after sprinting ends. Changing weapons clears the sprint override. Holster/draw remembers the last equipped slot from the current session; after loading, equip an item before drawing it this way.

## Compatibility

This addon supplies scripts and English localization; it does not replace weapon configs, animations, DLLs, or the original game's scripts. No DLTX patches are required.

Aiming, firing, reloads, crouching/sliding, and active Cover Tilt take priority over visual profiles. The HUD adjustment wrapper observes other addons' writes, but addons that cache engine functions before it loads or adjust HUD data natively may bypass that cooperation. Weapon animation rotations can affect the apparent direction of offsets; tune profiles in-game.

## Validation

LuaJIT checks cover script syntax, manual stance ownership during sprinting, wheel/key integration, and reset behavior. XML files are checked for valid structure and duplicate string IDs.

## Credits

- **Skieppy** — original Lower Weapon Sprint addon.
- **Spaicrab and Coverdrave** — Lower Weapon Sprint edits.
- **henryd** — original [Scroll Stance](https://www.moddb.com/mods/stalker-anomaly/addons/scroll-stance).
- **crispy** — extended versions and combined integration.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
