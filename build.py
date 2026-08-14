#!/usr/bin/env python3
"""Build the teaching site.

Reads data/, writes docs/. Standard library only, on purpose: no package manager,
no lockfile, nothing that needs updating in three years when nobody is looking.

    python3 build.py

Every page is generated. Never edit anything in docs/ by hand; it gets overwritten.
"""

import html
import json
import os
import shutil
from datetime import date, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs")
ASSETS = os.path.join(ROOT, "assets")


def load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return json.load(f)


def e(s):
    return html.escape(str(s), quote=True)


def slug(s):
    out = "".join(c if c.isalnum() else "-" for c in str(s).lower())
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


def write(path_parts, markup):
    path = os.path.join(OUT, *path_parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markup)


# ----------------------------------------------------------------- doodles
# Hand-drawn SVG marks, authored once and inlined so they inherit the ink
# colour and can draw themselves on. All decorative, all aria-hidden.

X_MARK = """<svg class="doodle fx" viewBox="0 0 40 40" aria-hidden="true">
<path d="M7 6 C14 14, 24 26, 34 35" stroke-width="3.6"/>
<path d="M33 7 C25 15, 15 26, 6 34" stroke-width="3.6"/></svg>"""

RING = """<svg class="doodle ring" viewBox="0 0 60 60" aria-hidden="true">
<path d="M30 4 C48 3, 57 13, 56 29 C55 47, 44 57, 28 56 C11 55, 3 45, 4 29 C5 13, 15 5, 32 5" stroke-width="3.4"/></svg>"""

CHECK = """<svg class="doodle" viewBox="0 0 24 24" aria-hidden="true">
<path d="M3 14 C6 17, 8 19, 9 20 C12 13, 17 6, 22 2"/></svg>"""

NOTE = """<svg class="doodle" viewBox="0 0 24 24" aria-hidden="true">
<path d="M9 18 C9 20, 5 21, 4 19 C3 17, 6 15, 9 16 L9 5 L19 3 L19 15 C19 17, 15 18, 14 16 C13 14, 16 12, 19 13"/></svg>"""

CLOCK = """<svg class="doodle doodle-clock" viewBox="0 0 72 72" aria-hidden="true">
<path d="M36 12 C52 11, 62 22, 61 37 C60 53, 49 62, 35 61 C20 60, 11 50, 12 36 C13 21, 22 13, 38 13"/>
<path d="M36 24 L36 38 L46 44"/>
<path d="M16 12 C12 8, 8 10, 7 14"/>
<path d="M56 12 C60 8, 64 10, 65 14"/>
<path d="M24 60 L20 66 M48 60 L52 66"/></svg>"""

ARROW_DOWN = """<svg class="doodle draw-on" viewBox="0 0 60 90" aria-hidden="true" style="width:38px;height:57px">
<path class="dashed" d="M42 6 C18 24, 16 52, 28 80"/>
<path d="M28 80 L16 68"/>
<path d="M28 80 L38 66"/></svg>"""

ARROW_POINT = """<svg class="doodle draw-on doodle-point" viewBox="0 0 60 40" aria-hidden="true">
<path class="dashed" d="M4 8 C20 30, 36 34, 54 26"/>
<path d="M54 26 L42 24"/>
<path d="M54 26 L46 35"/></svg>"""

ARROW_HOP = """<svg class="doodle draw-on dash-hop" viewBox="0 0 120 60" aria-hidden="true">
<path class="dashed" d="M8 52 C30 10, 78 6, 110 28"/>
<path d="M110 28 L96 24"/>
<path d="M110 28 L102 40"/></svg>"""

DOT = """<svg class="doodle" viewBox="0 0 24 24" aria-hidden="true">
<path d="M12 7 C16 6, 18 9, 17 13 C16 17, 11 18, 8 15 C6 12, 8 8, 13 8" stroke-width="3.4"/></svg>"""

NOTES_PAIR = """<svg class="doodle today-notes-doodle" viewBox="0 0 54 54" aria-hidden="true">
<path d="M20 40 C20 44, 13 45, 12 41 C11 37, 17 35, 20 37 L20 16 L34 12 L34 33 C34 37, 27 38, 26 34 C25 30, 31 28, 34 30" stroke-width="2.6"/>
<path d="M44 22 C44 25, 39 26, 38 23 C37 20, 42 19, 44 20 L44 8 L50 6" stroke-width="2.2"/></svg>"""

