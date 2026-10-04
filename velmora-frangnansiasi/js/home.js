/* ═══════════════════════════════════════════
   VELMORA — homepage behaviour
   brand marquee · signature rail · scent finder · reviews
   ═══════════════════════════════════════════ */
(function () {
  'use strict';
  var V = window.VELMORA, VL = window.VL, $ = VL.$, $$ = VL.$$, esc = VL.esc;

  /* ── brand marquee ── */
  var wanted = ['Chanel', 'Dior', 'Creed', 'Tom Ford', 'Parfums de Marly', 'Maison Francis Kurkdjian', 'Kayali', 'Versace', 'Burberry', 'Azzaro', 'Giorgio Armani', 'Hermes', 'Gucci', 'Givenchy', 'Carolina Herrera', 'Louis Vuitton'];
  var have = {}; V.products.forEach(function (p) { have[p.brand] = 1; });
  var brands = wanted.filter(function (b) { return have[b]; });
  var bt = $('#brandsTrack');
  if (bt) {
    var one = brands.map(function (b) { return '<span>' + esc(b) + '</span><i>✦</i>'; }).join('');
    bt.innerHTML = one + one;
  }

  /* ── signature rail ── */
  var track = $('#railTrack'), rail = $('#rail');
  if (track) {
    track.innerHTML = V.featured.map(function (file, i) {
      var p = V.byFile[file]; if (!p) return '';
      return '<article class="piece" role="button" tabindex="0" data-file="' + esc(file) + '" data-cursor="Order" aria-label="Order ' + esc(p.brand + ' ' + p.name) + '">' +
        '<div class="piece-img"><span class="piece-no">N° ' + String(i + 1).padStart(2, '0') + '</span>' +
        '<img src="' + V.img(file) + '" alt="' + esc(p.brand + ' ' + p.name) + '" loading="lazy" draggable="false">' +
        '<span class="piece-order">Quick order</span></div>' +
        '<div class="piece-meta"><small>' + esc(p.brand) + '</small><h3>' + esc(p.name) + ' Inspired</h3>' +
        '<div class="price">' + VL.priceHTML() + '</div></div></article>';
    }).join('');

    /* drag to scroll (mouse) — touch uses native scrolling */
    var down = false, startX = 0, startL = 0, moved = 0;
    rail.addEventListener('mousedown', function (e) { down = true; moved = 0; startX = e.pageX; startL = rail.scrollLeft; rail.classList.add('is-drag'); });
    window.addEventListener('mouseup', function () { down = false; rail.classList.remove('is-drag'); });
    window.addEventListener('mousemove', function (e) { if (!down) return; var dx = e.pageX - startX; moved = Math.max(moved, Math.abs(dx)); rail.scrollLeft = startL - dx; });
    var openPiece = function (el) { var p = V.byFile[el.dataset.file]; if (p) VL.order(p); };
    track.addEventListener('click', function (e) {
      if (moved > 6) { moved = 0; return; }
      var el = e.target.closest('.piece'); if (el) openPiece(el);
    });
    track.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      var el = e.target.closest('.piece'); if (el) { e.preventDefault(); openPiece(el); }
    });

    /* arrows + progress */
    var step = function () { var c = track.firstElementChild; return c ? c.getBoundingClientRect().width + 28 : 320; };
    $('#railPrev').addEventListener('click', function () { rail.scrollBy({ left: -step(), behavior: 'smooth' }); });
    $('#railNext').addEventListener('click', function () { rail.scrollBy({ left: step(), behavior: 'smooth' }); });
    var bar = $('#railBar');
    var prog = function () {
      var max = rail.scrollWidth - rail.clientWidth, p = max > 0 ? rail.scrollLeft / max : 0;
      bar.style.width = (20 + p * 80) + '%';
    };
    rail.addEventListener('scroll', prog, { passive: true }); prog();
  }

  /* ── reviews carousel ── */
  var quotes = $$('.quote'), dotsEl = $('#quoteDots'), qi = 0, timer;
  if (quotes.length && dotsEl) {
    dotsEl.innerHTML = quotes.map(function (_, i) { return '<button aria-label="Review ' + (i + 1) + '"' + (i === 0 ? ' class="is-on"' : '') + '></button>'; }).join('');
    var dots = $$('button', dotsEl);
    var show = function (i) {
      qi = (i + quotes.length) % quotes.length;
      quotes.forEach(function (q, k) { q.classList.toggle('is-on', k === qi); });
      dots.forEach(function (d, k) { d.classList.toggle('is-on', k === qi); });
    };
    var auto = function () { clearInterval(timer); if (!VL.reduce) timer = setInterval(function () { show(qi + 1); }, 7000); };
    $('#quotePrev').addEventListener('click', function () { show(qi - 1); auto(); });
    $('#quoteNext').addEventListener('click', function () { show(qi + 1); auto(); });
    dots.forEach(function (d, k) { d.addEventListener('click', function () { show(k); auto(); }); });
    $('#quoteStage').addEventListener('mouseenter', function () { clearInterval(timer); });
    $('#quoteStage').addEventListener('mouseleave', auto);
    auto();
  }

  /* ── scent finder ── */
  var quiz = $('#quiz');
  if (quiz) {
    var steps = ['1', '2', '3', '4'], idx = 0, ans = {}, match = null;
    var prog2 = $('#quizProgress'), back = $('#quizBack');
    prog2.innerHTML = steps.map(function () { return '<span></span>'; }).join('');
    var bars = $$('span', prog2);
    var showStep = function (key) {
      $$('.quiz-step', quiz).forEach(function (s) { s.classList.toggle('is-on', s.dataset.step === key); });
      bars.forEach(function (b, i) { b.classList.toggle('is-done', i <= idx); });
      back.style.visibility = (key === '1' || key === 'result') ? 'hidden' : 'visible';
    };
    var reset = function () {
      idx = 0; ans = {}; match = null;
      $$('.quiz-opt', quiz).forEach(function (b) { b.classList.remove('is-sel'); });
      showStep('1');
    };
    var openQuiz = function () { reset(); quiz.classList.add('is-open'); VL.lock(true); };
    var closeQuiz = function () { quiz.classList.remove('is-open'); VL.lock(false); };
    $$('[data-open-finder]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); openQuiz(); }); });
    $('#quizClose').addEventListener('click', closeQuiz);
    quiz.addEventListener('click', function (e) { if (e.target === quiz) closeQuiz(); });

    $$('.quiz-opt', quiz).forEach(function (btn) {
      btn.addEventListener('click', function () {
        var step = btn.closest('.quiz-step').dataset.step;
        ans[step] = btn.dataset.v;
        $$('.quiz-opt', btn.parentNode).forEach(function (b) { b.classList.remove('is-sel'); });
        btn.classList.add('is-sel');
        setTimeout(function () {
          if (idx < steps.length - 1) { idx++; showStep(steps[idx]); } else result();
        }, 260);
      });
    });
    back.addEventListener('click', function () { if (idx > 0) { idx--; showStep(steps[idx]); } });
    $('#qRestart').addEventListener('click', reset);

    var result = function () {
      var fam = ans['2'] || 'floral', vibe = ans['3'] || '', last = ans['4'] || '';
      var key = fam;
      if (fam === 'fresh' && (vibe === 'elegant' || last === 'light')) key = 'refined';
      if (fam === 'floral' && vibe === 'mysterious') key = 'woody';
      var pick = V.quiz[key], p = V.byFile[pick.file];
      match = p;
      $('#qImg').src = V.img(p.file); $('#qImg').alt = p.brand + ' ' + p.name;
      $('#qName').textContent = p.name + ' Inspired';
      $('#qBrand').textContent = p.brand;
      $('#qPrice').innerHTML = VL.priceHTML();
      $('#qNote').textContent = pick.note;
      $$('.quiz-step', quiz).forEach(function (s) { s.classList.toggle('is-on', s.dataset.step === 'result'); });
      bars.forEach(function (b) { b.classList.add('is-done'); });
      back.style.visibility = 'hidden';
    };
    $('#qOrder').addEventListener('click', function () { closeQuiz(); if (match) setTimeout(function () { VL.order(match); }, 250); });
  }
})();
