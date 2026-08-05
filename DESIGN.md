---
name: Year 10 Music class site
description: A hand-drawn zine of a class dashboard, where today's lesson is poster-sized and the term is a filmstrip
colors:
  paper: "#FFF8EC"
  ink: "#111111"
  soft-ink: "#5A544A"
  highlight-yellow: "#FFE34D"
  highlight-pink: "#FF6BAE"
  highlight-teal: "#00C7B7"
  teal-wash: "#B9ECE7"
typography:
  display:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "clamp(2.8rem, 7vw, 5.2rem)"
    fontWeight: 400
    lineHeight: 1.05
  display-cover:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "clamp(2.7rem, 7.5vw, 5.5rem)"
    fontWeight: 400
    lineHeight: 1.02
  display-lesson:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "clamp(2.4rem, 6vw, 4.4rem)"
    fontWeight: 400
    lineHeight: 1
  display-home:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "clamp(2.2rem, 5vw, 3.4rem)"
    fontWeight: 400
  counter:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "2.1rem"
    fontWeight: 400
    lineHeight: 1.1
  brand:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "1.65rem"
    fontWeight: 400
  headline:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "1.45rem"
    fontWeight: 400
    lineHeight: 1.15
  button:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "1.35rem"
    fontWeight: 400
  title:
    fontFamily: "Atkinson Hyperlegible, Trebuchet MS, sans-serif"
    fontSize: "clamp(1.3rem, 2.6vw, 1.8rem)"
    fontWeight: 700
  title-lesson:
    fontFamily: "Atkinson Hyperlegible, Trebuchet MS, sans-serif"
    fontSize: "clamp(1.5rem, 3.4vw, 2.3rem)"
    fontWeight: 700
  subtitle:
    fontFamily: "Atkinson Hyperlegible, Trebuchet MS, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 700
  body:
    fontFamily: "Atkinson Hyperlegible, Trebuchet MS, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  note:
    fontFamily: "Caveat, Bradley Hand, cursive"
    fontSize: "1.35rem"
    fontWeight: 400
    lineHeight: 1.3
  note-compact:
    fontFamily: "Caveat, Bradley Hand, cursive"
    fontSize: "1.25rem"
    fontWeight: 400
  label:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "1rem"
    fontWeight: 400
    letterSpacing: "0.02em"
  label-large:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "1.05rem"
    fontWeight: 400
    letterSpacing: "0.02em"
  small:
    fontFamily: "Atkinson Hyperlegible, Trebuchet MS, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 400
  label-micro:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "0.85rem"
    fontWeight: 400
  flag:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "0.72rem"
    fontWeight: 400
spacing:
  block: "2.3rem"
  panel-gap: "1.6rem"
  panel-pad: "1.4rem 1.5rem 1.5rem"
components:
  button-primary:
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    padding: "0.42em 1.3em 0.48em"
  tab-label:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "0.18em 0.8em 0.22em"
  panel:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "{spacing.panel-pad}"
---

# Design System: Year 10 Music class site

## Overview

**Creative North Star: "A mate's brilliant annotated notes"**

The whole site is one hand-drawn technical zine: cream paper, black marker ink, and exactly three highlighters. Every surface reads as if a sharp Year 10 student drew the page: wobbly inked panel borders, torn-edged highlighter swipes, doodle arrows hopping between panels, a scratchy crow mascot, and marker-lettered labels stuck on at a slight angle. The energy is playful but the reading experience is disciplined; the marker face carries labels and numbers, and everything students actually read is set in a hyperlegible sans.

Nothing on the page is flat-vector tidy. Highlighter fills carry rough SVG edges with the ink outline drawn into the torn edge itself, borders wobble through three different radius sets so neighbours never match, and labels rotate a degree or two off level. Depth is almost entirely line work; the page is flat paper.

**Key Characteristics:**
- Cream paper ground with black ink and three flat highlighter colours, nothing else
- Hand-inked wobbly borders and rough-edged marker swipes, never straight-edged fills
- Marker display type for labels and numbers, hyperlegible sans for content, Caveat for margin notes
- The class's live position is the loudest thing on every surface
- Doodle SVG vocabulary (arrows, crosses, rings, stars, clock, notes) that draws itself on scroll

## Colors

Paper and ink do the work; the three highlighters are meaning, not decoration.

