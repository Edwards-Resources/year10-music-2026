---
version: 1
slug: "build-py"
primary_target: "build.py"
related_targets: ["docs/index.html"]
---

# Surface brief: class site home and lesson surfaces (Marker Zine world)

## Scope and mode

The whole class site (home, course, topic, lesson pages), rebuilt in the Marker Zine world. Mode: Read (students come to understand lesson content; the home page adds an Operate layer of "get me to today"). Scope decision 5 Aug 2026: one site per class per year; this repo becomes the Year 10 Music 2026 site.

## Audience, job, action

Year 10 Music students (about 15), on school devices and projected in B2; Matthew teaching from it live. Job: reach today's lesson instantly, see position in the 30-lesson sequence, work down a lesson with pen in hand. Primary action: the START / GO TO LESSON button into the current lesson.

## Chosen direction

World: hand-drawn technical zine (source: hand-drawn-zine-explainer, seed key 4c7deea4, chosen over the assigned Mixtape direction by Matthew on the decision page). Composition: approved comp C, `.impeccable/mocks/comp-c-comic-dashboard.png` (approved 5 Aug 2026). Mascot: the inky black crow stays; comp B's deerstalker crow is the Sound Detectives topic variant. Palette fixed: paper #FFF8EC, ink #111111, highlight yellow #FFE34D, pink #FF6BAE, teal #00C7B7.

## Memorable moment

The comic-panel dashboard: TODAY panel with the lesson huge, doodle arrows hopping between hand-inked panels, and the 30-frame filmstrip along the bottom with the class position ringed in yellow highlighter.

## Component grammar (from the approved comp)

- Panels: hand-inked wobbly borders about 2.5-3px, slightly rotated tabs as corner labels (teal/yellow/pink highlighter blocks with marker caps), cream ground inside and out. TODAY panel carries a teal outer offset border.
- Type ramp: marker display caps for panel labels and lesson numbers (LESSON 6 at about 96-120px on desktop), clean humanist sans for titles and body, hand-note face for margin annotations. Headline scale relationship roughly 5:2:1.
- Doodle arrows: dashed, curved, hand-drawn character, hopping between panels; draw-on via stroke-dashoffset on scroll, pre-drawn under reduced motion.
- Highlighter swipes: rough-edged flat rectangles behind text, yellow for emphasis/current, pink for warnings/exam, teal for section identity.
- Callouts: LEARNING INTENTION as yellow starburst label, SUCCESS CRITERIA as pink strip label, both with marker caps and bulleted sans lists.
- Filmstrip: 30 numbered square frames edge to edge at the bottom; completed frames crossed out in marker X, current frame ringed in yellow, exam frame flagged pink. Numbers must run 1-30 with none skipped (the comp skips some; that is a comp defect, not design).
- Buttons: marker-lettered caps on yellow highlighter block with hand-inked border; active state adds emphasis dashes.

## Fidelity inventory (medium per ingredient)

| Ingredient | Medium |
| --- | --- |
| Crow mascot poses (masthead head, headphones listening, deerstalker detective) | generated raster on flat #FFF8EC, produce before ship |
| Marker display face | self-hosted woff2 (closest obtainable to comp lettering) |
| Body sans | self-hosted woff2, Atkinson Hyperlegible (access provisions) |
| Hand-note margin face | self-hosted woff2 |
| Wobbly panel borders | authored SVG (border-image / inline paths with subtle irregularity) |
| Doodle arrows, stars, checkmarks, crosses | authored inline SVG paths, draw-on animation |
| Highlighter swipes | authored SVG rough rects (or CSS clip-path), flat colour |
| LI starburst / SC strip labels | authored SVG shapes |
| Alarm clock doodle (exam panel) | authored SVG line art; regenerate as raster only if the SVG reads badly |
| Coming-up icons (mic, keys, question mark) | authored line SVG in world grammar |
| START button treatment (yellow block + inked border) | HTML/CSS/SVG, signature element, no shortcut |
| Exam countdown number | client-side JS (computed at view time) |
| Filmstrip | HTML/CSS with SVG marks |
| Paper ground | flat #FFF8EC (no texture raster; the quality bar's fiber is optional and omitted) |

## Compositional commitments

Nav: crow head + wordmark left, real IA links right (no login/signup; the comp's CONTACT is not real IA and is dropped). TODAY panel spans about two thirds; right rail stacks LAST TIME, COMING UP, EXAM IN N DAYS. Filmstrip full width at the base of the viewport. Lesson pages inherit the panel/callout/highlighter grammar in single-column zine layout.

## Must not literalize from the comp

Invented success criteria, coming-up items and week titles (real data exists); skipped filmstrip numbers; the comp's CONTACT nav item; any account UI.

## Unresolved

GitHub org name; final repo/folder rename to the class-year identity; the 23 unfilled listening slots; DoE external-publishing policy check before the URL goes to students.
