#!/usr/bin/env python3
"""Build the Year 10 Music teaching site.

Reads data/, writes docs/. Standard library only, on purpose: no package manager,
no lockfile, nothing that needs updating in three years when nobody is looking.

    python3 build.py

Every page is generated. Never edit anything in docs/ by hand; it gets overwritten.

Every page is built by the shared music shell (shell.py, copied in from
Sites/music-shell by its sync.py): direction B, Stage Card. This file only turns
the site's data into the shell's pieces. The Marker Zine world it replaced on
19 November 2026 is recorded in git history (up to d3cf237).
"""

import json
import os
import re
import shutil
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import shell as S  # noqa: E402  the shared page shell, copied in by music-shell/sync.py
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs")
ASSETS = os.path.join(ROOT, "assets")

FOOT = "Class material. Assessment tasks, submissions and marks stay in Canvas."


def load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return json.load(f)


def write(path_parts, markup):
    path = os.path.join(OUT, *path_parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markup)


def slug(s):
    """A fill-in table's id, from its title (#dynamics-words). Kept from the old
    build, because a single table can be linked to directly and site.js uses it
    to find answers saved under the old storage key."""
    out = "".join(c if c.isalnum() else "-" for c in str(s).lower())
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


# ---------------------------------------------------------------- helpers


def flat_lessons(topic):
    return [l for w in topic["weeks"] for l in w["lessons"]]


def page_word(topic):
    """What this topic calls one of its pages. Lessons run in sequence; the
    depth study's pages are steps a student works through at their own pace."""
    return topic.get("pageWord", "Lesson")


def page_slug(topic):
    return topic.get("pageSlug", "lesson")


def lesson_path(course, topic, lesson):
    """Site-relative. These addresses are what Canvas frames, so they never change."""
    return f"/{course['id']}/{topic['id']}/{page_slug(topic)}-{lesson['number']}/"


def group_label(topic, week):
    """Weeks by default; the depth study's phases each span a different stretch
    of the calendar, so they carry their own label instead of a number."""
    return f"{week.get('label') or 'Week ' + str(week['number'])}: {week['title']}"


def shell_site(site, topics_nav):
    return {"base": site["base"], "title": site["title"], "year": 10, "key": "y10-2026",
            "foot": FOOT, "nav": topics_nav, "noindex": site.get("noindex")}


ABBREV = {"ft", "feat", "mr", "mrs", "ms", "dr", "st", "vs", "no", "op"}


def first_sentence(text):
    """Split a media brief into the recording's name and the rest. A brief opens
    with what the recording is ("John Williams, 'Star Wars' Main Title. Heroic,
    adventurous mood."), so its first sentence names the clip. A sentence ends
    at a full stop followed by a capital, so "e.g. a band" does not split, and
    never after a short abbreviation."""
    head, rest = text, ""
    for m in re.finditer(r"[.!?]\s+(?=[A-Z])", text):
        # "Baker Boy ft. Yirrmal" is one name: a full stop after a short
        # abbreviation does not end the sentence.
        word = re.search(r"(\S+)$", text[:m.start()]).group(1)
        if word.lower().strip("(") in ABBREV:
            continue
        head, rest = text[:m.start() + 1], text[m.end():]
        break
    if len(head) > 90:
        return "Listening example", text
    return head, rest


# ------------------------------------------------------------------- blocks

# Labels that only said "this is reading". The shell's own label says that, so
# they are not repeated as a title. Any other label names the reading.
PLAIN_READ = {None, "Read this", "Read this too", "Read this first"}


def clip_of(b):
    pending = ""
    if not b.get("embed"):
        pending = ("Bring your own track for this one. Nothing to add in advance."
                   if b.get("studentSupplied") else "Not added yet. Mr Edwards is still picking this one.")
    brief = b.get("brief") or "A listening example for this lesson."
    if b.get("work"):
        title, by = b["work"], brief
    else:
        title, by = first_sentence(brief)
    return {"title": title, "embed": b.get("embed") or None, "by": by, "pending": pending}


def explain_body(body):
    out = []
    for item in body:
        if "h" in item:
            out.append({"h": item["h"]})
        elif "ul" in item:
            out.append({"ul": item["ul"]})
        else:
            out.append({"p": item["p"]})
    return out


