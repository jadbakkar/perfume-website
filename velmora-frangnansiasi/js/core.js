/* ═══════════════════════════════════════════
   VELMORA — core behaviour shared by every page
   preloader · header · menu · reveals · parallax
   cursor · toast · order modal
   ═══════════════════════════════════════════ */
(function () {
  'use strict';
  var V = window.VELMORA;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var root = document.documentElement;

  /* ── helpers exposed to page scripts ── */
  function lock(on) { document.body.classList.toggle('is-locked', on); }
  var toastTimer;
  function toast(msg) {
    var t = $('#toast'); if (!t) return;
    clearTimeout(toastTimer);
    t.textContent = msg; t.classList.add('is-on');
    toastTimer = setTimeout(function () { t.classList.remove('is-on'); }, 3200);
  }
  function priceHTML() {
    return Object.keys(V.prices).map(function (k) {
      var p = V.prices[k];
      return '<span><b>$' + p.now + '</b><s>$' + p.was + '</s><em>' + k.replace('ml', ' ml') + '</em></span>';
    }).join('');
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }

  /* ── preloader → "ready" (starts hero animation) ── */
  function ready() {
    root.classList.add('is-ready');
    var ht = $('.hero-title'); if (ht) ht.classList.add('in');
  }
  var pre = $('#preloader');
  if (!pre || root.classList.contains('no-preloader') || reduce) {
    ready();
  } else {
    var started = Date.now();
    var finish = function () {
      var wait = Math.max(0, 1700 - (Date.now() - started));
      setTimeout(function () {
        pre.classList.add('is-done');
        try { sessionStorage.setItem('vl-intro', '1'); } catch (e) {}
        setTimeout(ready, 450);
      }, wait);
    };
    if (document.readyState === 'complete') finish(); else window.addEventListener('load', finish);
    setTimeout(finish, 4500); // never trap the visitor
  }

  /* ── header: solid on scroll, hides when scrolling down ── */
  var header = $('#siteHeader');
  var lastY = window.scrollY, ticking = false;
  var alwaysSolid = header && header.hasAttribute('data-solid');
  function onScroll() {
    var y = window.scrollY;
    if (header) {
      header.classList.toggle('is-solid', alwaysSolid || y > 70);
      var goingDown = y > lastY + 4, goingUp = y < lastY - 4;
      if (goingDown && y > 480 && !alwaysSolid && !document.body.classList.contains('is-locked')) header.classList.add('is-hidden');
      else if (goingUp || y < 200) header.classList.remove('is-hidden');
    }
    lastY = y; ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(function () { onScroll(); parallax(); wordsLit(); }); } }, { passive: true });
  if (alwaysSolid && header) header.classList.add('is-solid');

  /* active nav link */
  var links = $$('[data-link]');
  if (links.length && 'IntersectionObserver' in window) {
    var secs = links.map(function (l) { return $(l.getAttribute('href')); });
    var navIO = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) links.forEach(function (l) { l.classList.toggle('is-active', $(l.getAttribute('href')) === e.target); });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    secs.forEach(function (s) { if (s) navIO.observe(s); });
  }

  /* ── full-screen menu ── */
  var drawer = $('#drawer'), menuBtn = $('#menuBtn');
  function drawerSet(open) {
    if (!drawer) return;
    drawer.classList.toggle('is-open', open); lock(open);
    if (menuBtn) menuBtn.setAttribute('aria-expanded', String(open));
  }
  if (menuBtn) menuBtn.addEventListener('click', function () { drawerSet(true); });
  var dc = $('#drawerClose'); if (dc) dc.addEventListener('click', function () { drawerSet(false); });
  $$('[data-drawer-link]').forEach(function (a) { a.addEventListener('click', function () { drawerSet(false); }); });

  /* ── scroll reveals ── */
  var revealEls = $$('.reveal, .img-reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else revealEls.forEach(function (el) { el.classList.add('in'); });

  /* ── count-up numbers ── */
  var counters = $$('[data-count]');
  if (counters.length && 'IntersectionObserver' in window && !reduce) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        cio.unobserve(e.target);
        var el = e.target, end = +el.dataset.count, suf = el.dataset.suffix || '', t0 = null;
        (function step(t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / 1600, 1), ease = 1 - Math.pow(1 - p, 4);
          el.textContent = Math.round(end * ease) + suf;
          if (p < 1) requestAnimationFrame(step);
        })(performance.now());
      });
    }, { threshold: 0.6 });
    counters.forEach(function (c) { c.textContent = '0' + (c.dataset.suffix || ''); cio.observe(c); });
  }

  /* ── parallax ── */
  var pxEls = reduce ? [] : $$('[data-parallax], [data-parallax-img]');
  function parallax() {
    var vh = window.innerHeight;
    pxEls.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var speed = parseFloat(el.dataset.parallax || el.dataset.parallaxImg);
      var off = (r.top + r.height / 2 - vh / 2) * -speed;
      el.style.transform = 'translate3d(0,' + off.toFixed(1) + 'px,0)';
    });
  }

  /* ── scroll-lit words (manifesto statement) ── */
  var stmt = $('#statement'), words = [];
  if (stmt) {
    stmt.innerHTML = stmt.textContent.trim().split(/\s+/).map(function (w) { return '<span class="w">' + esc(w) + '</span>'; }).join(' ');
    words = $$('.w', stmt);
    if (reduce) words.forEach(function (w) { w.classList.add('is-lit'); });
  }
  function wordsLit() {
    if (!words.length || reduce) return;
    var r = stmt.getBoundingClientRect(), vh = window.innerHeight;
    var p = (vh * 0.85 - r.top) / (r.height + vh * 0.35);
    p = Math.min(Math.max(p, 0), 1);
    var n = Math.round(p * words.length);
    words.forEach(function (w, i) { w.classList.toggle('is-lit', i < n); });
  }
  parallax(); wordsLit();
  window.addEventListener('resize', function () { parallax(); wordsLit(); });

  /* ── custom cursor ── */
  if (finePointer && !reduce) {
    var dot = $('#cursorDot'), ring = $('#cursorRing');
    if (dot && ring) {
      var mx = 0, my = 0, rx = 0, ry = 0;
      window.addEventListener('mousemove', function (e) { mx = e.clientX; my = e.clientY; dot.style.opacity = 1; ring.style.opacity = 1; dot.style.transform = 'translate(' + mx + 'px,' + my + 'px)'; });
      (function loop() { rx += (mx - rx) * 0.16; ry += (my - ry) * 0.16; ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px)'; requestAnimationFrame(loop); })();
      document.addEventListener('mouseover', function (e) {
        var lab = e.target.closest('[data-cursor]');
        var lnk = e.target.closest('a, button, [role="button"], .piece, .pcard, input, select, label');
        ring.classList.toggle('is-label', !!lab);
        ring.classList.toggle('is-link', !!lnk && !lab);
        ring.textContent = lab ? lab.getAttribute('data-cursor') : '';
      });
      document.addEventListener('mouseleave', function () { ring.style.opacity = 0; dot.style.opacity = 0; });
      document.addEventListener('mouseenter', function () { ring.style.opacity = 1; dot.style.opacity = 1; });
    }
  } else { document.body.classList.remove('has-cursor'); }

  /* ── anchor links (smooth, account for pinned header) ── */
  $$('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (id === '#' || id.length < 2) { if (id === '#') e.preventDefault(); return; }
      var t = $(id); if (!t) return;
      e.preventDefault();
      t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    });
  });

  /* ── newsletter (UI only — wire to a service to store emails) ── */
  var nl = $('#newsletter');
  if (nl) nl.addEventListener('submit', function (e) { e.preventDefault(); toast('Welcome to the private list ✦'); nl.reset(); });

  /* ═════════ ORDER MODAL ═════════ */
  var modal = $('#orderModal'), current = null, lastFocus = null;
  function orderOpen(p) {
    if (!modal) return;
    current = p; lastFocus = document.activeElement;
    $('#mImg').src = V.img(p.file); $('#mImg').alt = p.brand + ' ' + p.name;
    $('#mBrand').textContent = p.brand; $('#mName').textContent = p.name;
    $('#mSize').innerHTML = Object.keys(V.prices).map(function (k) {
      return '<option value="' + k + '"' + (k === '100ml' ? ' selected' : '') + '>' + k.replace('ml', ' ml') + ' — $' + V.prices[k].now + '</option>';
    }).join('');
    var lb = $('#locBtn'); lb.disabled = false; lb.innerHTML = '<i class="fa-solid fa-location-crosshairs"></i> Pinpoint my location';
    modal.classList.add('is-open'); lock(true);
    setTimeout(function () { $('#mClient').focus(); }, 500);
  }
  function orderClose() { if (!modal) return; modal.classList.remove('is-open'); lock(false); if (lastFocus) lastFocus.focus(); }
  if (modal) {
    $('#orderClose').addEventListener('click', orderClose);
    modal.addEventListener('click', function (e) { if (e.target === modal) orderClose(); });
    $('#locBtn').addEventListener('click', function () {
      var b = this, addr = $('#mAddress');
      if (!navigator.geolocation) { toast('Location is not supported on this browser'); return; }
      b.disabled = true; b.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Locating…';
      navigator.geolocation.getCurrentPosition(function (pos) {
        addr.value = '📍 https://www.google.com/maps?q=' + pos.coords.latitude + ',' + pos.coords.longitude;
        b.innerHTML = '<i class="fa-solid fa-check"></i> Location attached'; toast('Location attached');
      }, function () {
        b.disabled = false; b.innerHTML = '<i class="fa-solid fa-location-crosshairs"></i> Pinpoint my location';
        toast('Could not get location — please type your address');
      }, { enableHighAccuracy: true, timeout: 8000 });
    });
    $('#mSend').addEventListener('click', function () {
      var name = $('#mClient').value.trim(), phone = $('#mPhone').value.trim(), addr = $('#mAddress').value.trim();
      if (!name || !phone || !addr) { toast('Please fill in your name, phone and address'); return; }
      var size = $('#mSize').value, price = V.prices[size];
      var msg = '🌿 *New Velmora Order*\n\n' +
        '*Perfume:* ' + current.brand + ' — ' + current.name + '\n' +
        '*Size:* ' + size.replace('ml', ' ml') + ' ($' + price.now + ')\n' +
        '*Name:* ' + name + '\n*Phone:* ' + phone + '\n*Address:* ' + addr;
      window.open('https://wa.me/' + V.whatsapp + '?text=' + encodeURIComponent(msg), '_blank');
      orderClose(); toast('Order ready — finish it in WhatsApp');
    });
  }

  /* ── Escape closes whatever is open ── */
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    orderClose(); drawerSet(false);
    var q = $('#quiz'); if (q && q.classList.contains('is-open')) { q.classList.remove('is-open'); lock(false); }
  });

  window.VL = { $: $, $$: $$, lock: lock, toast: toast, order: orderOpen, priceHTML: priceHTML, esc: esc, reduce: reduce };
})();
