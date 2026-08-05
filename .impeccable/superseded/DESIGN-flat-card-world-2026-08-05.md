---
name: Mr Edwards | Class Material
description: A multi-course teaching site where the registered lesson sequence and the class's real position are shown together.
colors:
  course: "#00695C"
  ink: "#1a1a1a"
  ink-2: "#4a4a4a"
  paper: "#ffffff"
  ground: "#f4f6f7"
  line: "#dce1e3"
  now: "#b25e00"
  now-bg: "#fff6e8"
  now-line: "#e8b877"
  done: "#52605f"
  chip-done-bg: "#e7ebeb"
  chip-ahead-bg: "#eef1f2"
  surface-def: "#f7fbfa"
  surface-quiet: "#f7f9f9"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 5vw, 3.25rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "clamp(1.75rem, 4vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  title:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "1.375rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "normal"
  subtitle:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "normal"
  lede:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.65
  body:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  deck:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  body-small:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.65
  fine:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.65
  chip:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "0.75rem"
    fontWeight: 700
    letterSpacing: "0.04em"
  chip-lg:
    fontFamily: "{typography.display.fontFamily}"
    fontSize: "0.8125rem"
    fontWeight: 700
rounded:
  r: "10px"
  r-sm: "6px"
  pill: "999px"
spacing:
  xs: "0.4rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.25rem"
  xl: "1.75rem"
  xxl: "2.5rem"
components:
  card-lesson:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.r}"
    padding: "1rem 1.1rem 1.1rem"
  card-lesson-now:
    backgroundColor: "{colors.now-bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.r}"
    padding: "calc(1rem - 1px) calc(1.1rem - 1px) calc(1.1rem - 1px)"
  panel-position:
    backgroundColor: "{colors.now-bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.r}"
    padding: "1.1rem 1.25rem"
  hero-course:
    backgroundColor: "{colors.course}"
    textColor: "{colors.paper}"
    typography: "{typography.display}"
    padding: "2.75rem 0 3rem"
  aside-panel:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.r}"
    padding: "1.1rem 1.25rem"
  chip-now:
    backgroundColor: "{colors.now}"
    textColor: "{colors.paper}"
    typography: "{typography.chip}"
    rounded: "{rounded.pill}"
    padding: "0.15rem 0.5rem"
  chip-done:
    backgroundColor: "{colors.chip-done-bg}"
    textColor: "{colors.done}"
    typography: "{typography.chip}"
    rounded: "{rounded.pill}"
    padding: "0.15rem 0.5rem"
  chip-ahead:
    backgroundColor: "{colors.chip-ahead-bg}"
    textColor: "{colors.ink-2}"
    typography: "{typography.chip}"
    rounded: "{rounded.pill}"
    padding: "0.15rem 0.5rem"
  flag-here:
    backgroundColor: "{colors.now}"
    textColor: "{colors.paper}"
    typography: "{typography.body-small}"
    rounded: "{rounded.r-sm}"
    padding: "0.3rem 0.75rem"
---

# Design System: Mr Edwards | Class Material

## Overview

**Creative North Star: "The Clean Course Site"**

This is the category standard executed at full fidelity, and that is a standing decision rather than a fallback. The reference points are BBC Bitesize and Khan Academy: an unambiguous course to topic to lesson hierarchy with breadcrumbs on every page, one colour that identifies the course at a glance, short scannable lesson pages, and generous type at a size a fifteen-year-old can read across a projected screen. Nothing here is trying to be novel. The whole system's distinctiveness is a two-colour split, and it should stay that way as more courses arrive.

The world is a light grey ground carrying white cards with a soft two-layer shadow and a 10px radius. Type is the operating system's own sans at 17px with a 1.65 line height, which is a deliberate choice made against a self-hosted face: nothing in this project may rot unattended, and school devices must render it identically without a webfont round trip. There is exactly one branded surface per page, the course-colour hero, and everything below it is white on grey.

The one idea the system owns is the colour split. A single course colour owns the hero, every link, and the definition terms. A single amber owns position, meaning the "we are up to" panel, the current lesson card, the current week's heading, and the on-page here flag. Neither colour crosses into the other's job. With all the content removed, the page is still recognisable from that split alone. This is a platform, not a site: it currently ships one course and one topic, but it was built to carry every class and to roll over each year.

