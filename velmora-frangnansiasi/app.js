document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', () => {

    const WHATSAPP_NUMBER = '96181772615';

    // ── Header Scroll ──
    const header = document.getElementById('mainHeader');
    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 30);
    });

    // ── Mobile Drawer ──
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const drawerOverlay = document.getElementById('drawerOverlay');
    const drawerCloseBtn = document.getElementById('drawerCloseBtn');

    function toggleDrawer() {
        mobileDrawer.classList.toggle('open');
        drawerOverlay.classList.toggle('show');
        document.body.style.overflow = mobileDrawer.classList.contains('open') ? 'hidden' : '';
    }

    if (hamburgerBtn) hamburgerBtn.addEventListener('click', toggleDrawer);
    if (drawerCloseBtn) drawerCloseBtn.addEventListener('click', toggleDrawer);
    if (drawerOverlay) drawerOverlay.addEventListener('click', toggleDrawer);
    document.querySelectorAll('.drawer-nav-link').forEach(link => {
        link.addEventListener('click', toggleDrawer);
    });

    // ── Brand Marquee ──
    const brands = ["Chanel", "Dior", "Creed", "Tom Ford", "YSL", "Baccarat Rouge", "Kilian", "Parfums de Marly", "Azzaro", "Burberry"];
    const brandStrip = document.getElementById('brandStrip');
    if (brandStrip) {
        let html = '';
        for (let i = 0; i < 4; i++) {
            brands.forEach(b => { html += `<span class="brand-item">${b}</span>`; });
        }
        brandStrip.innerHTML = html;
    }

    // ── Duplicate Review Rows for Infinite Loop ──
    document.querySelectorAll('.marquee-track').forEach(track => {
        track.innerHTML += track.innerHTML;
    });

    // ── Products Scroll Indicator ──
    const scrollWrapper = document.getElementById('productsScroll');
    const scrollTrack = document.getElementById('productsTrack');
    const indicatorEl = document.getElementById('scrollIndicator');

    if (scrollWrapper && scrollTrack && indicatorEl) {
        const cards = scrollTrack.querySelectorAll('.product-card');
        const totalCards = cards.length;
        const visibleCount = Math.min(totalCards, 8); // show max 8 dots

        // Create dots
        for (let i = 0; i < visibleCount; i++) {
            const dot = document.createElement('div');
            dot.className = 'scroll-dot' + (i === 0 ? ' active' : '');
            indicatorEl.appendChild(dot);
        }

        const dots = indicatorEl.querySelectorAll('.scroll-dot');

        scrollWrapper.addEventListener('scroll', () => {
            const scrollLeft = scrollWrapper.scrollLeft;
            const maxScroll = scrollWrapper.scrollWidth - scrollWrapper.clientWidth;
            const progress = maxScroll > 0 ? scrollLeft / maxScroll : 0;
            const activeIndex = Math.round(progress * (dots.length - 1));

            dots.forEach((d, i) => d.classList.toggle('active', i === activeIndex));
        });

        // ── Products Scroll Arrow Buttons ──
        const leftArrow = document.getElementById('scrollLeftBtn');
        const rightArrow = document.getElementById('scrollRightBtn');
        if (leftArrow && rightArrow) {
            leftArrow.addEventListener('click', () => {
                scrollWrapper.scrollBy({ left: -320, behavior: 'smooth' });
            });
            rightArrow.addEventListener('click', () => {
                scrollWrapper.scrollBy({ left: 320, behavior: 'smooth' });
            });
        }
    }

    // ── Order Modal ──
    const orderModal = document.getElementById('orderModal');
    const modalCloseBtn = document.getElementById('modalCloseBtn');
    const getLocationBtn = document.getElementById('getLocationBtn');
    const addressInput = document.getElementById('modalClientAddress');

    window.openOrderModal = (brand, name) => {
        const modalBrand = document.getElementById('modalBrand');
        const modalName = document.getElementById('modalName');
        if (modalBrand) modalBrand.textContent = brand;
        if (modalName) modalName.textContent = name;
        
        // Reset Geolocation Button state
        if (getLocationBtn) {
            getLocationBtn.innerHTML = '<i class="fa-solid fa-location-crosshairs"></i> Pinpoint My Location (Google Maps)';
            getLocationBtn.disabled = false;
            getLocationBtn.style.color = 'var(--turquoise)';
            getLocationBtn.style.borderColor = 'var(--turquoise)';
        }
        
        if (orderModal) orderModal.classList.add('show');
        document.body.style.overflow = 'hidden';
    };

    if (modalCloseBtn) {
        modalCloseBtn.addEventListener('click', () => {
            orderModal.classList.remove('show');
            document.body.style.overflow = '';
        });
    }
    if (orderModal) {
        orderModal.addEventListener('click', (e) => {
            if (e.target === orderModal) {
                orderModal.classList.remove('show');
                document.body.style.overflow = '';
            }
        });
    }

    // ── HTML5 Geolocation ──
    if (getLocationBtn && addressInput) {
        getLocationBtn.addEventListener('click', () => {
            getLocationBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Getting Location...';
            getLocationBtn.disabled = true;

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        const lat = position.coords.latitude;
                        const lng = position.coords.longitude;
                        const mapsUrl = `https://www.google.com/maps?q=${lat},${lng}`;
                        
                        addressInput.value = `📍 Current Location Pin: ${mapsUrl}`;
                        getLocationBtn.innerHTML = '<i class="fa-solid fa-check"></i> Location Attached!';
                        getLocationBtn.style.color = '#25D366';
                        getLocationBtn.style.borderColor = '#25D366';
                        showToast('📌 Location attached successfully!');
                    },
                    (error) => {
                        console.error(error);
                        getLocationBtn.innerHTML = '<i class="fa-solid fa-xmark"></i> Permission Denied / Error';
                        getLocationBtn.style.color = '#ff4a4a';
                        getLocationBtn.style.borderColor = '#ff4a4a';
                        getLocationBtn.disabled = false;
                        showToast('⚠️ Could not get location. Please type your address.');
                    },
                    { enableHighAccuracy: true, timeout: 8000 }
                );
            } else {
                getLocationBtn.innerHTML = '<i class="fa-solid fa-xmark"></i> Not Supported';
                getLocationBtn.disabled = false;
                showToast('⚠️ Geolocation not supported by browser.');
            }
        });
    }

    // ── WhatsApp Send ──
    const sendBtn = document.getElementById('modalSendBtn');
    if (sendBtn) {
        sendBtn.addEventListener('click', () => {
            const brand = document.getElementById('modalBrand').textContent;
            const name = document.getElementById('modalName').textContent;
            const size = document.getElementById('modalSize').value;
            const clientName = document.getElementById('modalClientName').value;
            const phone = document.getElementById('modalClientPhone').value;
            const address = document.getElementById('modalClientAddress').value;

            if (!clientName.trim() || !phone.trim() || !address.trim()) {
                showToast('⚠️ Please fill in your name, phone and address.');
                return;
            }

            const msg = `🌿 *New Velmora Order*\n\n` +
                `*Perfume:* ${brand} — ${name}\n` +
                `*Size:* ${size}\n` +
                `*Name:* ${clientName}\n` +
                `*Phone:* ${phone}\n` +
                `*Address:* ${address}`;

            const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank');

            orderModal.classList.remove('show');
            document.body.style.overflow = '';
            showToast('✅ Order sent! Check WhatsApp.');
        });
    }

    // ── Toast ──
    let toastTimer;
    window.showToast = (msg) => {
        const toast = document.getElementById('toastEl');
        if (!toast) return;
        clearTimeout(toastTimer);
        toast.textContent = msg;
        toast.style.opacity = '1';
        toast.style.transform = 'translateX(-50%) translateY(0)';
        toastTimer = setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(-50%) translateY(20px)';
        }, 3000);
    };

    // ── Scroll reveal ──
    const revealEls = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver((entries) => {
            entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        revealEls.forEach(el => io.observe(el));
    } else {
        revealEls.forEach(el => el.classList.add('in'));
    }

    // ── Extra "Find my scent" triggers ──
    document.querySelectorAll('[data-open-quiz]').forEach(b => b.addEventListener('click', () => {
        const q = document.getElementById('openQuizBtn');
        if (q) q.click();
    }));

    // ── Close modal / drawer with Escape ──
    document.addEventListener('keydown', (e) => {
        if (e.key !== 'Escape') return;
        if (orderModal && orderModal.classList.contains('show')) {
            orderModal.classList.remove('show');
            document.body.style.overflow = '';
        }
        if (mobileDrawer && mobileDrawer.classList.contains('open')) toggleDrawer();
        const quiz = document.getElementById('quizModalOverlay');
        if (quiz) quiz.classList.remove('active');
    });

    // ── Keyboard access for clickable product cards ──
    window.makeCardAccessible = (card) => {
        card.setAttribute('role', 'button');
        card.setAttribute('tabindex', '0');
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); card.click(); }
        });
    };
    document.querySelectorAll('.product-card').forEach(window.makeCardAccessible);

    // ── Active nav link on scroll ──
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
    const sections = [...navLinks].map(l => document.querySelector(l.getAttribute('href'))).filter(Boolean);
    if (sections.length) {
        window.addEventListener('scroll', () => {
            const pos = window.scrollY + header.offsetHeight + 80;
            let current = sections[0];
            sections.forEach(sec => { if (sec.offsetTop <= pos) current = sec; });
            navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + current.id));
        }, { passive: true });
    }

    // ── Smooth Scroll for Nav Links ──
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const headerHeight = header.offsetHeight;
                const targetPos = target.getBoundingClientRect().top + window.scrollY - headerHeight;
                window.scrollTo({ top: targetPos, behavior: 'smooth' });
            }
        });
    });

});
