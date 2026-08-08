(function () {
  var search = document.getElementById("addon-search");
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip"));
  var cards = Array.prototype.slice.call(document.querySelectorAll(".addon-card"));
  var noResults = document.getElementById("no-results");
  var activeTag = "all";

  function applyFilters() {
    var query = (search.value || "").trim().toLowerCase();
    var visible = 0;

    cards.forEach(function (card) {
      var tags = card.getAttribute("data-tags") || "";
      var text = card.textContent.toLowerCase();
      var tagOk = activeTag === "all" || tags.indexOf(activeTag) !== -1;
      var queryOk = !query || text.indexOf(query) !== -1;
      var show = tagOk && queryOk;
      card.style.display = show ? "" : "none";
      if (show) visible++;
    });

    if (noResults) noResults.style.display = visible === 0 ? "block" : "none";
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      chips.forEach(function (c) { c.classList.remove("active"); });
      chip.classList.add("active");
      activeTag = chip.getAttribute("data-tag");
      applyFilters();
    });
  });

  if (search) search.addEventListener("input", applyFilters);
})();