**Key Characteristics:**
- Light grey ground (`#f4f6f7`), white cards, 10px radius, soft ambient shadow.
- System sans throughout at 17px base, 1.65 line height, no webfont.
- One course colour and one amber; each owns a single job.
- Breadcrumb on every page below the top level; hierarchy is never implied.
- No uppercase letterspaced micro-labels anywhere on the site.
- Status is carried by a worded chip, never by colour alone.

## Colors

A near-neutral cool grey base carrying two saturated signals: the course's own colour and one amber that means "here".

### Primary
- **Course Teal** (`#00695C` for Year 10 Music): the per-course identity. It fills the full-bleed hero, colours every body link, card link, topic and course name, the definition term, and the focus ring. It is supplied by the `--course` custom property and by nothing else.

### Secondary
- **Position Amber** (`#b25e00`): the class's real position in the sequence, and only that. It colours the "we are up to" jump line, the current week's heading, the "Up to here" chip, the here flag on the lesson page, and the "Up to" label on the course and home cards.
- **Amber Wash** (`#fff6e8`) and **Amber Edge** (`#e8b877`): the fill and border of any surface marking position, namely the jump panel and the current lesson card.

### Neutral
- **Ink** (`#1a1a1a`): body text, headings, current breadcrumb, card body on tinted surfaces.
- **Muted Ink** (`#4a4a4a`): secondary prose, week titles and intros, card intentions, breadcrumb links, aside body, footer.
- **Paper** (`#ffffff`): every card, panel, aside, masthead, breadcrumb bar and footer.
- **Ground** (`#f4f6f7`): the page background behind all cards.
- **Line** (`#dce1e3`): every card and panel border, and the masthead, breadcrumb and footer rules.
- **Taught Grey** (`#52605f` on `#e7ebeb`): the "Taught" chip. **Coming Up Grey** (`#4a4a4a` on `#eef1f2`): the "Coming up" chip.
- **Tinted surfaces**: definition blocks sit on a barely-there course-tinted white (`#f7fbfa`); teacher notes and exit tickets sit on a barely-there neutral white (`#f7f9f9`, `#fafbfb`). These are whispers, not colours.

### Named Rules

**The One Lever Rule.** A new course supplies `--course` and nothing else. No new palette, no per-course type, no per-course component. Set it in the page's inline `:root` block (and on the `.ccard` list item on the home page) and the hero, links, card titles, definition terms and focus ring all follow. If adding a course needs a second decision, the system has been broken.

**The Two Jobs Rule.** The course colour identifies the course. The amber identifies position. Neither is ever used for the other's job, and no third accent is introduced. Audit test: cover the content of any page; if you can still tell which course it is and where the class is, the split is intact.

**The Never Colour Alone Rule.** Position and lesson status are always carried by words as well as colour: "Up to here", "Taught", "Coming up", "This is the lesson we are up to". A colour change is never the only signal, because access provisions and projection both defeat it.

## Typography

**Display Font:** the system UI stack (`-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial`, sans-serif)
**Body Font:** the same stack. There is one family in this system.

**Character:** plainly institutional and completely unbranded, which is the point. The stack is a durable decision, not a placeholder: the project must survive with no maintenance and no build dependency, and school devices must render it instantly and identically. Do not replace it with a self-hosted or CDN face.

### Hierarchy
- **Display** (700, `clamp(2rem, 5vw, 3.25rem)`, line-height 1.2, `-0.02em`): the course or topic name in the full-bleed hero. One per page, maximum.
- **Headline** (700, `clamp(1.75rem, 4vw, 2.5rem)`, `-0.02em`): the lesson page `h1` and the home page `h1`, both of which sit on white rather than in a hero.
- **Title** (700, 1.375rem / 22px): week headings, topic and course card names, and the lesson number inside the jump line.
- **Subtitle** (700, 1.25rem / 20px): lesson content block headings ("What we are doing", "Your task") and the jump panel's lesson title.
- **Lede** (400, 1.125rem / 18px, max 62ch): the hero blurb and the home page intro.
- **Body** (400, 1.0625rem / 17px, line-height 1.65): all running prose, card links, aside headings. Prose measures are capped at 62–70ch on wide surfaces and the lesson page itself is capped at 40rem.
- **Small** (400, 0.9375rem / 15px): card learning intentions, aside body, media briefs, teacher notes, the here flag.
- **Fine** (400, 0.875rem / 14px): breadcrumbs, masthead subtitle, footer.
- **Chip** (700, 0.75rem / 12px, `0.04em`, sentence case): status chips only.