### Primary
- **Marker Ink** (#111111): all text, all borders, every doodle stroke. The system's single voice.
- **Cream Paper** (#FFF8EC): the only ground. Panels, page, and mascot rasters share it exactly, so images sit borderless on the page.

### Secondary
- **Highlighter Yellow** (#FFE34D): the position colour. Current lesson swipes, the primary button, the "We are up to" jump panel, learning-intention labels.
- **Highlighter Pink** (#FF6BAE): the warning colour. Exam frames and flags, assessment labels, success-criteria strips, before-you-leave tabs.
- **Highlighter Teal** (#00C7B7): the identity colour. Panel tabs, key-word labels, focus rings, the TODAY panel's outer wash (as **Teal Wash** #B9ECE7).

### Neutral
- **Soft Ink** (#5A544A): margin notes, secondary lines, done-state text. Always the Caveat or body face, never borders.

### Named Rules
**The Three Highlighters Rule.** Yellow means where we are, pink means what is coming for you, teal names things. No fourth accent exists, and a highlighter never swaps jobs.
**The Torn Edge Rule.** A highlighter fill is a rough-edged SVG swipe with its ink outline drawn in the same SVG. A straight-edged flat rectangle of colour is a defect.

## Typography

**Display Font:** Permanent Marker (with Comic Sans MS, cursive fallback)
**Body Font:** Atkinson Hyperlegible (with Trebuchet MS fallback)
**Note Font:** Caveat (with Bradley Hand fallback)

**Character:** A confident marker voice for the things the page shouts (lesson numbers, labels, buttons), a deliberately hyperlegible sans for everything students read with a pen in hand, and a handwritten margin voice for asides. All three are self-hosted woff2 files; nothing loads from a CDN.

### Hierarchy
- **Display family** (400, marker): four clamped steps, one per surface. Dashboard lesson number clamp(2.8rem, 7vw, 5.2rem); topic cover clamp(2.7rem, 7.5vw, 5.5rem); lesson-page number clamp(2.4rem, 6vw, 4.4rem); course/home heading clamp(2.2rem, 5vw, 3.4rem). One display per page.
- **Counter** (400, 2.1rem, marker): the exam countdown line only.
- **Brand** (400, 1.65rem, marker; 1.35rem below 44rem): the masthead wordmark.
- **Headline** (400, 1.45rem, marker): section headings, week tabs' titles, card names, the jump line.
- **Button** (400, 1.35rem, marker): the primary action.
- **Title** (700, clamp(1.3rem, 2.6vw, 1.8rem), sans) and **Title-lesson** (700, clamp(1.5rem, 3.4vw, 2.3rem)): lesson titles on dashboard and lesson pages.
- **Subtitle** (700, 1.15rem, sans): week titles, ledes, jump titles, cover subtitles.
- **Body** (400, 1.0625rem, 1.6): all content. Prose measures cap at 68 to 70ch.
- **Note** (400, 1.35rem, Caveat) and **Note-compact** (400, 1.25rem): margin voice; compact for breadcrumbs, prev/next kickers and row marks.
- **Label** (400, 1rem, 0.02em, marker), **Label-large** (1.05rem), **Label-micro** (0.85rem), **Flag** (0.72rem): tab blocks, nav links and row numbers, mini-callout labels, the filmstrip EXAM flag.
- **Small** (400, 0.95rem, sans): secondary lines inside cards and rows.

### Named Rules
**The Marker Shouts, The Sans Explains Rule.** Permanent Marker never sets a sentence students must read carefully; anything longer than a label drops to Atkinson Hyperlegible.

## Layout

A 72rem wrapped page. The dashboard is a comic page: a two-thirds TODAY panel beside a one-third rail (LAST TIME, COMING UP, exam countdown), with the 30-frame filmstrip full width beneath and doodle arrows crossing the gutters. Lesson pages run a single 52rem column. Panels sit 1.6rem apart; content blocks step at 2.3rem; a panel's tab overlaps its top border by about 1rem, so panels always carry top clearance.

Breakpoints at 44rem and 62rem, both rem-based. Below 62rem the dashboard stacks and the filmstrip becomes a scroller with a handwritten "slide for more →" hint and auto-centres the current frame; below 44rem the TODAY panel goes single column and the crow tucks under the text.

## Elevation & Depth

Flat paper, drawn depth. There are no resting shadows anywhere; separation comes from inked borders and the paper itself. Exactly two depth devices exist: the TODAY panel's 6px teal wash (a solid `box-shadow: 0 0 0 6px #B9ECE7` ring, colour not depth), and a hard ink-tinted offset (`3px 4px 0 rgba(17,17,17,0.16)`, as drop-shadow on rough-fill elements) that appears only on hover of a link target.

### Named Rules
**The Drawn Depth Rule.** If something needs to stand out, it gets more ink or a highlighter swipe, never a soft shadow.

## Shapes

Every container is a hand-inked rectangle. Borders are 2.5 to 3px solid ink with one of three wobble radius sets (`--wob-a/b/c`), assigned so adjacent panels never share an outline. Rough-fill elements (tabs, buttons, swipes, the jump panel) take no CSS border at all; their outline lives in the SVG's torn edge. Small marks are irregular circles (step numbers), a jagged 16-point starburst (learning intention), and squarish wobble frames (filmstrip). The empty listening slot is the one dashed border in the system, meaning "not finished yet".

## Components

### Panels
The page's building block: paper fill, wobbly ink border, a marker tab overlapping the top-left corner.
- **Corner Style:** one of the three wobble sets, rotated through siblings.
- **Tab:** torn-edge SVG block (teal by default, yellow for position, pink for assessment) rotated ±2deg.
- **Internal Padding:** 1.4rem 1.5rem 1.5rem, plus ~0.3rem top clearance for the tab.

### Buttons
- **Shape:** rough marker block, ink outline in the SVG edge, rotated -1deg at rest.
- **Primary:** yellow fill, marker caps at 1.35rem, ink text (0.42em 1.3em padding).
- **Hover / Focus:** straightens to 0deg, scales 1.04, gains the hard ink offset and two hand-drawn emphasis dash marks either side.

### Highlighter swipes
Inline `.hl/.hl-pink/.hl-teal` spans with rough SVG fills, `box-decoration-break: clone` so wrapped lines each get torn ends. The `.uline` variant is a rough yellow underline swipe for headline emphasis.

### Filmstrip
The term at a glance: 30 numbered wobble frames, flex edge-to-edge on desktop. Done frames carry a hand-drawn X and soft-ink numbers, the current frame is yellow with a rough ring overhanging its box, the exam frame is pink with a rotated EXAM flag above. Every frame is a link with a full aria-label; state is never colour alone (X, ring, flag carry it).

### Position grammar
One vocabulary on every surface: done = strikethrough title plus "done ✓" in Caveat; current = yellow rough swipe plus "← we are here"; exam = pink plus flag. The topic page's jump panel ("We are up to Lesson N of 30") is the same yellow at panel scale.

### Doodles
An inlined SVG set generated by build.py: X_MARK, RING, CHECK, NOTE, CLOCK, ARROW_DOWN, ARROW_POINT, ARROW_HOP, STAR, DOT. All stroke `currentColor`-equivalent ink at 2.2 to 3.6 width, round caps. Arrows carry `.draw-on` and draw themselves via stroke-dashoffset when 40% visible (IntersectionObserver); under `prefers-reduced-motion: reduce` they render pre-drawn and all transitions stop.

### Crow mascot
Scratchy black-ink raster poses (head for the masthead, headphones for the dashboard, deerstalker for Sound Detectives), generated on the exact paper colour and background-normalised to #FFF8EC so they sit borderless. New poses must keep the same scratchy pen character and exact paper ground.

### Inputs
Success-criteria checkboxes: hand-inked wobble squares (appearance: none), ticked with an oversized hand-drawn check that overshoots the box; ticked items grey to soft ink. State persists per lesson in localStorage; the page works fully without it.

### Navigation
Masthead: crow head, marker wordmark, marker-caps links right; 3px ink rule below. Breadcrumbs in Caveat with "→" separators, current page bold ink with `aria-current`. Focus everywhere is a 3px teal outline at 2px offset, never removed.

## Do's and Don'ts

### Do:
- **Do** give every new container a wobbly ink border in one of the three radius sets, and vary the set between neighbours.
- **Do** carry position with words and marks ("← we are here", the X, the ring), never colour alone.
- **Do** keep prose in Atkinson Hyperlegible at a 68 to 70ch measure, and margin commentary in Caveat.
- **Do** draw new icons in the doodle grammar: single ink stroke, round caps, slightly wrong on purpose.
- **Do** keep every asset self-hosted; the site must survive unattended for years.

### Don't:
- **Don't** ship a straight-edged rectangle of highlighter colour; every fill is a torn-edge SVG swipe.
- **Don't** add a fourth accent colour or reassign a highlighter's meaning.
- **Don't** use resting shadows, gradients, or glass; depth is drawn in ink.
- **Don't** put school branding, logos, letterhead or even the school's name anywhere; the site is anonymous by decision, and the crow and the marker voice are the identity.
- **Don't** let Permanent Marker set body copy, and don't uppercase-track labels outside the torn-edge tab blocks.
- **Don't** animate anything except the authored draw-on doodles and the button's hover straighten, and always honour reduced motion.
