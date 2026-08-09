# Next session

**Where things stand (9 August 2026):** Site live at **https://edwards-resources.github.io/year10-music-2026/** (org `Edwards-Resources`, Pages on `/docs`, `noindex` confirmed). Two units, both complete: Sound Detectives (Term 3, 28 lessons) and Depth Study (Term 4, all 5 steps plus the three marking rubrics).

## Depth Study: done

All five steps are built and live: Choose your project, Write your proposal, Develop it, Refine and finalise, Present it. Step 4 carries all three marking rubrics (Performing, Composing, Listening and Investigation), pulled verbatim from `Year 10 (2026)/Program and Assessment/AT4 Depth Study/AT4 Task Notification Depth Study.docx`, tables 1 to 3.

Building the rubrics added a new **`rubric` block type** to `build.py` (see `block_html`, and the `.rubric-*` / `.band-*` rules in `assets/site.css`): one panel per criterion, bands listed rather than a five-column table (unreadable on a phone), with the mark-to-grade legend (A 17-20 / B 13-16 / C 9-12 / D 5-8 / E 0-4) drawn once above the criteria rather than repeated on every panel. Reuse this block type for any future rubric on this site or the Year 8 one.

Verified in-browser: content renders correctly on all three new pages, no console errors, no horizontal overflow at 390px width (`document.documentElement.scrollWidth === clientWidth`), and the `.gap-in-multi` textarea trap (below) still holds.

### The depth study's design decisions, already made

- **Steps, not lessons.** The registered program has a 12-lesson spine, but six of those lessons are "Development 3", "Development 4". A student page saying "keep working" is useless, so the site carries five steps and the 12-lesson spine stays in the registered program where it belongs. `pageWord` / `pageSlug` on the topic control this.
- **No position marker, ever, on this unit.** Every student is on a different project, so a single "we are up to" claim is wrong for the whole class rather than merely stale. `up_to()` returns None for a topic with no `position` key, and such a topic never becomes the home dashboard's subject. **When Term 4 starts and the dashboard should move to the depth study, do not solve it by adding a position** - that is a build.py change, not a data change.
- **Milestones are the honest substitute.** Baked at build time and recomputed by site.js from `[data-mile-date]`, because the page sits for weeks between rebuilds.
- **The unit has no crow pose.** The cover is data-driven (`topic.cover`) and renders text-only rather than borrowing Sound Detectives' deerstalker, which belongs to a listening unit. Generating one is ~10 minutes: the exact recipe (fal-ai/nano-banana-pro, 1:1, 2K, scratchy black ink marker sketch on flat warm cream) is in `assets/img/crow-detective.webp.json`. Match the paper ground exactly or it will not sit borderless.
- **Rubric bands are per-criterion text, mark ranges are rubric-level.** The task notification's table repeats "A (17-20)" as a column header across all four criteria; that is a total-rubric mark range, not a per-row one, so the JSON stores `bandRanges` once on the rubric block and each criterion only carries `[letter, text]` pairs.

### Two traps this increment found

- **`.gap-in-multi` must stay after `.gap-in` in site.css.** Both are single-class weight, `.gap-in` sets `border: 0`, so source order is the only thing making the textarea a box instead of a bare dashed rule. It shipped wrong once and the screenshot caught it.
- **Outcome statements on this site were paraphrased.** MU5-LIS-01 and MU5-LIS-02 were corrected on 9 August against the NESA PDF (`Syllabus Reference/Music 7-10 (2024)/NESA - music_7_10_2024 (S4, S5, LS).pdf`, table of outcomes, p13-14). MU5-LIS-02 had been carrying "musical concepts", which is 2009 syllabus language on a 2024 syllabus course. **Assume nothing about outcome wording already in `data/`; check it against the PDF.**

**Earlier state (7 August 2026):** Every listening slot in the Elements Toolkit unit (Lessons 1-27) is filled; Lesson 27 is deliberately `studentSupplied` and Lessons 28-30 have no media blocks.

**Done 7 August:** a new reusable `gapfill` block type, and nine fill-in tables across the elements lessons. Typed answers save to `localStorage` per lesson **per table**, each table has its own Clear button, and each gets an id from its title (`#dynamics-words`, `#tempo-words-italian`) so a single table can be linked to directly. No answers are stored in the page: these are filled in together, not self-marked. Pushed and live.

| Lesson | Tables |
| --- | --- |
| 1 | The six elements |
| 2 | Duration words; Tempo words (Italian); Pitch words |
| 4 | More texture words |
| 5 | Performing media words; Instrument families |
| 7 | Dynamics words; Expression words |
| 8 | Structure words |

Three judgement calls, all easy to reverse if Matthew disagrees: Lessons 4 and 8 already define their key terms on the page (the three textures; the four forms), so their tables cover the vocabulary *around* those instead of putting the answers directly above the blanks. Lesson 2 has three tables and is now the longest page in the unit. Lesson 5's second table changes the job (Family / "Name one instrument you heard"), so it is a listening record rather than a definition drill. Lesson 6 was left alone (it already has the timbre word bank and a book-table task); Lessons 3 and 9 are writing lessons.

**Still open:**

1. **NSW DoE publishing policy** - checked 5 August, no definitive ruling found. The Social Media Policy (PD-2011-0418) plausibly covers a role-connected public site, and the DoE Code of Conduct asserts the Department generally owns copyright in material staff create in connection with their employment. Matthew to raise with his Head Teacher or DoE legal (`legal@det.nsw.edu.au`) before the URL goes to students. Site already has no-index and no school branding as a precaution.
2. **Optional, only if Matthew asks:** a revision variant of `gapfill` that reveals answers (currently by design it does not), and/or porting the Year 8 site's general `table` block (any blank cell becomes a typeable field, `Sites/year8-music/build.py` line ~303) to Year 10 for multi-column worksheets. The two sites are separate codebases, so nothing is shared automatically.

**Model/effort:** Sonnet, low-medium - both units are now content-complete; remaining work is optional polish or new units, no design decisions pending.

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

**Last commit:** `3c2c31e Finish the Depth Study: steps 3-5 and the three marking rubrics` (pushed and deployment verified, 9 August 2026). Verify a fresh deployment rather than trusting the push:

```bash
curl -s "https://edwards-resources.github.io/year10-music-2026/10mus1-2026/depth-study/step-4/" | grep -c "Performing rubric"
```