### Named Rules

**The No Micro-Label Rule.** No uppercase letterspaced micro-labels anywhere. No kickers, no eyebrows, no all-caps section tags above headings. Nine were built and removed at the finish review; two survived only by being rewritten as real sentences and relocated below their heading, because they carried information a reader needed. If a label seems necessary, either the heading is not saying enough or the label is decoration. The status chips are the single exception and they are sentence case, worded, and attached to a lesson rather than floating above a heading.

**The One Family Rule.** One font family, one weight pair (400 and 700). No 500 or 600 display weights, no italic display, no second face for headings. Emphasis comes from size and colour.

## Layout

A single centred container (`max-width: 1120px`, `1.25rem` side padding) governs every page. The lesson page narrows further to `40rem` inside that container, because a lesson is read, not scanned.

Every page runs the same vertical spine: masthead, breadcrumb bar, then either a full-bleed course-colour hero (course and topic pages) or a white page head (home and lesson pages), then body on the grey ground, then footer.

The topic page is the system's densest surface. Its first viewport is breadcrumb, hero, then the amber position panel pulled up by `-3.6rem` so it overlaps the hero's bottom edge, then Week 1. Below that, a two-column grid appears at `62rem`: lessons on the left, a sticky `20rem` sidebar of assessment and outcomes on the right, sticking at `1.25rem` from the top. Below `62rem` the sidebar drops beneath the lessons.

Lesson cards are a three-up grid from `40rem` and stack below it. Topic and course cards are two-up from `44rem`. The lesson page's learning-intentions pair and its previous/next navigation both split to two columns at `40rem`.

Breakpoints, all rem-based so they respond to text scaling: `40rem`, `44rem`, `62rem`.

Vertical rhythm: `1rem` between cards in a grid, `1.75rem` between lesson content blocks, `2.5rem` between weeks and before the teacher-notes and previous/next blocks. Panel padding is `1.1rem 1.25rem`; card padding is `1rem 1.1rem 1.1rem`.

## Elevation & Depth

Cards float, barely. Every white surface carries the same two-layer ambient shadow at rest, and the only state change in the system is that shadow deepening on hover. There is no colour change, no lift transform, no border change on hover. Depth is ambient, not structural: it separates the card from the grey ground and nothing more.

### Shadow Vocabulary
- **Rest** (`box-shadow: 0 1px 2px rgba(16,24,32,.06), 0 4px 12px rgba(16,24,32,.06)`): every card, panel, aside and previous/next block.
- **Lift** (`box-shadow: 0 2px 4px rgba(16,24,32,.08), 0 10px 24px rgba(16,24,32,.10)`): the hover state of anything that is a link target.

Transition: `box-shadow .18s cubic-bezier(.22, 1, .36, 1)`, and only box-shadow. All transitions are disabled under `prefers-reduced-motion: reduce`.

### Named Rules

**The Shadow-Only Hover Rule.** Hover changes the shadow and, on lesson cards, thickens the link underline to 2px. It never moves the card, changes its background, or changes its border. If a surface is not clickable, it never lifts.

**The One Shadow Rule.** Two shadow values exist and no more. Nothing in this system uses a hard offset shadow, an inner shadow, or a glow.

## Shapes

Everything is a soft rectangle. The card radius is 10px (`--r`) and it applies to every card, panel, aside, video frame, empty-state block and previous/next tile without exception. A 6px radius (`--r-sm`) is reserved for small solid blocks: the here flag and the skip link. Status chips are fully rounded pills (999px).

Borders are 1px hairlines in `#dce1e3`. Two deliberate departures: the current lesson card takes a 2px amber border with its padding reduced by 1px so it does not shift in the grid, and the empty listening block takes a 1px dashed grey border to read as unfinished rather than empty.

The hero is the only full-bleed element and it is a flat colour block with a hard bottom edge, which the amber position panel then overlaps.

## Components

### Cards (lesson)
Flat white tiles in a three-up grid, each a whole-card click target.
- **Corner Style:** 10px.
- **Background:** paper on ground; amber wash when current.
- **Shadow Strategy:** rest shadow, lift on hover.
- **Border:** 1px `#dce1e3`; 2px `#e8b877` when current.
- **Internal Padding:** `1rem 1.1rem 1.1rem`.
- **Content order:** underlined course-colour title ("Lesson 6. Title"), the learning intention in muted 15px, then a status chip pinned to the bottom by a flex spacer.
- **Behaviour:** the title link carries a full-card `::after` overlay so the entire card is clickable while the accessible name stays the lesson title.