def keys_dl(defs):
    kw = "".join(f'<div class="kw"><dt>{S.rich(d["term"])}</dt><dd>{S.rich(d["text"])}</dd></div>'
                 for d in defs)
    return f"<dl>{kw}</dl>"


def keys_label(defs):
    return "Key word" if len(defs) == 1 else "Key words"


def keys_side(defs):
    """Key words beside the section they belong to."""
    return S.side_card(keys_label(defs), "key", keys_dl(defs), cls="keys") if defs else ""


def ideabank(b):
    cards = []
    for f in b["focuses"]:
        tiers = "".join(f'<li><span class="tier">{S.e(n)}</span> <span>{S.rich(t)}</span></li>'
                        for n, t in f["tiers"])
        cards.append(f'<li class="idea"><h3>{S.rich(f["name"])}</h3><ul class="tiers">{tiers}</ul>'
                     f'<p class="idea-product"><strong>You hand in</strong> {S.rich(f["product"])}</p></li>')
    lead = f'<p class="brief">{S.rich(b["lead"])}</p>' if b.get("lead") else ""
    return S.section("ideas", "Ideas", "target", b["title"], f'{lead}<ul class="ideas">{"".join(cards)}</ul>')


def wordbank(b):
    words = "".join(f"<li>{S.e(w)}</li>" for w in b["words"])
    return S.section("words", "Word bank", "key", b.get("title"), f'<ul class="wordbank">{words}</ul>')


def block_section(b, side=""):
    """One block as one shell section, or None if this block takes no side card
    (the caller then shows any waiting key words on their own first)."""
    t = b["type"]
    if t == "steps":
        label = "In class" if b["title"] == "What we are doing" else "Step by step"
        return S.steps(b["items"], title=b["title"], label=label, side=side)
    if t == "explain":
        lab = b.get("label")
        return S.learn(explain_body(b.get("body", [])), call=b.get("call"),
                       title=None if lab in PLAIN_READ else lab, side=side)
    if t == "activity":
        return S.task(b["text"], side=side)
    if t == "worked":
        z = b.get("zero")
        return S.worked(question=b["question"], marks=b.get("marks"), lead=b.get("lead"), model=b["model"],
                        rungs=[(r["move"], r["text"]) for r in b.get("rungs", [])],
                        zero=(z["answer"], z["why"]) if z else None,
                        labels=("A full answer", "What scores nothing"), side=side)
    if t == "gapfill":
        cols = b.get("columns", ["Word", "What it means"])[:2]
        return S.compare(cols, [[r, ""] for r in b["rows"]], title=b["title"], form=True,
                         brief=b.get("prompt", ""), label="Fill in", sid=slug(b["title"]), side=side)
    if t == "formfill":
        return S.form([(r["label"], r["prompt"], r.get("lines", 1)) for r in b["rows"]],
                      title=b["title"], brief=b.get("prompt", ""), sid=slug(b["title"]), side=side)
    return None


def plain_section(b):
    """Blocks that never take a side card."""
    t = b["type"]
    if t == "guide":
        lab = b.get("label")
        work = {"title": b["work"], "embed": b["embed"], "meta": b.get("meta", ""),
                "cues": b["cues"], "note": b.get("note")}
        return S.cues([work], brief=b.get("brief", ""), title=None if lab == "Listen" else lab)
    if t == "check":
        summary = b["summary"]
        label = "If you were away" if summary.startswith("If you were away") else "Check yourself"
        return S.reveal(summary, b["items"], ordered=b.get("ordered", False), label=label)
    if t == "rubric":
        return S.rubric([(c["name"], c["bands"]) for c in b["criteria"]], bands=b.get("bandRanges", ()),
                        title=b["title"], lead=b.get("lead", ""))
    if t == "exit":
        return S.exit_ticket(b["text"])
    if t == "ideabank":
        return ideabank(b)
    if t == "wordbank":
        return wordbank(b)
    raise ValueError(f"no shell mapping for block type {t!r}")


