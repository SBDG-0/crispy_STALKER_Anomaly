# Item Spawner Search Box

**Version:** `1.0.2.0`

## Description

**Item Spawner Search Box** adds a search field and result counter to the debug item spawner in *S.T.A.L.K.E.R. Anomaly 1.5.3*. Find items by their display name or section ID across all spawner categories, including modded items supported by the installed spawner.

## Preview

<img width="900" alt="crispy_Item_Spawner_Search_Box" src="https://github.com/user-attachments/assets/3a393a7c-b049-47dc-97b1-5ac2e7627f2d" />

## Features

- Search every category without opening each one individually.
- Filter both the section list and icon grid together.
- Match multiple words in any order; every word must be present in the name or section ID.
- Show a live result count after a short 250 ms typing delay.
- Align the search label, input, and result-count panel with the Item type, By list, and By icon columns, with subtle translucent backgrounds behind the label and count.
- Keep the existing click-to-spawn behavior, destination setting, and exact-section spawn field.
- Block the Home shortcut during searches so it cannot spawn an entire category of hidden items.

## Requirements

- S.T.A.L.K.E.R. Anomaly **1.5.3**, with its debug item spawner available.
- Debug mode enabled to access the spawner.
- Mod Organizer 2 recommended for installation.

## Installation

1. Install this folder through MO2, with `gamedata` at the mod's root.
2. Enable **crispy_Item_Spawner_Search_Box** and restart the game.
3. Disable any older copy named **crispy_Debug_Item_Search** to avoid loading duplicate hooks.

Disable the mod in MO2 to uninstall it. No existing game files need editing.

## Usage

1. Load a save with debug mode enabled.
2. Open **F7 → Item spawner (1)**.
3. Type an item name or section ID into the search field at the top. Try `medkit` or a modded item's section ID.
4. Wait briefly for the list, grid, and result count to update.
5. Click a result to spawn it using the spawner's existing inventory/cursor destination setting.

Clear the search field to return to the selected category. If you have not selected a category yet, choose one. A search with no matches leaves both result views empty.

| Search behavior | Details |
| --- | --- |
| Fields searched | Item display name and section ID |
| Multiple words | All words must match; order does not matter |
| Letter case | ASCII case is ignored; non-ASCII case folding is not provided |
| Special characters | Matched literally, without patterns or regular expressions |
| Search scope | All categories, respecting the installed spawner's existing filters and blacklist |
| Home shortcut | Disabled while any non-whitespace search text is entered |

## Compatibility

The addon wraps the existing item-spawner methods at startup and supplies a small XML layout. It does not replace `ui_debug_launcher.script`, `ui_debug_launcher.xml`, or `ui_debug_launcher_16.xml`.

The controls occupy the top margin above the original panels. The layout targets vanilla and Sota/MAS ultrawide layouts whose panels begin at `y=40`. The label spans the Item type column (`x=40`, width `150`), the input spans By list (`x=200`, width `200`), and the count background spans By icon (`x=420`, width `564`). All occupy `y=6`, height `28`, with padding inside the count panel. The label and count use translucent black backgrounds matching the panel style. Other UIs using different column positions or that top margin may need the controls repositioned in `gamedata/configs/ui/crispy_debug_item_search.xml`.

Mods replacing the same spawner methods after startup may conflict. Existing spawning permissions and server restrictions continue to apply.

## Troubleshooting

- **No search field:** restart the game and check that this mod is enabled with the correct `gamedata` folder structure.
- **An item is missing:** try its section ID. Items excluded by the installed spawner's filters or blacklist remain excluded.
- **Controls overlap:** adjust the three controls in the addon XML for your UI layout.
- **Results stay empty after clearing:** select a category if none was selected before searching.

## Changelog

### 1.0.2.0

- Aligned the search row with the three spawner columns and removed overlapping control bounds.
- Added subtle translucent backgrounds behind the search label and result counter.
- Kept the changing counter as `CUITextWnd`, with a separate background static.

### 1.0.1.0

- Fixed the menu-opening crash from 1.0 by creating the result counter as `CUITextWnd` with `InitTextWnd`, which supports `SetText`.

### 1.0.0.0

- Added search across categories, synchronized list/grid filtering, result counts, and Home shortcut protection.

## Validation

LuaJIT checks cover script syntax and mocked search behavior.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