STAR = """<svg class="doodle panel-star" viewBox="0 0 24 24" aria-hidden="true">
<path d="M12 3 L14 9 L21 10 L16 14 L17 21 L12 17 L7 21 L8 14 L3 10 L10 9 Z"/></svg>"""


# ---------------------------------------------------------------- page shell


def layout(site, title, body, crumbs=None, description="", body_attrs="", nav_links=None):
    base = site["base"]
    crumbs = crumbs or []
    nav = ""
    links = nav_links or site.get("nav") or []
    if links:
        items = "".join(f'<a href="{base}{href}">{e(label)}</a>' for label, href in links)
        nav = f'<nav class="site-nav" aria-label="Site">{items}</nav>'
    robots = '<meta name="robots" content="noindex, nofollow">' if site.get("noindex") else ""

    trail = ""
    if crumbs:
        links = []
        for i, (label, href) in enumerate(crumbs):
            if href and i < len(crumbs) - 1:
                links.append(f'<li><a href="{base}{href}">{e(label)}</a></li>')
            else:
                links.append(f'<li><span aria-current="page">{e(label)}</span></li>')
        trail = (
            '<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap">'
            f'<ol>{"".join(links)}</ol></div></nav>'
        )

    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}
<title>{e(title) if title == site['title'] else e(title) + ' | ' + e(site['title'])}</title>
<meta name="description" content="{e(description)}">
<link rel="stylesheet" href="{base}/assets/site.css">
</head>
<body{body_attrs}>
<!--
THESIS: A class dashboard drawn like a mate's brilliant annotated notes. Refuses
the school-course-card-grid: the home page is a comic page of hand-inked panels
where TODAY is enormous and the term is a filmstrip you can touch.
OWN-WORLD: Cream paper, black marker ink, three flat highlighters (yellow, pink,
teal). Marker caps display over a hyperlegible sans, Caveat margin notes, wobbly
inked borders, doodle arrows that draw themselves, a scratchy crow mascot.
Recognisable with all content removed by the ink-and-highlighter grammar alone.
STORY: A student lands, sees WE ARE UP TO at poster scale, hits START, listens,
ticks off success criteria, and knows exactly how far the exam is.
FIRST VIEWPORT: Masthead, then the TODAY panel at two-thirds width (lesson number
huge, title, crow listening, START button), rail of LAST TIME / COMING UP / EXAM
panels, filmstrip of all 30 lessons across the base.
FORM: Hand-drawn technical zine (hand-drawn-zine-explainer), chosen by Matthew
over the assigned mixtape direction. Seed key 4c7deea4.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish
review, the verdict, and DESIGN.md
-->
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <div class="wrap">
    <img class="brand-crow" src="{base}/assets/img/crow-head.webp" alt="" width="52" height="52">
    <a class="brand" href="{base}/">{e(site['title'])}</a>
    {nav}
  </div>
</header>
{trail}
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <p>Class material. Assessment tasks, submissions and marks stay in Canvas.</p>
    <p class="foot-date">Updated {date.today().strftime('%-d %B %Y')}</p>
  </div>
</footer>
<script src="{base}/assets/site.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------- helpers


def flat_lessons(topic):
    return [l for w in topic["weeks"] for l in w["lessons"]]


def up_to(topic):
    """The lesson a class is currently on, or None.

    A topic may carry no position at all. The depth study is the case that
    forced this: every student is on a different project, so a single "we are
    up to" claim would be wrong for the whole class rather than merely stale.
    Such a topic publishes with no position grammar anywhere and never becomes
    the home dashboard's subject.
    """
    lesson_no = (topic.get("position") or {}).get("lesson")
    if not lesson_no:
        return None
    return next((l for l in flat_lessons(topic) if l["number"] == lesson_no), None)


def page_word(topic):
    """What this topic calls one of its pages. Lessons run in sequence; the
    depth study's pages are steps a student works through at their own pace."""
    return topic.get("pageWord", "Lesson")


def page_slug(topic):
    return topic.get("pageSlug", "lesson")


def group_label(topic, week):
    """The heading for a group of pages. Weeks by default; the depth study's
    phases each span a different stretch of the calendar, so they carry their
    own label instead of a number."""
    return week.get("label") or f"Week {week['number']}"


def lesson_href(site, course, topic, lesson):
    return (
        f"{site['base']}/{course['id']}/{topic['id']}/"
        f"{page_slug(topic)}-{lesson['number']}/"
    )