def lesson_sections(blocks):
    """The lesson's blocks in order, as shell sections.

    Consecutive media blocks share one Listen card. A key word (definition)
    sits beside the next section that can take a side card; when the next one
    cannot (a cue sheet, a check, an exit ticket), the key words get their own
    card first. Nothing is reordered and nothing is dropped."""
    secs, defs, i = [], [], 0

    def flush():
        if defs:
            secs.append(S.section("keys", keys_label(defs), "key", None, f'<div class="keys">{keys_dl(defs)}</div>'))
            defs.clear()

    while i < len(blocks):
        b = blocks[i]
        if b["type"] == "definition":
            defs.append(b)
            i += 1
            continue
        if b["type"] == "media":
            j = i
            while j < len(blocks) and blocks[j]["type"] == "media":
                j += 1
            secs.append(S.listen([clip_of(m) for m in blocks[i:j]], side=keys_side(defs)))
            defs.clear()
            i = j
            continue
        sec = block_section(b, side=keys_side(defs))
        if sec is not None:
            defs.clear()
            secs.append(sec)
        else:
            flush()
            secs.append(plain_section(b))
        i += 1
    flush()
    return secs


# -------------------------------------------------------------- schedules


def topic_groups(course, topic):
    """Every page of a topic, grouped by week (or phase). No "Up to here": the
    Sound Detectives marker went stale when the unit finished, and the depth
    study never had one, because every student is on a different project."""
    exam_no = topic["assessment"].get("examLesson")
    groups = []
    for w in topic["weeks"]:
        rows = []
        for l in w["lessons"]:
            rows.append({"n": str(l["number"]), "title": l["title"], "meta": l["intention"],
                         "href": lesson_path(course, topic, l), "at": l["number"] == exam_no})
        groups.append((group_label(topic, w), rows, w.get("intro", "")))
    return groups


def milestones(topic):
    """The depth study's shared dates. States come from the build date and are
    worked out again by shell.js when the page opens."""
    miles = topic.get("milestones")
    if not miles:
        return ""
    rows = [{"n": str(i + 1), "title": m["what"], "meta": f'{m["when"]} · {m["detail"]}',
             "date": m["date"], "at": bool(m.get("assessed"))} for i, m in enumerate(miles)]
    # Bake the states the way shell.js will recompute them.
    today, found = date.today().isoformat(), False
    for r in rows:
        if r["date"] < today:
            r["state"] = "done"
        elif not found:
            r["state"], found = "next", True
    return S.schedule([(None, rows)], base="", label="Milestones", title="Your milestones",
                      note="Everyone's project is different. These dates are not.")


# ------------------------------------------------------------------- pages


def build_lesson(site, sh, course, topic, lesson, prev_l, next_l):
    word = page_word(topic)
    n = lesson["number"]
    total = len(flat_lessons(topic))
    where = lesson.get("where") or f"in Week {lesson['week']} of {topic['name']}"
    hd = S.head(lesson["title"], kicker=topic["name"], num=n, meta=f"{word} {n} of {total}, {where}.")
    it = S.intent(lesson["intention"], criteria=lesson["criteria"])
    secs = lesson_sections(lesson["blocks"])
    if lesson.get("teacher"):
        lis = "".join(f"<li>{S.rich(t)}</li>" for t in lesson["teacher"])
        secs.append(S.section("teacher", "Slides and notes", "list", None, f'<ul class="plain-list">{lis}</ul>'))
    body = S.lesson(hd, it, secs)

    pn = (("Previous", prev_l["title"], lesson_path(course, topic, prev_l)) if prev_l else None,
          ("Next", next_l["title"], lesson_path(course, topic, next_l)) if next_l else None)
    plural = "steps" if word == "Step" else "lessons"
    extras = S.fold(f"{topic['name']}: all {total} {plural}",
                    S.schedule(topic_groups(course, topic), base=site["base"], label=topic["name"]))
    crumbs = [("Home", "/"), (topic["name"], f"/{course['id']}/{topic['id']}/"), (f"{word} {n}", None)]
    return S.page(sh, title=f"{word} {n}: {lesson['title']}", body=body, description=lesson["intention"],
                  crumbs=crumbs, nav_current=topic["id"], prevnext=pn, extras=extras,
                  site_js=True)  # site.js carries saved answers across from before the shell


