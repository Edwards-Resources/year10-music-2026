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
