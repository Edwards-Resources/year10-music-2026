/* Small, dependency-free enhancements. The site works fully without this file. */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Exam countdown: [data-exam-date] holds an ISO date; the baked-in text stays
     as the fallback when JS never runs. */
  document.querySelectorAll("[data-exam-date]").forEach(function (el) {
    var exam = new Date(el.getAttribute("data-exam-date") + "T00:00:00");
    var today = new Date();
    today.setHours(0, 0, 0, 0);
    var days = Math.round((exam - today) / 86400000);
    var out;
    if (days > 1) out = "Exam in " + days + " days";
    else if (days === 1) out = "Exam tomorrow!";
    else if (days === 0) out = "Exam TODAY";
    else return; // Past: keep the baked-in date text rather than counting up.
    el.textContent = out;
  });

  /* Milestones: the baked-in states come from the build date, and this page can
     sit for weeks between rebuilds. Recompute from [data-mile-date] at view
     time so "next up" is never pointing at a date that has already gone. */
  var miles = document.querySelectorAll(".mile[data-mile-date]");
  if (miles.length) {
    var noon = new Date();
    noon.setHours(0, 0, 0, 0);
    var foundNext = false;
    miles.forEach(function (li) {
      var due = new Date(li.getAttribute("data-mile-date") + "T00:00:00");
      var done = due < noon;
      var isNext = !done && !foundNext;
      if (isNext) foundNext = true;

      li.classList.toggle("mile-done", done);
      li.classList.toggle("mile-next", isNext);

      var what = li.querySelector(".mile-what");
      var state = li.querySelector(".mile-state");
      if (!what || !state) return;

      /* Yellow means where we are, so it belongs to the next milestone and
         nowhere else. Pink stays on the assessed one whatever the date. */
      var swipe = what.querySelector(".hl");
      if (isNext && !swipe && !what.querySelector(".hl-pink")) {
        what.innerHTML = '<span class="hl">' + what.innerHTML + "</span>";
      } else if (!isNext && swipe) {
        what.innerHTML = swipe.innerHTML;
      }

      /* A milestone that has passed since the last build has no mark baked in
         at all, so set the text on the span or create one. The hand-drawn X
         only exists in the built markup; a date that rolls over between builds
         gets the words without it rather than a half-drawn doodle. */
      var mark = state.querySelector(".mile-mark");
      var want = done ? "done ✓" : isNext ? "← next up" : "";
      if (!want) {
        if (mark) mark.remove();
      } else if (mark) {
        mark.textContent = want;
      } else {
        mark = document.createElement("span");
        mark.className = "mile-mark";
        mark.textContent = want;
        state.appendChild(mark);
      }
    });
  }

  /* Success criteria ticks persist per lesson on this device only. */
  var lessonKey = document.body.getAttribute("data-lesson-key");
  if (lessonKey) {
    var store = "crit-" + lessonKey;
    var saved = [];
    try { saved = JSON.parse(localStorage.getItem(store) || "[]"); } catch (e) {}
    var boxes = document.querySelectorAll(".crit input[type=checkbox]");
    boxes.forEach(function (box, i) {
      box.checked = saved.indexOf(i) !== -1;
      box.addEventListener("change", function () {
        var on = [];
        boxes.forEach(function (b, j) { if (b.checked) on.push(j); });
        try { localStorage.setItem(store, JSON.stringify(on)); } catch (e) {}
      });
    });
  }

  /* Fill-in tables keep what was typed, per lesson, on this device only, so a
     phone locking mid-lesson does not wipe the class's work. */
  if (lessonKey) {
    document.querySelectorAll(".blk-gap").forEach(function (blk) {
      var gapStore = "gap-" + lessonKey + "-" + blk.getAttribute("data-gap-key");
      var answers = {};
      try { answers = JSON.parse(localStorage.getItem(gapStore) || "{}"); } catch (e) {}
      var inputs = blk.querySelectorAll(".gap-in");
      inputs.forEach(function (input) {
        var n = input.getAttribute("data-gap");
        if (answers[n]) input.value = answers[n];
        input.addEventListener("input", function () {
          var out = {};
          inputs.forEach(function (b) {
            if (b.value.trim()) out[b.getAttribute("data-gap")] = b.value;
          });
          try { localStorage.setItem(gapStore, JSON.stringify(out)); } catch (e) {}
        });
      });
      var clear = blk.querySelector(".gap-clear");
      if (clear) {
        clear.addEventListener("click", function () {
          inputs.forEach(function (b) { b.value = ""; });
          try { localStorage.removeItem(gapStore); } catch (e) {}
          inputs[0].focus();
        });
      }
    });
  }

  /* Doodle arrows draw themselves in as they enter the viewport. */
  var arrows = document.querySelectorAll(".draw-on");
  if (arrows.length && !reduced && "IntersectionObserver" in window) {
    arrows.forEach(function (svg) {
      svg.querySelectorAll("path").forEach(function (p) {
        var len = Math.ceil(p.getTotalLength());
        p.parentElement.closest("svg").style.setProperty("--len", len);
      });
      svg.setAttribute("data-drawn", "no");
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.setAttribute("data-drawn", "yes");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.4 });
    arrows.forEach(function (svg) { io.observe(svg); });
  }

  /* Cue times seek the player on the page instead of navigating to YouTube.
     The href is a real watch?t= link so it still works with JavaScript off;
     this only intercepts when there is an embed in the same block to seek. */
  document.querySelectorAll(".cues .cue-t").forEach(function (a) {
    a.addEventListener("click", function (ev) {
      var block = a.closest(".blk-guide");
      var frame = block && block.querySelector(".video iframe");
      if (!frame) return;                       // no player here, let the link go
      var at = parseInt(a.getAttribute("data-at"), 10);
      if (isNaN(at)) return;
      var src = frame.getAttribute("src").split("?")[0];
      ev.preventDefault();
      frame.setAttribute("src", src + "?start=" + at + "&autoplay=1");
      frame.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  });

  /* Keep the current lesson visible when the filmstrip overflows. */
  var now = document.querySelector(".strip .frame-now");
  if (now) {
    var scroller = now.closest(".strip-scroll");
    if (scroller && scroller.scrollWidth > scroller.clientWidth) {
      var nr = now.getBoundingClientRect();
      var sr = scroller.getBoundingClientRect();
      var target = scroller.scrollLeft + (nr.left - sr.left) - sr.width / 2 + nr.width / 2;
      scroller.scrollLeft = Math.max(0, target);
    }
  }
})();