def build_topic(site, sh, course, topic):
    lessons = flat_lessons(topic)
    word = page_word(topic)
    plural = "steps" if word == "Step" else "lessons"
    hd = S.head(topic["name"], kicker=topic["term"], meta=f"{topic['subtitle']} · {len(lessons)} {plural}")
    outs = "".join(f"<li><strong>{S.e(code)}</strong> {S.rich(text)}</li>" for code, text in topic["outcomes"])
    about = S.section("about", "This unit", "learn", None, f'<p class="intent-text">{S.rich(topic["blurb"])}</p>',
                      side=S.side_card("Outcomes", "criteria", f'<ul class="plain">{outs}</ul>', cls="outcomes"))
    a = topic["assessment"]
    at = S.assessment(a["name"], due=a["when"], about=a["detail"],
                      where=a.get("note") or "The task notification and the exam itself are in Canvas.")
    sched = S.schedule(topic_groups(course, topic), base=site["base"],
                       label=f"Every {word.lower()}", title=None)
    body = hd + about + at + milestones(topic) + sched
    return S.page(sh, title=topic["name"], body=body, description=topic["blurb"],
                  crumbs=[("Home", "/"), (topic["name"], None)], nav_current=topic["id"])


def topic_cards(course, topics, open_id=None):
    cards = []
    for t in topics:
        n = len(flat_lessons(t))
        word = page_word(t).lower()
        cards.append({"title": t["name"], "href": f"/{course['id']}/{t['id']}/", "kicker": t["term"],
                      "text": t["blurb"], "meta": f"{n} {word}{'' if n == 1 else 's'}",
                      "open": t["id"] == open_id})
    return cards


def build_course(site, sh, course, topics):
    hd = S.head(course["name"], kicker=f"{course['code']} · {course['year']}", meta=course["blurb"])
    body = hd + S.card_grid(topic_cards(course, topics), base=site["base"])
    return S.page(sh, title=course["name"], body=body, description=course["blurb"],
                  crumbs=[("Home", "/"), (course["name"], None)], nav_current="home")


def build_home(site, sh, course, topics):
    """The units, newest open. There is no live position to show: Sound
    Detectives finished in Term 3, and the depth study has milestones, not a
    lesson the whole class is on."""
    hd = S.head(course["name"], kicker=f"{course['code']} · {course['year']}", meta=course["blurb"])
    body = hd + S.card_grid(topic_cards(course, topics, open_id=topics[-1]["id"]), base=site["base"])
    return S.page(sh, title=site["title"], body=body,
                  description=f"{course['name']}, lesson by lesson.", nav_current="home")


# -------------------------------------------------------------------- main


def main():
    site = load("site.json")
    S.set_base(site["base"])
    if len(site["courses"]) != 1:
        sys.exit("this build expects one course per site")
    course = load("courses", site["courses"][0], "course.json")
    topics = [load("courses", course["id"], "topics", f"{tid}.json") for tid in course["topics"]]
    nav = [("Home", "/", "home")] + [(t["name"], f"/{course['id']}/{t['id']}/", t["id"]) for t in topics]
    sh = shell_site(site, nav)

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    pages = 0
    cid = course["id"]
    for topic in topics:
        write([cid, topic["id"], "index.html"], build_topic(site, sh, course, topic))
        pages += 1
        lessons = flat_lessons(topic)
        for i, lesson in enumerate(lessons):
            write([cid, topic["id"], f"{page_slug(topic)}-{lesson['number']}", "index.html"],
                  build_lesson(site, sh, course, topic, lesson,
                               lessons[i - 1] if i else None,
                               lessons[i + 1] if i + 1 < len(lessons) else None))
            pages += 1
    write([cid, "index.html"], build_course(site, sh, course, topics))
    write(["index.html"], build_home(site, sh, course, topics))
    pages += 2

    shutil.copytree(ASSETS, os.path.join(OUT, "assets"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    missing = sum(1 for t in topics for l in flat_lessons(t) for b in l["blocks"]
                  if b["type"] == "media" and not b["embed"] and not b.get("studentSupplied"))
    print(f"built {pages} pages into docs/")
    if missing:
        print(f"  {missing} listening slots still have no recording")


if __name__ == "__main__":
    main()
