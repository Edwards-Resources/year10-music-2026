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

## How it looks

Every page is built by the shared music shell (`shell.py` and `assets/shell.css`,
copied in from a local folder beside this repo). See `DESIGN.md`.

## Adding a listening example

Find the lesson in the topic file and set the `embed` on its media block to the YouTube
video id (the part after `v=`), not the whole URL:

```json
{ "type": "media", "n": 1, "brief": "...", "embed": "dQw4w9WgXcQ" }
```

## Adding a course

1. Create `data/courses/<id>/course.json` with a `topics` list.
2. Add topic files under `data/courses/<id>/topics/`.
3. Add the course id to `courses` in `data/site.json`.

The build expects one course per site.

## What must never go on this site

Student names, student work, marks, Sentral or markbook data, NESA past papers or
marking guidelines, and copyright audio or video files. Recordings are embedded from
YouTube, never uploaded. The site is public.
