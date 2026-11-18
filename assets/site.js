/* Year 10's own script: one job, done once per page per device.

   Before 19 November 2026 this site kept ticks and typed answers under its own
   storage names ("crit-<lesson>", "gap-<lesson>-<table>"). The shared shell
   keeps them under new ones. So the first time a student opens a lesson after
   the move, anything saved under the old names is put back into the boxes,
   and the shell then keeps it under its own names from there. The old entries
   are left where they are; nothing is deleted.

   Runs after shell.js (both are deferred, in that order), so the shell's
   listeners are already in place and an "input" or "change" event is enough
   for it to save what is restored. */
(function () {
  "use strict";

  var m = location.pathname.match(/\/([^\/]+)\/([^\/]+)\/[a-z]+-(\d+)\/?(?:index\.html)?$/);
  if (!m) return;
  var old = m[1] + "-" + m[2] + "-" + m[3];
  var site = document.documentElement.getAttribute("data-site") || "site";

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function parse(s, empty) { try { return JSON.parse(s) || empty; } catch (e) { return empty; } }

  if (!get(site + ":ticks:" + location.pathname)) {
    var oldTicks = get("crit-" + old);
    if (oldTicks) {
      var boxes = document.querySelectorAll(".sc-list input[type=checkbox]");
      parse(oldTicks, []).forEach(function (i) {
        var b = boxes[i];
        if (!b) return;
        b.checked = true;
        b.dispatchEvent(new Event("change"));
      });
    }
  }

  if (!get(site + ":answers:" + location.pathname)) {
    Array.prototype.forEach.call(document.querySelectorAll(".blk[id]"), function (sec) {
      var saved = get("gap-" + old + "-" + sec.id);
      if (!saved) return;
      var answers = parse(saved, {});
      Array.prototype.forEach.call(sec.querySelectorAll("textarea.field"), function (f, row) {
        if (!answers[row] || f.value) return;
        f.value = answers[row];
        f.dispatchEvent(new Event("input"));
      });
    });
  }
})();
