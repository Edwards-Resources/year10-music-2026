#!/usr/bin/env python3
"""Pull the Sound Detectives lessons out of the old Canvas HTML pages into lesson data.

One-time import. The JSON in data/ is the source of truth from here on; this script
exists so the import can be re-run if the Canvas pages are corrected before we cut over.

Usage:  python3 tools/extract_canvas.py "<path to Term 3 - Sound Detectives folder>"
"""

import html
import json
import os
import re
import sys

# Style fingerprints from the Canvas pages, which were built from one template.
LESSON_BAR = re.compile(r'font-size:18px;font-weight:bold;">(.*?)</span>', re.S)
BLOCK = re.compile(r'<div style="([^"]*)"[^>]*>(.*?)</div>', re.S)

META_NOISE = (
    "delete before publishing",
    "delete this box",
    "find a clip and check it",
    "in canvas: click here",
    "paste the embed",
    "<iframe",
    "youtube.com/embed",
    "insert ",
)


def text_of(fragment):
    """Strip tags, unescape entities, normalise whitespace, remove em dashes."""
    t = re.sub(r"<br\s*/?>", "\n", fragment)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = t.replace("—", ", ").replace("–", "-")
    t = re.sub(r"[ \t]+", " ", t)
    return "\n".join(line.strip() for line in t.split("\n")).strip()


def list_items(fragment):
    return [text_of(m) for m in re.findall(r"<li[^>]*>(.*?)</li>", fragment, re.S)]


def is_noise(s):
    low = s.lower()
    return any(n in low for n in META_NOISE)


def tidy_title(t):
    t = text_of(t)
    t = t.replace("·", "|")
    parts = [p.strip() for p in t.split("|", 1)]
    num = int(re.search(r"(\d+)", parts[0]).group(1))
    title = parts[1] if len(parts) > 1 else parts[0]
    title = title.replace(" & ", " and ")
    return num, title[0].upper() + title[1:]


def parse_week(path, week_no):
    raw = open(path, encoding="utf-8").read()

    week_title = text_of(re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.S).group(1))
    week_title = re.sub(r"^.*?Week \d+:\s*", "", week_title).replace(" & ", " and ")

    intro_m = re.search(r"</h2><p[^>]*>(.*?)</p>", raw, re.S)
    week_intro = text_of(intro_m.group(1)) if intro_m else ""

    # Split the page into one chunk per lesson.
    marks = [(m.start(), m.group(1)) for m in LESSON_BAR.finditer(raw)]
    lessons = []
    for i, (pos, bar) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(raw)
        chunk = raw[pos:end]
        num, title = tidy_title(bar)

        lesson = {
            "number": num,
            "week": week_no,
            "title": title,
            "intention": "",
            "criteria": [],
            "blocks": [],
            "teacher": [],
        }

        # "What we are doing" sits outside a styled div, so take it first and
        # remember where, so the ordered blocks can be slotted around it.
        steps_m = re.search(
            r"<strong>What we are doing</strong></p><ol[^>]*>(.*?)</ol>", chunk, re.S
        )
        steps = list_items(steps_m.group(1)) if steps_m else []
        steps_at = steps_m.start() if steps_m else None

        video_n = 0
        for m in BLOCK.finditer(chunk):
            style, body = m.group(1), m.group(2)
            label_m = re.search(r"<strong[^>]*>(.*?)</strong>", body, re.S)
            label = text_of(label_m.group(1)) if label_m else ""
            rest = text_of(re.sub(r"<strong[^>]*>.*?</strong>", "", body, count=1, flags=re.S))
            rest = "\n".join(l for l in rest.split("\n") if l and not is_noise(l)).strip()
            rest = rest.lstrip(",").strip()

            if steps_at is not None and m.start() > steps_at and steps:
                lesson["blocks"].append(
                    {"type": "steps", "title": "What we are doing", "items": steps}
                )
                steps = []

            if "#2E5496" in style:
                lesson["intention"] = rest
            elif "#2E7D32" in style:
                lesson["criteria"] = list_items(body)
            elif "#eef1f7" in style and "Slides" in label:
                if rest:
                    lesson["teacher"].append(rest)
            elif "dashed #888" in style:
                video_n += 1
                lesson["blocks"].append(
                    {
                        "type": "media",
                        "n": video_n,
                        "brief": rest,
                        "embed": None,
                    }
                )
            elif "#C77A12" in style and label.lower() == "activity":
                lesson["blocks"].append({"type": "activity", "text": rest})
            elif "#C77A12" in style:
                lesson["blocks"].append({"type": "definition", "term": label, "text": rest})
            elif "dashed #999" in style and "Exit ticket" in label:
                lesson["blocks"].append({"type": "exit", "text": rest.lstrip("- ").strip()})
            elif "Teacher note" in label or is_noise(label):
                if rest and not is_noise(rest):
                    lesson["teacher"].append(rest)

        if steps:  # no styled block came after the steps
            lesson["blocks"].append(
                {"type": "steps", "title": "What we are doing", "items": steps}
            )

        lessons.append(lesson)

    return {"number": week_no, "title": week_title, "intro": week_intro, "lessons": lessons}


def main():
    src = sys.argv[1]
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    os.makedirs(out_dir, exist_ok=True)

    weeks = []
    for name in os.listdir(src):
        m = re.match(r"Canvas - Y10 Music Term 3 Week (\d+) ", name)
        if m:
            weeks.append((int(m.group(1)), os.path.join(src, name)))
    weeks.sort()

    parsed = [parse_week(path, n) for n, path in weeks]

    total = sum(len(w["lessons"]) for w in parsed)
    missing = sum(
        1 for w in parsed for l in w["lessons"] for b in l["blocks"]
        if b["type"] == "media" and not b["embed"]
    )
    no_intention = [l["number"] for w in parsed for l in w["lessons"] if not l["intention"]]

    with open(os.path.join(out_dir, "sound-detectives.json"), "w", encoding="utf-8") as f:
        json.dump({"weeks": parsed}, f, indent=2, ensure_ascii=False)

    print(f"weeks: {len(parsed)}  lessons: {total}  media slots without an embed: {missing}")
    if no_intention:
        print(f"  lessons missing a learning intention: {no_intention}")


if __name__ == "__main__":
    main()
