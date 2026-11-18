# Design: Year 10 Music (2026)

**This site is on the shared music shell**, since 19 November 2026. Every page, lessons, depth study steps, the two unit hubs, the course page and home, is built by `shell.py` and styled by `assets/shell.css`. The look belongs to the shell, not to this repo, and is the same across the music sites apart from one accent per year group. Year 10's is violet (`#5B3CC4`), set by `data-year="10"`.

The Marker Zine look it replaced (cream paper, marker type, highlighter tabs, the crow) is in git history up to `d3cf237`.

## Where the look lives

- **`../music-shell/README.md`**: what the shell is, what each file does, and its rules. The shell is a local repo beside this one and is never pushed.
- **`../.serve/proto/redesign/SHELL-PLAN.md`**: the plan the shell was built to.
- **`shell.py`, `assets/shell.css`, `assets/shell.js` and the fonts in `assets/fonts/`** are copies. Never edit them here. Edit `music-shell/`, then run `python3 music-shell/sync.py year10-music-2026` from `Sites/`.

## How the data reaches the shell

The data did not move. `data/courses/10mus1-2026/` is read as before and `build.py` hands the pieces to shell functions.

### Lessons and steps (28 lessons, 5 steps)

| Data | On the page |
| --- | --- |
| `title`, number, `week` or `where` | Head card: the unit as kicker, "Lesson n of 28, in Week w of Sound Detectives." as the meta line |
| `intention`, `criteria` | Learning intention, with the success criteria beside it |
| `steps` | In class when titled "What we are doing", otherwise Step by step, with the title kept |
| `explain` | Learn. The `call` sits large over the prose. A label that only says "Read this" is dropped; any other label is the title |
| `guide` | Cue sheet. Finer cues (`sub`) nest inside their cue; the `note` sits under the list. `provenance` and `receipt` stay in the data and are never printed |
| `media` | Listen. Consecutive media blocks share one card. The `work` names the clip; without one, the brief's first sentence does. No recording yet, or bring your own, says so in the clip's frame |
| `definition` | Key words, beside the next section that can take a side card, or on their own card when the next one cannot |
| `gapfill` | Fill in: a two-column table whose second column is boxes. Its id is still the slug of its title (`#dynamics-words`) |
| `formfill` | Fill this in: labelled questions with boxes, `lines` setting each box's height |
| `worked` | Worked example, full form: "A full answer" and "What scores nothing" |
| `check` | Check yourself, or If you were away: one fold, shut on load. **Answers live only here** |
| `rubric` | Marking criteria: the band ranges once as a key, then one card per criterion |
| `activity` | Your task |
| `exit` | Exit ticket |
| `wordbank`, `ideabank` | This site's own furniture (below) |
| `teacher` | Slides and notes, last |

Under the lesson, standalone only: the unit's pages folded shut.

### Unit hubs

Head card, "This unit" (the blurb with the outcomes beside it), the assessment card, the depth study's milestones, then every page of the unit grouped by week or phase, with each group's intro.

**No "Up to here" anywhere.** Sound Detectives' `position` (Lesson 10) went stale when the unit finished in Term 3 and is no longer read. The depth study never had one: every student is on a different project, so its milestones carry the dates instead, and `shell.js` works out done and next up from today's date when the page opens.

### Course page and home

The two units as cards. Home opens the newest one.

## What is still this site's own

- **The idea bank and the word bank**, styled in `assets/site.css`.
- **`assets/site.js`** carries ticks and typed answers saved under this site's old storage names across to the shell's, once per page per device. It never deletes the old entries.
- **In-text links** (`[Lesson 9](/10mus1-2026/sound-detectives/lesson-9/)`) are a shell feature now; `S.set_base()` is called once in `main()`.

## Rules that still hold

- Guide cues keep their `provenance` and `receipt`. Do not add, move or reword a cue's time without a run behind it.
- Answers live only inside `check` blocks.
- Italics are written `_x_`.
- Lessons 20 and 21 carry First Nations content and are under review. Do not edit their content.
