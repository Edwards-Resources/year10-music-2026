# Next session

**Where things stand (5 August 2026):** The site is live at **https://edwards-resources.github.io/year10-music-2026/** (org `Edwards-Resources`, Pages on `/docs`, `noindex` confirmed). **Every listening slot in the Elements Toolkit unit (Lessons 1–27) is now filled**, including Lesson 12 (added 5 August: Grieg's "In the Hall of the Mountain King", Sydney Symphony Orchestra/Ashkenazy, `BLZl-hhbXDI` — unseen, tempo/dynamics/texture all build together, good for real-time multi-element annotation practice). Lesson 27 (student-choice listening) is intentionally left without a preset video via the `studentSupplied` flag. Lessons 28–30 (Week 10) have no media blocks at all, so there's nothing left to fill in this unit.

**Decided 5 August:** presentation mode — going with the lesson page itself as the presentable surface in class. No native "presenter mode" build. Nothing further to do here unless Matthew changes his mind.

**Still open:**

1. **NSW DoE publishing policy** — checked 5 August, no definitive ruling found. The Social Media Policy (PD-2011-0418) plausibly covers a role-connected public site, and more materially, the DoE Code of Conduct asserts the Department generally owns copyright in material staff create in connection with their employment (even made at home) — a copyright-ownership question, not just a hosting-location one. Matthew to raise with his Head Teacher or DoE legal (`legal@det.nsw.edu.au`) before the URL goes to students. Site already has no-index and no school branding as a precaution.

**Model/effort:** Sonnet, low-medium — remaining work here is routine (data entry, minor build tweaks) unless a new feature gets scoped.

**Watch out for:**
- `docs/` is generated; edit `data/` and `build.py`, then rebuild. Grep the built output for a candidate's YouTube ID after structural changes to confirm it landed on the right lesson page.
- After every content change: `python3 build.py`, commit, `git push`. The live Pages site only updates on push to `main`.
- The local preview symlink (`.claude/launch.json` → scratchpad `serve/year10-music-2026` → `docs/`) is session-scoped and needs recreating each new session. Recreate with:
  `ln -sfn ".../Sites/year10-music-2026/docs" "<current scratchpad>/serve/year10-music-2026"` and point `launch.json`'s `--directory` at that scratchpad's `serve` folder.
- Watch for exam-stimulus conflicts when picking tracks: the AT3 listening exam is Tuesday 18 August. Don't reuse its stimulus (e.g. *Uptown Funk*, already excluded) as a teaching example beforehand.
- Matthew has a separate, more mature "Bump It Up Wall" app at `~/Documents/Developer/Bump It Up Wall/` with real student data and its own privacy clearance (local-only). Its `10MUS1-elements-toolkit-content.md` is a good source of vetted definitions/listening examples to pull from, but the live board itself should not be folded into this public repo.
- No school name and no school brand assets anywhere, including the repo name, org name and README — this is a recorded product rule, not a preference.
- The design hook guards DESIGN.md; straight-edged highlighter fills or off-ramp font sizes are real defects, not noise.
- First Nations content (Lesson 22/23) follows the ICIP protocol note in the data: artist-approved recordings only, First Nations voices centred, no sacred/restricted material. If any of those tracks are ever swapped, keep that standard.

**Last commit:** `05b6cc5 Fill final listening slots (lessons 24-26) and fix student-choice copy for lesson 27` (pushed to `Edwards-Resources/year10-music-2026`).
