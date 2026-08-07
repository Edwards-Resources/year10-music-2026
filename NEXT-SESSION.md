# Next session

**Where things stand (7 August 2026):** Site live at **https://edwards-resources.github.io/year10-music-2026/** (org `Edwards-Resources`, Pages on `/docs`, `noindex` confirmed). Every listening slot in the Elements Toolkit unit (Lessons 1-27) is filled; Lesson 27 is deliberately `studentSupplied` and Lessons 28-30 have no media blocks.

**Done 7 August:** Lesson 7 gained two fill-in tables (dynamics, expression) via a new reusable `gapfill` block type. Typed answers save to `localStorage` per lesson **per table**, each table has its own Clear button, and each gets an id from its title (`#dynamics-words`, `#expression-words`) so it can be linked to directly. No answers are stored in the page: these are filled in together, not self-marked. Pushed and live.

**Still open:**

1. **NSW DoE publishing policy** - checked 5 August, no definitive ruling found. The Social Media Policy (PD-2011-0418) plausibly covers a role-connected public site, and the DoE Code of Conduct asserts the Department generally owns copyright in material staff create in connection with their employment. Matthew to raise with his Head Teacher or DoE legal (`legal@det.nsw.edu.au`) before the URL goes to students. Site already has no-index and no school branding as a precaution.
2. **Optional, only if Matthew asks:** a revision variant of `gapfill` that reveals answers (currently by design it does not), and/or porting the Year 8 site's general `table` block (any blank cell becomes a typeable field, `Sites/year8-music/build.py` line ~303) to Year 10 for multi-column worksheets. The two sites are separate codebases, so nothing is shared automatically.

**Model/effort:** Sonnet, low-medium - remaining work here is routine content and small build tweaks, no design decisions pending.

**Watch out for:**
- `docs/` is generated; edit `data/` and `build.py`, then rebuild with `python3 build.py`. Commit and push, or the live Pages site does not update.
- The site sets `scroll-behavior: smooth`. Reading `window.scrollY` straight after a scroll returns a mid-animation value, and browser-tool screenshots lag a step behind. Set `document.documentElement.style.scrollBehavior='auto'` before scripted scrolling, or you will chase a scroll bug that is not there.
- Local preview needs a symlink because asset paths are absolute under `/year10-music-2026/`. Serve a folder containing a `year10-music-2026` symlink to `docs/`, not `docs/` itself:
  `ln -sfn ".../Sites/year10-music-2026/docs" "<scratchpad>/serve/year10-music-2026"`, then point the `teaching-site` entry in `School Master/.claude/launch.json` at `<scratchpad>/serve`. That path is session-scoped and needs recreating each session.
- Headless Chrome screenshots do not honour narrow `--window-size` values here (a 375-wide shot renders at a wider layout and crops), so they are not proof of mobile layout. Measure `document.documentElement.scrollWidth` against `clientWidth` in the browser instead.
- The design hook guards DESIGN.md; off-ramp font sizes and straight-edged highlighter fills are real defects. Use the documented type steps (`note` 1.35rem, `note-compact` 1.25rem, `label` 1rem, `label-large` 1.05rem).
- Don't reuse AT3 listening-exam stimulus as a teaching example beforehand. AT3 is Wednesday 19 August.
- No school name and no school brand assets anywhere, including repo, org and README. Recorded product rule, not a preference.
- First Nations content (Lessons 22/23) follows the ICIP protocol note in the data: artist-approved recordings only, no sacred or restricted material.

**Last commit:** `dd62452 Add fill-in tables for dynamics and expression words in Lesson 7` (pushed to `Edwards-Resources/year10-music-2026`).
