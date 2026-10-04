/* ═══════════════════════════════════════════
   VELMORA — collection page
   brand-grouped catalogue · live search · A–Z jump
   ═══════════════════════════════════════════ */
(function () {
  'use strict';
  var V = window.VELMORA, VL = window.VL, $ = VL.$, esc = VL.esc;
  var results = $('#results'), search = $('#search'), count = $('#count'), az = $('#az');

  /* group + sort */
  var groups = {};
  V.products.forEach(function (p) { (groups[p.brand] = groups[p.brand] || []).push(p); });
  var brands = Object.keys(groups).sort(function (a, b) { return a.localeCompare(b); });
  var priceHTML = VL.priceHTML();

  function card(p, i) {
    return '<article class="pcard" role="button" tabindex="0" data-file="' + esc(p.file) + '" data-cursor="Order" style="--i:' + Math.min(i, 14) + '" aria-label="Order ' + esc(p.brand + ' ' + p.name) + '">' +
      '<div class="pcard-img"><img src="' + V.img(p.file) + '" alt="' + esc(p.brand + ' ' + p.name) + '" loading="lazy"><b>Quick order</b></div>' +
      '<div class="pcard-meta"><small>' + esc(p.brand) + '</small><h3>' + esc(p.name) + '</h3><div class="price">' + priceHTML + '</div></div></article>';
  }

  function render(q) {
    q = (q || '').trim().toLowerCase();
    var html = '', total = 0, letters = {};
    brands.forEach(function (b) {
      var list = groups[b].filter(function (p) { return !q || p.name.toLowerCase().indexOf(q) > -1 || b.toLowerCase().indexOf(q) > -1; });
      if (!list.length) return;
      total += list.length;
      var L = b.charAt(0).toUpperCase(); var first = !letters[L]; letters[L] = 1;
      html += '<section class="brand-block"' + (first ? ' id="L-' + L + '"' : '') + '><div class="brand-title"><h2>' + esc(b) + '</h2><span>' + list.length + (list.length === 1 ? ' scent' : ' scents') + '</span></div><div class="grid">' +
        list.map(function (p, i) { return card(p, i); }).join('') + '</div></section>';
    });
    if (!total) {
      html = '<div class="empty"><i class="fa-regular fa-gem"></i><h3>No fragrance found</h3><p></p><button class="btn btn--dark" id="clear">Clear search</button></div>';
    }
    results.innerHTML = html;
    if (!total) { results.querySelector('.empty p').textContent = 'Nothing matches “' + q + '”. Try a brand name like Dior or Creed.'; $('#clear').addEventListener('click', function () { search.value = ''; render(''); search.focus(); }); }
    count.textContent = total + (total === 1 ? ' fragrance' : ' fragrances') + (q ? ' found' : ' · ' + brands.length + ' houses');
    buildAZ(letters);
  }

  function buildAZ(active) {
    var out = '';
    for (var c = 65; c <= 90; c++) { var L = String.fromCharCode(c); out += '<button data-l="' + L + '"' + (active[L] ? '' : ' disabled') + '>' + L + '</button>'; }
    az.innerHTML = out;
  }
  az.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b || b.disabled) return;
    var t = document.getElementById('L-' + b.dataset.l);
    if (t) t.scrollIntoView({ behavior: VL.reduce ? 'auto' : 'smooth', block: 'start' });
  });

  /* open order modal */
  function open(el) { var p = V.byFile[el.dataset.file]; if (p) VL.order(p); }
  results.addEventListener('click', function (e) { var el = e.target.closest('.pcard'); if (el) open(el); });
  results.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var el = e.target.closest('.pcard'); if (el) { e.preventDefault(); open(el); }
  });

  /* live search (debounced) */
  var t; search.addEventListener('input', function () { clearTimeout(t); t = setTimeout(function () { render(search.value); }, 120); });

  render('');
})();
