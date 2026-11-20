# Development log

## 2026-11-20 — Stealth Overhaul Reworked + Ghillie Rework compatibility patch — 1.0.0.0

### Implementation and behavior decisions

- User chose the earlier Stealth 2.31 compatibility patch's ghillie behavior within Reworked's broader stealth systems. The older patch is a reference, not a runtime dependency.
- Authored project: `crispy_Stealth_Overhaul_Reworked_Ghillie_Rework_1.2_Compatibility_Patch`.
- Uses a full `visual_memory_manager.script` overlay because Reworked keeps camouflage state in private locals. Other Reworked detection code remains in place, including noise integration, squad awareness, adaptation, night vision, HUD, memory, and engine-version guards.
- Slot 13 `ghillie_outfit` recognition reads actual equipment regardless of the event's triggering item and works without a slot 7 outfit. Refreshing inside actor camouflage evaluation also covers callbacks delivered before slot changes.
- Ghillie camouflage uses earth/dirt/grass/bush footstep materials, a 10-metre minimum, moving camouflage, the previous distance curve, and an extra crouch factor. Formula: clamp(visibility / 160 * (1 - distance * 0.018) * crouch * alert_factor, 0.01, 1). Defaults: visibility 100; firing-alert coefficient 60.
- Every unsuppressed non-melee weapon shot extends a three-second alert. Within 60 metres, alert_factor is firing_alert / distance; outside that range it is 1. Reworked's existing muzzle/noise responses remain active separately.
- Outside qualifying ghillie terrain, retains Reworked's stationary outfit camouflage, including its rain/night adjustments. The ghillie branch deliberately preserves the old formula without those additional adjustments. Camouflage is restricted to the actor so it does not affect NPC-to-NPC checks.
- First update resets terrain and ghillie firing-alert state. Unknown terrain gives no ghillie bonus until a footstep reports a material.
- `trans_outfit.script` provides only the legacy no-op timer entry point, preventing Ghillie Rework's global NPC range/FOV changes from competing with Reworked.
- `ghillie_stealth_mcm.script` preserves `poof/visibility` and `poof/firing_alert` settings, adds safe default fallback, and removes the unused angle control. English `ui_st_poof.xml` labels describe the new meaning. Old saved visibility values may come from the original mod's different formula.

### Source provenance and installation

- Authoring repository: `E:\!programming\.crispy_github_repository\_crispy_STALKER_Anomaly_repo`.
- Reworked source: `I:\.other.games\Mod.Organizer_Instance_Anomaly\mods\Stealth_Overhaul_Reworked`.
- Ghillie source: `I:\.other.games\Mod.Organizer_Instance_Anomaly\mods\[jaggervorog]_Ghillie_Rework_1.2`.
- Baseline Reworked `visual_memory_manager.script` SHA-256: `85e55a2aa288536b2384c46d5d617d58d5b7ee44a23d700c60a509c5bae68659`. MO2 metadata references multiple upstream versions, so no precise upstream version is claimed from it.
- Development installation is a directory junction with the project folder name under the MO2 `mods` directory, targeting the repository project. Both original installed mods remain untouched, verified by file hashes.
- Future Reworked updates require comparing the baseline and remerging the visual-memory overlay. Other mods replacing these scripts also require a merge. Anomaly 1.5.3 is the intended target; multiplayer is unverified.
- Local build and focused validation helpers are in `C:\Users\nerox\Documents\ChatGPT\anomaly modlist tedious tasks\stealth-overhaul-build`.

### Validation and remaining checks

- All three scripts compiled using the existing Lua 5.1 runtime. Parsed compiled prototypes to verify local counts below 200; maximum was 102 for the visual-memory script.
- Mocked checks passed for missing outfit, equipment removal, actor-only camouflage, natural/artificial/unknown terrain, distances around 10 metres, long-distance clamping, crouch variants, repeated-shot alert extension, suppressed shots, stationary outfit fallback, night adjustment, load reset, MCM changes/defaults, and absent actor guards.
- XML parsing, deployed-file comparison, README links/footer, original-mod hashes, and `git diff --check` passed.
- Repository packaging suite passed all 9 tests. Packaging built and verified all 16 mod archives; the new archive contained `meta.ini` plus four gamedata files, with no README.
- Still requires in-game checks for equip/unequip/drop, no regular outfit, natural versus artificial terrain, walking/crouching, distances near 10 metres, repeated loud and suppressed shots, MCM changes, and save/load. Automated checks do not establish gameplay balance or crash-free operation, especially interaction with Reworked's noise/awareness systems.

### Documentation policy

- Updated the parent Anomaly-specific AGENTS rules and repository AGENTS rules: READMEs are for players; development context belongs in this shared `.changelogs/devlogs.md`. Existing separate mod changelogs remain short and user-facing.
- Moved technical details, source evidence, local installation notes, and validation history out of this patch's README. Documentation-only revision; package version remains 1.0.0.0.

### Changelog location update

- User-facing changelogs now live in each mod's README. Development logs use separate per-mod Markdown files with descriptive filenames under `.changelogs/`.
- Relocated this patch's development history from the previously shared `devlogs.md` to `stealth-overhaul-reworked-ghillie-rework.md`, and moved its existing user-facing release entry into the patch README without changing its wording. Earlier documentation-policy notes above describe the previous arrangement.
