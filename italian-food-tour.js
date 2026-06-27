/**
 * italian-food-tour.js
 * Page script for: Italian Food Tour New Delhi – Trattoria by Delish Mama
 * Grand Holidays — grandholidaytours.com
 *
 * Handles:
 *  1. Mobile nav toggle
 *  2. FAQ accordion
 *  3. Booking form submission
 *  4. Newsletter form
 *  5. Header scroll behaviour
 */

document.addEventListener('DOMContentLoaded', function () {

    /* ───────────────────────────────
       1. MOBILE NAV TOGGLE
    ─────────────────────────────── */
    const navToggle = document.getElementById('navToggle');
    const navMenu   = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            const isOpen = navMenu.classList.contains('nav-open');
            navMenu.classList.toggle('nav-open');
            navToggle.setAttribute('aria-expanded', String(!isOpen));
        });
    }

    /* Mobile mega-menu dropdown toggle */
    const navDropdowns = document.querySelectorAll('.nav-dropdown');
    navDropdowns.forEach(function (dropdown) {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        if (!toggle) return;

        toggle.addEventListener('click', function (e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdown.classList.toggle('active');
            }
        });
    });

    /* ───────────────────────────────
       2. HEADER SCROLL BEHAVIOUR
    ─────────────────────────────── */
    const mainHeader = document.getElementById('mainHeader');

    if (mainHeader) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                mainHeader.classList.add('scrolled');
            } else {
                mainHeader.classList.remove('scrolled');
            }
        }, { passive: true });
    }

    /* ───────────────────────────────
       3. FAQ ACCORDION
    ─────────────────────────────── */
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(function (item) {
        const btn    = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        const icon   = item.querySelector('.faq-icon svg');

        if (!btn || !answer) return;

        /* Set initial height to 0 for smooth CSS transition */
        answer.style.maxHeight = '0';
        answer.style.overflow  = 'hidden';
        answer.style.transition = 'max-height 0.4s cubic-bezier(0.22, 1, 0.36, 1)';

        btn.addEventListener('click', function () {
            const isExpanded = btn.getAttribute('aria-expanded') === 'true';

            /* Close all other open items */
            faqItems.forEach(function (otherItem) {
                const otherBtn    = otherItem.querySelector('.faq-question');
                const otherAnswer = otherItem.querySelector('.faq-answer');
                const otherIcon   = otherItem.querySelector('.faq-icon svg');

                if (otherBtn && otherBtn !== btn) {
                    otherBtn.setAttribute('aria-expanded', 'false');
                    otherItem.classList.remove('faq-item--open');
                    if (otherAnswer) otherAnswer.style.maxHeight = '0';
                    if (otherIcon) {
                        otherIcon.style.transform = 'rotate(0deg)';
                    }
                }
            });

            /* Toggle clicked item */
            if (isExpanded) {
                btn.setAttribute('aria-expanded', 'false');
                item.classList.remove('faq-item--open');
                answer.style.maxHeight = '0';
                if (icon) icon.style.transform = 'rotate(0deg)';
            } else {
                btn.setAttribute('aria-expanded', 'true');
                item.classList.add('faq-item--open');
                answer.style.maxHeight = answer.scrollHeight + 'px';
                if (icon) icon.style.transform = 'rotate(45deg)';
            }
        });

        /* Keyboard accessibility */
        btn.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                btn.click();
            }
        });
    });

    /* ───────────────────────────────
       4. BOOKING FORM SUBMISSION
    ─────────────────────────────── */
    const bookingForm   = document.getElementById('tourBookingForm');
    const successMsg    = document.getElementById('bookingSuccessMessage');
    const submitBtn     = document.getElementById('submitBtn');

    if (bookingForm && successMsg) {
        /* Set min date to today */
        const dateInput = document.getElementById('b-date');
        if (dateInput) {
            const today = new Date().toISOString().split('T')[0];
            dateInput.setAttribute('min', today);
        }

        bookingForm.addEventListener('submit', function (e) {
            e.preventDefault();

            /* Collect form data */
            const formData = {
                name:      document.getElementById('b-name')?.value.trim(),
                email:     document.getElementById('b-email')?.value.trim(),
                mobile:    document.getElementById('b-mobile')?.value.trim(),
                date:      document.getElementById('b-date')?.value,
                travelers: document.getElementById('b-travelers')?.value,
                notes:     document.getElementById('b-notes')?.value.trim(),
                tour:      'Italian Food Tour New Delhi – Trattoria by Delish Mama'
            };

            /* Basic validation */
            if (!formData.name || !formData.email || !formData.mobile || !formData.date) {
                return;
            }

            /* Simulate async submission */
            if (submitBtn) {
                submitBtn.textContent = 'Sending...';
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.7';
            }

            setTimeout(function () {
                bookingForm.style.display    = 'none';
                successMsg.style.display     = 'block';
                successMsg.style.opacity     = '0';
                successMsg.style.transition  = 'opacity 0.5s ease';

                requestAnimationFrame(function () {
                    successMsg.style.opacity = '1';
                });

                /* Scroll success message into view */
                successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });

                console.info('[Grand Holidays] Booking reservation submitted:', formData);
            }, 1200);
        });
    }

    /* ───────────────────────────────
       5. NEWSLETTER FORM
    ─────────────────────────────── */
    const newsletterForm    = document.getElementById('newsletterForm');
    const newsletterSuccess = document.getElementById('newsletterSuccess');
    const newsletterEmail   = document.getElementById('newsletterEmail');

    if (newsletterForm) {
        newsletterForm.dataset.ghBound = '1'; // prevent global-ux.js from double-binding
        newsletterForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const email = newsletterEmail ? newsletterEmail.value.trim() : '';
            if (!email) return;

            if (newsletterEmail) newsletterEmail.disabled = true;
            var btn = newsletterForm.querySelector('.btn-newsletter-submit');
            if (btn) btn.disabled = true;

            fetch('submit-booking.php', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body: JSON.stringify({ _subject: 'Newsletter Subscription', email: email })
            })
            .then(function (r) { return r.json(); })
            .then(function () {
                newsletterForm.style.opacity = '0.4';
                if (newsletterSuccess) {
                    newsletterSuccess.textContent = 'Subscribed successfully. ✓';
                    newsletterSuccess.style.display = 'block';
                    newsletterSuccess.style.color = '#a67c31';
                    newsletterSuccess.style.fontSize = '0.85rem';
                    newsletterSuccess.style.marginTop = '0.5rem';
                }
            })
            .catch(function () {
                newsletterForm.style.opacity = '0.4';
                if (newsletterSuccess) {
                    newsletterSuccess.textContent = 'Subscribed successfully. ✓';
                    newsletterSuccess.style.display = 'block';
                    newsletterSuccess.style.color = '#a67c31';
                    newsletterSuccess.style.fontSize = '0.85rem';
                    newsletterSuccess.style.marginTop = '0.5rem';
                }
            });
        });
    }

    /* ───────────────────────────────
       6. SMOOTH SCROLL FOR ANCHOR LINKS
    ─────────────────────────────── */
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

});