def exam_days_text(a):
    """Baked-in fallback; site.js recomputes at view time."""
    if not a.get("examDate"):
        return ""
    exam = datetime.strptime(a["examDate"], "%Y-%m-%d").date()
    days = (exam - date.today()).days
    if days > 1:
        return f"Exam in {days} days"
    if days == 1:
        return "Exam tomorrow!"
    if days == 0:
        return "Exam TODAY"
    return ""


def filmstrip(site, course, topic):
    """Every lesson of the topic as one touchable strip."""
    current = topic["position"]["lesson"]
    exam_no = topic["assessment"].get("examLesson")
    frames = []
    for l in flat_lessons(topic):
        n = l["number"]
        cls, extra, label = "", "", f"{page_word(topic)} {n}: {l['title']}"
        if n < current:
            cls, extra = " frame-done", X_MARK
            label += " (done)"
        elif n == current:
            cls, extra = " frame-now", RING
            label += " (we are up to here)"
        if n == exam_no:
            cls += " frame-exam"
            extra += '<span class="frame-flag" aria-hidden="true">EXAM</span>'
            label += " (the AT3 exam)"
        frames.append(
            f'<li class="frame{cls}">'
            f'<a href="{lesson_href(site, course, topic, l)}" aria-label="{e(label)}">{n}</a>'
            f"{extra}</li>"
        )
    return f"""<section class="strip" aria-label="All lessons in {e(topic['name'])}">
  <div class="strip-head">
    <h2>The whole term</h2>
    <p class="note">every lesson, tap any square<span class="strip-hint"> · slide for more →</span></p>
    {ARROW_DOWN}
  </div>
  <div class="strip-scroll"><ol>{''.join(frames)}</ol></div>
</section>"""


# ------------------------------------------------------------------- blocks


