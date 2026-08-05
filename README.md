# Teaching site

Lesson material for a Year 10 Music course, published with GitHub Pages. Students read
it; assessment stays in Canvas.

## How it works

- `data/` is the source of truth. One file per course, one per topic.
- `build.py` turns that into static pages in `docs/`. Standard library only, no
  dependencies to install and nothing to keep updated.
- `docs/` is what GitHub Pages serves. It is generated. Never edit it by hand.

## Building

```
python3 build.py
```

## Updating where a class is up to

Edit `position` in the topic file, for example
`data/courses/10mus1-2026/topics/sound-detectives.json`:

```json
"position": { "lesson": 7, "asAt": "2026-08-07", "note": "Lesson 7 runs Friday 7 August." }
```

Then rebuild and push.

## Adding a listening example

Find the lesson in the topic file and set the `embed` on its media block to the YouTube
video id (the part after `v=`), not the whole URL:

```json
{ "type": "media", "n": 1, "brief": "...", "embed": "dQw4w9WgXcQ" }
```

## Adding a course

1. Create `data/courses/<id>/course.json` with a `colour`, and a `topics` list.
2. Add topic files under `data/courses/<id>/topics/`.
3. Add the course id to `courses` in `data/site.json`.

Nothing else needs changing. The colour is the only per-course styling.

## What must never go on this site

Student names, student work, marks, Sentral or markbook data, NESA past papers or
marking guidelines, and copyright audio or video files. Recordings are embedded from
YouTube, never uploaded. The site is public.
