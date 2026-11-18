# MCM UI Tweaks

**Version:** `1.0.0`

## Description

**MCM UI Tweaks** combines the Back and Forth Button Position Patch and Custom Mod Categories Dropdown Position Patch into one expandable addon for S.T.A.L.K.E.R. Anomaly. Move both control groups from one MCM menu, with independent settings in two tabs.

## Preview

<img src="https://github.com/user-attachments/assets/3848a52b-f745-447b-8aae-19f334947130" alt="Back and Forth positioning controls from the standalone patch" width="900" />

The screenshots show the original standalone patches. The combined addon groups their settings under **MCM UI Tweaks**.

## Features

- One **MCM UI Tweaks** menu with **Back and Forth Position** and **Custom Mod Categories Dropdown** tabs.
- Independent horizontal and vertical offsets for each control group.
- Negative values move left/up; positive values move right/down; zero restores native placement.
- X range: −1024 to +1024 UI units. Y range: −768 to +768 UI units. These are virtual UI coordinates, applicable to both 16:9 and 21:9 layouts.
- Clamp movement to the clickable parent frame with a four-unit margin, using the complete control group's dimensions.
- Move CMC dropdowns and their labels together, including category and preset selectors.
- Copy existing standalone-patch offsets into the combined settings when those settings have not yet been saved. Existing combined values take priority, and Reset retains the zero defaults.
- Preserve native methods through wrappers, without replacing `ui_mcm.script` or original UI XML.

## Requirements

- [Mod Configuration Menu — ravenascendant](https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu).
- [Back and Forth — ser_nailus](https://www.moddb.com/mods/stalker-anomaly/addons/back-and-forth-buttons) for button positioning.
- [Custom Mod Categories — elseform](https://github.com/elseform/anomaly-mods/tree/release/Custom%20Mod%20Categories) for dropdown positioning.

Each component only adjusts controls supplied by its corresponding addon. If that addon is absent, its positioning component has no effect. Existing English and Russian slider translations are included; the new menu and tab names use the English names above in both languages.

## Installation

1. Install `crispy_MCM_UI_Tweaks.zip` as a separate mod in Mod Organizer 2.
2. Disable **crispy_Back_and_Forth_Button_Position_Patch** and **crispy_CMC_Dropdown_Position_Patch**. Keep Back and Forth, CMC, and MCM enabled as needed.
3. Enable **crispy_MCM_UI_Tweaks** and restart the game.
4. Open **MCM UI Tweaks**, choose a tab, adjust the offsets, and press **Apply**.

Do not enable the standalone position patches alongside this combined addon: their wrappers would adjust the same controls twice. Their source folders have been removed from this checkout; historical versions remain in Git history.

## Compatibility and limitations

Offsets are relative to each layout's native geometry and do not accumulate across updates. Moving beyond the allowed bounds leaves controls at the parent-frame edge, so the requested slider value may exceed the effective movement.

Controls can still overlap other UI elements. Expanded dropdown popup placement remains managed by the engine. Addons that replace the wrapped methods after installation may interfere with positioning. This addon targets the existing Anomaly/MCM addons and does not require GAMMA.

## Extending the addon

Runtime components live in separate scripts. The shared `crispy_mcm_ui_position.script` holds capture, bounds, movement, and offset-reading helpers. `zzz_crispy_mcm_ui_tweaks_mcm.script` is the only MCM entry point and registers the component tabs.

To add a future tweak, create a component exposing `build_tab()`, give it a unique tab ID and localized control hints, and add it to the entry point's component registry. Keep installation idempotent. Component filenames should not end in `mcm.script`; they must not create a second standalone menu. Existing standalone setting IDs remain available for migration.

## More screenshots

<img src="https://github.com/user-attachments/assets/d5e4ee85-4fc2-4d3d-86ec-c3945e3053f3" alt="Custom Mod Categories positioning controls from the standalone patch" width="900" />

## Changelog

### 1.0.0

- Combined both standalone position patches, based on their 1.3.0 implementations.
- Added one parent menu, two tabs, saved-offset migration, shared positioning helpers, and a component registry for future additions.

## Validation

Automated checks cover Lua compilation, menu structure, settings migration, independent offsets, bounds, reset-to-zero behavior, and repeated menu construction. Actual mouse hitboxes, popup behavior, and appearance still require in-game testing with the installed addons.

---

## Reuse

This software is provided “as is”, without warranty of any kind. You may use, modify, and distribute it, provided you credit SavageBulldogOG and include a link to this repository.

[crispy_stalker_anomaly](https://github.com/SBDG-0/crispy_stalker_anomaly)

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