def block_html(block):
    t = block["type"]

    if t == "steps":
        items = "".join(f"<li><span>{e(i)}</span></li>" for i in block["items"])
        return f'<section class="blk"><h2>{e(block["title"])}</h2><ol class="steps">{items}</ol></section>'

    if t == "definition":
        return (
            '<section class="blk blk-panel blk-def inked-b">'
            '<h2 class="tab">Key word</h2>'
            f'<p class="def-term"><span class="hl-teal">{e(block["term"])}</span></p>'
            f'<p>{e(block["text"])}</p></section>'
        )

    if t == "wordbank":
        words = "".join(f'<li><span class="hl-teal">{e(w)}</span></li>' for w in block["words"])
        return (
            '<section class="blk blk-panel blk-def inked-b">'
            f'<h2 class="tab">{e(block.get("title", "Word bank"))}</h2>'
            f'<ul class="wordbank">{words}</ul></section>'
        )

    if t == "gapfill":
        # A term-and-meaning table students fill in on screen. Answers are not in
        # the page: this is filled in together, not self-marked.
        key = slug(block["title"])
        cols = block.get("columns", ["Word", "What it means"])
        rows = "".join(
            f'<tr><th scope="row"><span class="hl-teal">{e(term)}</span></th>'
            f'<td><input type="text" class="gap-in" data-gap="{i}" '
            f'aria-label="{e(cols[1])} for {e(term)}" '
            f'autocomplete="off" autocapitalize="none" spellcheck="false"></td></tr>'
            for i, term in enumerate(block["rows"])
        )
        prompt = f'<p class="gap-prompt">{e(block["prompt"])}</p>' if block.get("prompt") else ""
        return (
            f'<section class="blk blk-panel blk-gap inked-c" id="{e(key)}" data-gap-key="{e(key)}">'
            f'<h2 class="tab tab-yellow">{e(block["title"])}</h2>'
            f"{prompt}"
            '<div class="gap-scroll"><table class="gaptable">'
            f"<thead><tr><th>{e(cols[0])}</th><th>{e(cols[1])}</th></tr></thead>"
            f"<tbody>{rows}</tbody></table></div>"
            '<p class="gap-tools"><button type="button" class="gap-clear">Clear this table</button>'
            '<span class="gap-saved">Your answers stay on this device.</span></p>'
            "</section>"
        )

    if t == "ideabank":
        # The menu of what a depth study can be. One panel per focus area, each
        # tiered so a student can see an honest entry point as well as a
        # stretch, and each naming the product it ends in.
        cards = []
        for i, f in enumerate(block["focuses"]):
            wob = ["inked", "inked-b", "inked-c"][i % 3]
            tiers = "".join(
                f'<li><span class="tier">{e(name)}</span><span>{e(text)}</span></li>'
                for name, text in f["tiers"]
            )
            cards.append(
                f'<li class="idea {wob}"><h3 class="tab">{e(f["name"])}</h3>'
                f'<ul class="idea-tiers">{tiers}</ul>'
                f'<p class="idea-product"><span class="idea-lab">You hand in</span> '
                f'{e(f["product"])}</p></li>'
            )
        lead = f'<p class="idea-lead">{e(block["lead"])}</p>' if block.get("lead") else ""
        return (
            f'<section class="blk"><h2>{e(block["title"])}</h2>{lead}'
            f'<ul class="ideabank">{"".join(cards)}</ul></section>'
        )

    if t == "formfill":
        # A proposal students fill in on screen. Same storage and Clear
        # behaviour as gapfill (it reuses those class names on purpose), but
        # the prompts are full questions, so they are set in the reading face
        # and only the short part label wears the marker.
        key = slug(block["title"])
        parts = []
        for i, row in enumerate(block["rows"]):
            if row.get("lines", 1) > 1:
                field = (
                    f'<textarea class="gap-in gap-in-multi" data-gap="{i}" '
                    f'rows="{int(row["lines"])}" aria-label="{e(row["label"])}" '
                    f'autocomplete="off" spellcheck="true"></textarea>'
                )
            else:
                field = (
                    f'<input type="text" class="gap-in" data-gap="{i}" '
                    f'aria-label="{e(row["label"])}" autocomplete="off" '
                    f'spellcheck="true">'
                )
            parts.append(
                f'<li><p class="form-lab"><span class="hl-teal">{e(row["label"])}</span></p>'
                f'<p class="form-q">{e(row["prompt"])}</p>{field}</li>'
            )
        prompt = f'<p class="gap-prompt">{e(block["prompt"])}</p>' if block.get("prompt") else ""
        return (
            f'<section class="blk blk-panel blk-gap blk-form inked-b" id="{e(key)}" '
            f'data-gap-key="{e(key)}">'
            f'<h2 class="tab tab-yellow">{e(block["title"])}</h2>'
            f"{prompt}"
            f'<ol class="formlist">{"".join(parts)}</ol>'
            '<p class="gap-tools"><button type="button" class="gap-clear">Clear this form</button>'
            '<span class="gap-saved">Your answers stay on this device.</span></p>'
            "</section>"
        )

    if t == "activity":
        return (
            '<section class="blk blk-panel blk-do inked">'
            '<h2 class="tab tab-yellow">Your task</h2>'
            f'<p>{e(block["text"])}</p></section>'
        )

    if t == "exit":
        return (
            '<section class="blk blk-panel blk-exit inked-c">'
            '<h2 class="tab tab-pink">Before you leave</h2>'
            f'<p>{e(block["text"])}</p></section>'
        )

    if t == "rubric":
        # One panel per criterion with the bands listed, not a five-column
        # table: a table that wide does not survive a phone screen. The mark
        # ranges are shared across the whole rubric (they describe the total,
        # not each 5-mark row), so they are drawn once as a legend rather than
        # repeated on every criterion.
        legend = "".join(
            f'<li><span class="band-chip">{e(letter)}</span>'
            f'<span class="band-range">{e(rng)}</span></li>'
            for letter, rng in block["bandRanges"]
        )
        lead = f'<p class="rubric-lead">{e(block["lead"])}</p>' if block.get("lead") else ""
        cards = []
        for i, c in enumerate(block["criteria"]):
            wob = ["inked", "inked-b", "inked-c"][i % 3]
            bands = "".join(
                f'<li class="rubric-band"><span class="band-tag">{e(letter)}</span>'
                f'<span>{e(text)}</span></li>'
                for letter, text in c["bands"]
            )
            cards.append(
                f'<li class="rubric-crit {wob}"><h3 class="tab">{e(c["name"])}</h3>'
                f'<ul class="rubric-bands">{bands}</ul></li>'
            )
        return (
            f'<section class="blk"><h2>{e(block["title"])}</h2>{lead}'
            f'<ul class="rubric-legend">{legend}</ul>'
            f'<ul class="rubriclist">{"".join(cards)}</ul></section>'
        )

    if t == "media":
        if block["embed"]:
            brief = f'<p class="media-brief">{e(block["brief"])}</p>' if block.get("brief") else ""
            work = f'<p class="media-work">{e(block["work"])}</p>' if block.get("work") else ""
            return f"""<section class="blk"><h2>Listen</h2>{work}
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{e(block['embed'])}"
title="Listening example" loading="lazy" allowfullscreen
allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture"></iframe></div>
{brief}</section>"""
        brief = block.get("brief") or "A listening example for this lesson."
        if block.get("studentSupplied"):
            mark = "Bring your own track for this one — nothing to add in advance."
        else:
            mark = "Not added yet. Mr Edwards is still picking this one."
        return f"""<section class="blk blk-panel blk-empty inked"><h2 class="tab">Listen</h2>
<p class="empty-mark">{e(mark)}</p>
<p class="media-brief">{e(brief)}</p></section>"""

    return ""