### Cards (topic and course)
Larger two-up tiles with the same shape and shadow. A 22px underlined course-colour name, a muted term or course code line, a short blurb, then the position line: an amber "Up to" label followed by an ink underlined link straight to the current lesson.

### Position Panel
The signature component. An amber-washed, amber-bordered 10px panel that sits on the topic page pulled up over the hero's bottom edge, and is itself a link to the current lesson. Three stacked grid rows: "We are up to **Lesson 6** of 30" in amber (the number at 22px), the lesson title at 20px underlined, then a muted note carrying the date, period and lessons completed. This is where the registered sequence and the class's real position meet, and it is the reason the site exists.

### Status Chips
Small sentence-case pills, 12px 700 with `0.04em` tracking, `0.15rem 0.5rem` padding.
- **Up to here:** white on amber.
- **Taught:** `#52605f` on `#e7ebeb`.
- **Coming up:** muted ink on `#eef1f2`.

### Here Flag
On the current lesson's own page, a solid amber 6px-radius block reading "This is the lesson we are up to", directly under the lesson subtitle. It states the fact in words; it is not a badge.

### Lesson Content Blocks
A vertical stack of sections at `1.75rem` intervals, each with a 20px heading. Three block types get a card treatment (10px, hairline border, rest shadow): the definition block on a faint course tint with the term in the course colour, the task block on white with a slightly warmer border and a course-colour heading, and the exit ticket on a faint neutral tint with a smaller heading. Step lists are plain ordered lists with roomy items. The video frame is a 16:9 padded box with a near-black fill and clipped 10px corners.

### Asides
Assessment, outcomes and teacher notes share one shape: white, hairline, 10px, `1.1rem 1.25rem`, 17px heading, 15px muted body. On the topic page the assessment and outcomes asides live in the sticky sidebar; teacher notes sit at the foot of a lesson page on a faintly tinted ground.

### Navigation
- **Masthead:** white bar, hairline bottom rule, baseline-aligned. Bold 17px ink brand link that underlines on hover, then a 14px muted school name. No logo and no school brand assets, by product constraint.
- **Breadcrumbs:** white bar below the masthead, hairline bottom, 14px muted links separated by a `›` glyph, current page in ink at weight 600 with `aria-current="page"`. Present on every page below the home page.
- **Previous / Next:** paired white tiles at the foot of a lesson page, a muted "Previous"/"Next" line above a course-colour underlined lesson title, right-aligned on the next tile. A lone next tile is pushed to the second column.
- **Skip link:** offscreen until focused, then a solid ink block at the top left.

### Focus
A single global treatment: `3px solid var(--course)` at `2px` offset with a `3px` radius, on everything. It changes colour with the course and is never removed.

## Do's and Don'ts

### Do:
- **Do** add a new course by setting `--course` to one colour and nothing else. Everything that identifies the course follows from it.
- **Do** keep the amber for position only, and always pair it with words ("Up to here", "This is the lesson we are up to").
- **Do** use the system font stack. It is chosen so the site cannot rot and school devices render it instantly.
- **Do** give every card and panel the same 10px radius, hairline border, and rest shadow, so a new block type inherits the world for free.
- **Do** put a breadcrumb on every page below the home page, and give prose a measure (62ch for ledes, 70ch for intros, 40rem for a whole lesson page).
- **Do** check the course colour against white for WCAG AA before shipping it; the hero, links and focus ring all depend on it.

### Don't:
- **Don't** add uppercase letterspaced micro-labels, kickers or eyebrows anywhere. If a heading needs a label above it, rewrite the heading.
- **Don't** introduce a third accent colour, a per-course typeface, or a per-course component. The colour split is the entire visual signature.
- **Don't** self-host or CDN-load a webfont, and don't add any dependency that needs maintenance.
- **Don't** move, recolour or re-border a card on hover. Hover deepens the shadow, and that is the whole interaction vocabulary.
- **Don't** convey position or status by colour alone.
- **Don't** apply school branding, logos or letterhead. The site's identity is its own, by product constraint.
- **Don't** style content-specific one-offs. Anything built for Sound Detectives must work unchanged for the next topic and the next course.