# -------------------------------------------------------------- milestones


def milestones_html(topic):
    """The depth study's shared spine.

    A unit where every student builds something different has no single lesson
    position, but it does have dates everyone shares. These are that: the
    checkpoints, in order, with the one coming up next carrying the position
    grammar. States are baked from the build date and recomputed by site.js at
    view time, because this page sits for weeks between rebuilds and a stale
    "next up" is worse than none.
    """
    miles = topic.get("milestones")
    if not miles:
        return ""

    today = date.today()
    nexted = False
    rows = []
    for m in miles:
        due = datetime.strptime(m["date"], "%Y-%m-%d").date()
        done = due < today
        is_next = not done and not nexted
        if is_next:
            nexted = True

        if done:
            cls, mark = " mile-done", f'{X_MARK}<span class="mile-mark">done ✓</span>'
        elif is_next:
            cls, mark = " mile-next", '<span class="mile-mark">← next up</span>'
        else:
            cls, mark = "", ""

        # Pink is the warning colour and belongs to the thing being marked.
        if m.get("assessed"):
            cls += " mile-due"

        what = e(m["what"])
        if is_next:
            what = f'<span class="hl">{what}</span>'
        elif m.get("assessed"):
            what = f'<span class="hl-pink">{what}</span>'

        rows.append(
            f'<li class="mile{cls}" data-mile-date="{e(m["date"])}">'
            f'<span class="mile-when">{e(m["when"])}</span>'
            f'<span class="mile-body"><span class="mile-what">{what}</span>'
            f'<span class="mile-detail">{e(m["detail"])}</span></span>'
            f'<span class="mile-state">{mark}</span></li>'
        )

    return f"""<section class="miles inked" aria-label="Milestones for {e(topic['name'])}">
  <div class="miles-head">
    <h2 class="tab">Your milestones</h2>
    <p class="note">everyone's project is different, these dates are not</p>
  </div>
  <ol class="mile-list">{''.join(rows)}</ol>
</section>"""


# ------------------------------------------------------------------- pages


def build_lesson(site, course, topic, lesson, prev_l, next_l):
    cur_l = up_to(topic)
    current = cur_l["number"] if cur_l else 0
    word = page_word(topic)

    crit = "".join(
        f'<li class="crit"><input type="checkbox" id="crit-{i}">'
        f'<span><label for="crit-{i}">{e(c)}</label></span></li>'
        for i, c in enumerate(lesson["criteria"])
    )
    blocks = "".join(block_html(b) for b in lesson["blocks"])

    teacher = ""
    if lesson.get("teacher"):
        items = "".join(f"<li>{e(t)}</li>" for t in lesson["teacher"])
        teacher = (
            '<aside class="teach inked-b"><h2 class="tab">Slides and notes</h2>'
            f"<ul>{items}</ul></aside>"
        )

    nav = []
    if prev_l:
        nav.append(
            f'<a class="pn pn-prev" href="{lesson_href(site, course, topic, prev_l)}">'
            f"<span>Previous</span><strong>{e(prev_l['title'])}</strong></a>"
        )
    if next_l:
        nav.append(
            f'<a class="pn pn-next" href="{lesson_href(site, course, topic, next_l)}">'
            f"<span>Next</span><strong>{e(next_l['title'])}</strong></a>"
        )

    here = ""
    if lesson["number"] == current:
        here = '<p class="here-flag">This is the lesson we are up to</p>'

    total = len(flat_lessons(topic))
    # Lessons sit in a numbered week; a depth study step spans its own stretch
    # of the calendar and says so in its own words.
    where = lesson.get("where") or f"in Week {lesson['week']} of {topic['name']}"

    body = f"""<article class="lesson">
<div class="wrap">
  <header class="lesson-head">
    <p class="lesson-no" aria-hidden="true">{e(word)} {lesson['number']}</p>
    <h1><span class="visually-hidden">{e(word)} {lesson['number']}: </span>{e(lesson['title'])}</h1>
    <p class="lesson-sub note">{e(word)} {lesson['number']} of {total}, {e(where)}.</p>
    {here}
  </header>

  <div class="aims">
    <section class="aim inked">
      <h2 class="tab-burst tab">Learning intention</h2>
      <p>{e(lesson['intention'])}</p>
    </section>
    <section class="aim inked-c">
      <h2 class="tab tab-pink">Success criteria</h2>
      <ul>{crit}</ul>
      <p class="note">tick them off as you go, they save on your device</p>
    </section>
  </div>

  {blocks}
  {teacher}

  <nav class="prevnext" aria-label="Lessons">{''.join(nav)}</nav>
</div>
</article>"""

    crumbs = [
        ("Home", "/"),
        (topic["name"], f"/{course['id']}/{topic['id']}/"),
        (f"{word} {lesson['number']}", None),
    ]
    key = f"{course['id']}-{topic['id']}-{lesson['number']}"
    return layout(
        site,
        f"{word} {lesson['number']}: {lesson['title']}",
        body,
        crumbs,
        lesson["intention"],
        body_attrs=f' data-lesson-key="{e(key)}"',
    )


def build_topic(site, course, topic):
    cur = up_to(topic)
    current = cur["number"] if cur else 0

    weeks = []
    for w in topic["weeks"]:
        rows = []
        for l in w["lessons"]:
            n = l["number"]
            cls, mark = "", ""
            if n < current:
                cls, mark = " row-done", '<span class="row-mark">done ✓</span>'
            elif n == current:
                cls, mark = " row-now", '<span class="row-mark">← we are here</span>'
            rows.append(
                f'<li><a class="row{cls}" href="{lesson_href(site, course, topic, l)}">'
                f'<span class="row-no" aria-hidden="true">{n}</span>'
                f'<span><span class="row-title">{e(l["title"])}</span><br>'
                f'<span class="row-int">{e(l["intention"])}</span></span>'
                f"{mark}</a></li>"
            )
        wob = ["inked", "inked-b", "inked-c"][w["number"] % 3]
        weeks.append(f"""<section class="week {wob}">
  <div class="week-head">
    <h2 class="tab">{e(group_label(topic, w))}</h2>
    <p class="week-title">{e(w['title'])}</p>
  </div>
  <p class="week-intro">{e(w['intro'])}</p>
  <ul>{''.join(rows)}</ul>
</section>""")

    outcomes = "".join(
        f"<li><strong>{e(code)}</strong> {e(text)}</li>" for code, text in topic["outcomes"]
    )

    a = topic["assessment"]
    assess_note = a.get("note") or "The task notification and the exam itself are in Canvas."
    assess = f"""<aside class="assess inked-c">
  <h2 class="tab tab-pink">{e(a['name'])}</h2>
  <p class="assess-when"><span class="hl-pink">{e(a['when'])}</span></p>
  <p>{e(a['detail'])}</p>
  <p class="note">{e(assess_note)}</p>
</aside>"""

    taught = sum(1 for l in flat_lessons(topic) if l["number"] < current)
    jump = ""
    if cur:
        jump = f"""<a class="jump" href="{lesson_href(site, course, topic, cur)}">
  <span class="jump-line">We are up to {page_word(topic)} {cur['number']} of {len(flat_lessons(topic))}</span>
  <span class="jump-title">{e(cur['title'])}</span>
  <span class="jump-note note">{e(topic['position']['note'])} {taught} lessons done so far.</span>
</a>"""

    # Each topic brings its own crow pose. A topic with no pose yet renders a
    # text-only cover rather than borrowing another unit's mascot, which would
    # put a detective hat on a unit that has nothing to do with detectives.
    cover_img = ""
    cov = topic.get("cover")
    if cov:
        cover_img = (
            f'<img class="cover-crow" src="{site["base"]}/assets/img/{e(cov["image"])}" '
            f'alt="{e(cov["alt"])}" width="300" height="300">'
        )

    body = f"""<div class="cover">
  <div class="wrap cover-grid{'' if cov else ' cover-grid-solo'}">
    <div>
      <h1><span class="hl-pink">{e(topic['name'])}</span></h1>
      <p class="cover-sub">{e(topic['subtitle'])} · {e(topic['term'])}</p>
      <p class="cover-blurb">{e(topic['blurb'])}</p>
      {jump}
    </div>
    {cover_img}
  </div>
</div>
<div class="wrap">
  <div class="topic-cols">
    <div class="topic-main">{milestones_html(topic)}{''.join(weeks)}</div>
    <div class="topic-side">
      {assess}
      <aside class="outcomes inked-b">
        <h2 class="tab">Outcomes</h2>
        <ul>{outcomes}</ul>
      </aside>
    </div>
  </div>
</div>"""

    crumbs = [("Home", "/"), (topic["name"], None)]
    return layout(site, topic["name"], body, crumbs, topic["blurb"])


def position_line(site, course, topic):
    """The one way this site says where a class is up to, at card scale."""
    cur = up_to(topic)
    if not cur:
        return ""
    return (
        f'<p class="pos-line"><span class="pos-lab">Up to</span> '
        f'<a href="{lesson_href(site, course, topic, cur)}">Lesson {cur["number"]}, {e(cur["title"])}</a></p>'
    )


def build_course(site, course, topics):
    base = site["base"]
    items = []
    for i, t in enumerate(topics):
        n = len(flat_lessons(t))
        wob = ["inked", "inked-b", "inked-c"][i % 3]
        unit = page_word(t).lower()
        items.append(f"""<li class="tcard {wob}">
  <a class="tcard-name" href="{base}/{course['id']}/{t['id']}/">{e(t['name'])}</a>
  <p class="tcard-term">{e(t['term'])}, {n} {unit}{'' if n == 1 else 's'}</p>
  <p>{e(t['blurb'])}</p>
  {position_line(site, course, t)}
</li>""")

    body = f"""<div class="home-head">
  <div class="wrap">
    <h1>{e(course['name'])}</h1>
    <p class="lede">{e(course['blurb'])}</p>
  </div>
</div>
<div class="wrap">
  <ul class="tcards">{''.join(items)}</ul>
</div>"""
    return layout(site, course["name"], body, [("Home", "/"), (course["name"], None)],
                  course["blurb"])


def build_home(site, courses):
    """The comic dashboard: TODAY at poster scale, the rail, the filmstrip."""
    base = site["base"]

    # The active topic: the one carrying the class position. One course per site
    # by scope decision; the loop keeps the build honest if that ever changes.
    course, topic, cur = None, None, None
    for c, topics in courses:
        for t in topics:
            got = up_to(t)
            if got is not None:
                course, topic, cur = c, t, got

    if not cur:
        # No live position anywhere: fall back to a plain course listing.
        body = """<div class="home-head"><div class="wrap">
<h1>Class material</h1>
<p class="lede">Everything we are working on, lesson by lesson.</p>
</div></div>"""
        return layout(site, "Class material", body, [], "Lesson material.")

    lessons = flat_lessons(topic)
    idx = next(i for i, l in enumerate(lessons) if l["number"] == cur["number"])
    prev_l = lessons[idx - 1] if idx else None
    coming = lessons[idx + 1 : idx + 4]

    last_time = ""
    if prev_l:
        last_time = f"""<section class="panel inked-b">
      <h2 class="tab tab-yellow">Last time</h2>
      <ul><li>{CHECK}<span><a href="{lesson_href(site, course, topic, prev_l)}">Lesson {prev_l['number']}: {e(prev_l['title'])}</a></span></li></ul>
    </section>"""

    coming_rows = "".join(
        f'<li>{NOTE}<span><a href="{lesson_href(site, course, topic, l)}">Lesson {l["number"]}: {e(l["title"])}</a></span></li>'
        for l in coming
    )

    a = topic["assessment"]
    exam_panel = ""
    if a.get("examDate"):
        fallback = exam_days_text(a) or f"Exam: {e(a['when'])}"
        exam_panel = f"""<section class="panel panel-exam inked-c">
      <h2 class="tab tab-pink">{e(a['name'])}</h2>
      {CLOCK}
      <p class="exam-count" data-exam-date="{e(a['examDate'])}">{fallback}</p>
      <span class="exam-when note">{e(a['when'])}</span>
    </section>"""

    first_crits = "".join(f"<li>{DOT}<span>{e(c)}</span></li>" for c in cur["criteria"])

    # The home page is a dashboard for whichever topic is running. Without this
    # head it read as though the site were the Term 3 unit, because the unit name
    # was the only name on the page. Sound Detectives is one term of the year.
    head = f"""<div class="home-head"><div class="wrap">
<h1>{e(course['name'])}</h1>
<p class="lede">Right now: <a href="{base}/{course['id']}/{topic['id']}/">{e(topic['name'])}</a>, {e(topic['term'])}. The other terms go up here as we get to them.</p>
</div></div>"""

    body = head + f"""<div class="dash">
<div class="wrap">
  <div class="dash-grid">
    {ARROW_HOP}
    <section class="panel panel-today inked" aria-label="Where we are up to">
      <h2 class="tab">We are up to</h2>
      {STAR.replace('panel-star', 'panel-star star-tr')}
      <div class="today-body">
        <div>
          <p class="today-lesson">Lesson {cur['number']}</p>
          <p class="today-title"><span class="uline">{e(cur['title'])}</span></p>
          <p class="today-note note">{e(topic['position']['note'])}</p>
          <div class="today-aims">
            <div class="mini-aim">
              <p class="tab-burst" aria-hidden="true">Learning intention</p>
              <p><span class="visually-hidden">Learning intention: </span>{e(cur['intention'])}</p>
            </div>
            <div class="mini-aim">
              <p class="tab tab-pink">Success criteria</p>
              <ul>{first_crits}</ul>
            </div>
          </div>
          <div class="today-actions">
            {ARROW_POINT}
            <a class="btn" href="{lesson_href(site, course, topic, cur)}">Go to the lesson</a>
            <a href="{base}/{course['id']}/{topic['id']}/">the whole topic →</a>
          </div>
        </div>
        <div class="today-crow-spot">
          {NOTES_PAIR}
          <img class="today-crow" src="{base}/assets/img/crow-listening.webp"
               alt="A scruffy sketched crow listening happily in big headphones" width="250" height="250">
        </div>
      </div>
    </section>
    <div class="rail">
      {last_time}
      <section class="panel inked">
        <h2 class="tab">Coming up</h2>
        <ul>{coming_rows}</ul>
      </section>
      {exam_panel}
    </div>
  </div>
  {filmstrip(site, course, topic)}
</div>
</div>"""

    return layout(site, course["name"], body, [],
                  f"Where {course['name']} is up to in {topic['name']}, lesson by lesson.")


# -------------------------------------------------------------------- main


def main():
    site = load("site.json")
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    pages = 0
    courses = []
    for cid in site["courses"]:
        course = load("courses", cid, "course.json")
        topics = [
            load("courses", cid, "topics", f"{tid}.json") for tid in course["topics"]
        ]
        courses.append((course, topics))

    # Masthead links: home plus every topic, built before any page renders.
    site["nav"] = [("Home", "/")] + [
        (t["name"], f"/{c['id']}/{t['id']}/") for c, ts in courses for t in ts
    ]

    for course, topics in courses:
        cid = course["id"]

        for topic in topics:
            write([cid, topic["id"], "index.html"], build_topic(site, course, topic))
            pages += 1
            lessons = flat_lessons(topic)
            for i, lesson in enumerate(lessons):
                write(
                    [cid, topic["id"], f"{page_slug(topic)}-{lesson['number']}", "index.html"],
                    build_lesson(
                        site, course, topic, lesson,
                        lessons[i - 1] if i else None,
                        lessons[i + 1] if i + 1 < len(lessons) else None,
                    ),
                )
                pages += 1

        write([cid, "index.html"], build_course(site, course, topics))
        pages += 1

    write(["index.html"], build_home(site, courses))
    pages += 1

    shutil.copytree(ASSETS, os.path.join(OUT, "assets"))
    # Prompt sidecars travel with the source assets, not the published site.
    for root_dir, _, files in os.walk(os.path.join(OUT, "assets")):
        for f in files:
            if f.endswith(".json"):
                os.remove(os.path.join(root_dir, f))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    missing = sum(
        1
        for _, ts in courses
        for t in ts
        for w in t["weeks"]
        for l in w["lessons"]
        for b in l["blocks"]
        if b["type"] == "media" and not b["embed"] and not b.get("studentSupplied")
    )
    print(f"built {pages} pages into docs/")
    if missing:
        print(f"  {missing} listening slots still have no recording")


if __name__ == "__main__":
    main()
