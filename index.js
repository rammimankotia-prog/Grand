document.addEventListener('DOMContentLoaded', () => {
    // 1. Navigation Header Scroll Effect
    const header = document.getElementById('mainHeader');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // 1b. Scroll-Reveal via IntersectionObserver
    const revealEls = document.querySelectorAll('.reveal');
    // Immediately mark visible if already in viewport
    revealEls.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(28px)';
    });
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'none';
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });
    revealEls.forEach(el => revealObserver.observe(el));


    // Mobile Navigation Toggle
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');

    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        // Simple hamburger to X transformation
        const bars = menuToggle.querySelectorAll('.bar');
        bars[0].style.transform = navMenu.classList.contains('active') ? 'rotate(45deg) translate(5px, 6px)' : 'none';
        bars[1].style.opacity = navMenu.classList.contains('active') ? '0' : '1';
        bars[2].style.transform = navMenu.classList.contains('active') ? 'rotate(-45deg) translate(5px, -6px)' : 'none';
    });

    // 2. Parallax Effect on Hero Background Image
    const heroBgImg = document.getElementById('heroBgImg');
    window.addEventListener('scroll', () => {
        const scrollOffset = window.scrollY;
        // Move image slower than scroll speed (parallax)
        if (scrollOffset < window.innerHeight) {
            heroBgImg.style.transform = `translateY(${scrollOffset * 0.3}px) scale(1.1)`;
        }
    });

    // 3. Canvas Particle System: Floating Marigold Petals & Levitating Water Droplets
    const canvas = document.getElementById('hero-particles');
    const ctx = canvas.getContext('2d');

    let particles = [];
    const maxParticles = 65;

    // Handle Resize
    function resizeCanvas() {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Particle Classes
    class Petal {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * canvas.width;
            this.y = canvas.height + Math.random() * 100; // Start below screen
            this.size = Math.random() * 8 + 6;
            this.speedY = -(Math.random() * 1.2 + 0.6); // Float upwards
            this.speedX = Math.random() * 0.8 - 0.4;
            this.opacity = Math.random() * 0.5 + 0.3;
            // Orange/yellow marigold petal palette or soft jasmine pink/white
            this.type = Math.random() > 0.5 ? 'marigold' : 'jasmine';
            if (this.type === 'marigold') {
                this.color = Math.random() > 0.5 ? 'hsl(35, 100%, 55%)' : 'hsl(45, 100%, 50%)'; // vibrant orange/gold
            } else {
                this.color = 'rgba(255, 255, 255, 0.75)'; // white jasmine
            }
            this.rotation = Math.random() * 360;
            this.rotationSpeed = Math.random() * 1.5 - 0.75;
            this.flutter = Math.random() * 2 * Math.PI;
            this.flutterSpeed = Math.random() * 0.02 + 0.01;
        }

        update() {
            this.y += this.speedY;
            this.flutter += this.flutterSpeed;
            // Add slight drift left/right
            this.x += this.speedX + Math.sin(this.flutter) * 0.2;
            this.rotation += this.rotationSpeed;

            // Reset when leaving top of screen
            if (this.y < -20 || this.x < -20 || this.x > canvas.width + 20) {
                this.reset();
                this.y = canvas.height + 20;
            }
        }

        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate((this.rotation * Math.PI) / 180);
            ctx.globalAlpha = this.opacity;
            ctx.fillStyle = this.color;

            // Draw petal shapes
            ctx.beginPath();
            if (this.type === 'marigold') {
                // Oval rounded petal
                ctx.moveTo(0, -this.size);
                ctx.quadraticCurveTo(this.size / 2, -this.size / 2, 0, 0);
                ctx.quadraticCurveTo(-this.size / 2, -this.size / 2, 0, -this.size);
            } else {
                // Sleeker teardrop petal
                ctx.moveTo(0, -this.size);
                ctx.quadraticCurveTo(this.size / 3, -this.size / 1.5, 0, 0);
                ctx.quadraticCurveTo(-this.size / 3, -this.size / 1.5, 0, -this.size);
            }
            ctx.fill();
            ctx.restore();
        }
    }

    class WaterDroplet {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * canvas.width;
            this.y = canvas.height + Math.random() * 200;
            this.size = Math.random() * 2 + 1;
            this.speedY = -(Math.random() * 2.2 + 1.2); // Faster upward rise
            this.opacity = Math.random() * 0.35 + 0.15;
            this.color = 'rgba(74, 185, 230, ' + this.opacity + ')'; // turquoise glow
        }

        update() {
            this.y += this.speedY;
            // Float straight up
            if (this.y < -20) {
                this.reset();
                this.y = canvas.height + 20;
            }
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.shadowBlur = 10;
            ctx.shadowColor = 'rgba(74, 185, 230, 0.8)';
            ctx.fill();
            // Reset shadow defaults
            ctx.shadowBlur = 0;
        }
    }

    // Initialize Particle Arrays
    function initParticles() {
        particles = [];
        for (let i = 0; i < maxParticles * 0.6; i++) {
            particles.push(new Petal());
        }
        for (let i = 0; i < maxParticles * 0.4; i++) {
            particles.push(new WaterDroplet());
        }
    }
    initParticles();

    // Loop
    function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles.forEach(p => {
            p.update();
            p.draw();
        });
        
        requestAnimationFrame(animateParticles);
    }
    animateParticles();

    // Re-init on resize to keep count consistent
    window.addEventListener('resize', initParticles);

    // 4. 3D Tilt & Light Reflection Card Effect
    const cards = document.querySelectorAll('[data-tilt]');
    
    cards.forEach(card => {
        // Spotlight Glow Tracker
        const glow = document.createElement('div');
        glow.className = 'card-glow-effect';
        card.appendChild(glow);

        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; // Mouse position inside card
            const y = e.clientY - rect.top;

            // Set variables for CSS spotlight glow
            glow.style.setProperty('--x', `${x}px`);
            glow.style.setProperty('--y', `${y}px`);

            // Tilt Calculations
            const cardWidth = rect.width;
            const cardHeight = rect.height;
            const centerX = rect.left + cardWidth / 2;
            const centerY = rect.top + cardHeight / 2;
            const mouseX = e.clientX - centerX;
            const mouseY = e.clientY - centerY;

            // Tilt limit: 12 degrees max
            const maxTilt = 10;
            const rotateX = -(mouseY / (cardHeight / 2)) * maxTilt;
            const rotateY = (mouseX / (cardWidth / 2)) * maxTilt;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
            glow.style.setProperty('--x', `-1000px`);
            glow.style.setProperty('--y', `-1000px`);
        });
    });

    // 5. Booking Inquiry Modal Controls
    const inquiryModal = document.getElementById('inquiryModal');
    const openModalBtn = document.getElementById('openModalBtn');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const modalForm = document.getElementById('modalForm');
    const modalSuccess = document.getElementById('modalSuccessMessage');
    const modalJourneyTitle = document.getElementById('modalJourneyTitle');
    const modalJourneyInput = document.getElementById('modalJourneyInput');

    function openInquiry(journeyName = '') {
        modalForm.reset();
        modalForm.style.display = 'flex';
        modalSuccess.style.display = 'none';
        
        if (journeyName) {
            modalJourneyTitle.innerText = `Plan Your Custom ${journeyName} Journey`;
            modalJourneyInput.value = journeyName;
        } else {
            modalJourneyTitle.innerText = 'Plan Your Custom Luxury Indian Journey';
            modalJourneyInput.value = 'General Custom Journey';
        }
        
        inquiryModal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Stop background scrolling
    }

    function closeInquiry() {
        inquiryModal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }

    // Connect trigger buttons
    openModalBtn.addEventListener('click', () => openInquiry());
    closeModalBtn.addEventListener('click', closeInquiry);
    
    // Connect explore buttons on individual travel cards
    document.querySelectorAll('.open-booking-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const journeyName = e.target.getAttribute('data-journey');
            openInquiry(journeyName);
        });
    });

    // Close on overlay click
    inquiryModal.addEventListener('click', (e) => {
        if (e.target === inquiryModal) closeInquiry();
    });

    // 6. Form Submit Handlers with Smooth Visual Feedback
    // Modal Form
    modalForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const submitBtn = modalForm.querySelector('.btn-submit');
        submitBtn.innerText = 'Transmitting to Concierge...';
        submitBtn.disabled = true;

        const data = {
            _subject: `New Grand Holidays Inquiry: ${document.getElementById('modalJourneyInput').value}`,
            name: document.getElementById('modalName').value,
            email: document.getElementById('modalEmail').value,
            preferredDates: document.getElementById('modalDates').value,
            message: document.getElementById('modalMessage').value
        };

        fetch("submit-booking.php", {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success || data.success === "true") {

            modalForm.style.display = 'none';
            modalSuccess.style.display = 'flex';
        
            } else {
                alert("Server Message: " + (data.message || "Email service requires activation. Please check tours@godwinhotels.com for an activation link."));
                const submitBtn = bookingForm.querySelector('button[type="submit"]') || bookingForm.querySelector('.btn-sidebar-submit');
                if (submitBtn) {
                    submitBtn.innerText = 'Submit Reservation Request';
                    submitBtn.disabled = false;
                }
            }
        })
        .catch(err => {
            console.error(err);
            submitBtn.innerText = 'Error. Try Again.';
            submitBtn.disabled = false;
        });
    });

    // Page Concierge Form
    const conciergeForm = document.getElementById('conciergeForm');
    const formSuccess = document.getElementById('formSuccessMessage');

    conciergeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const submitBtn = conciergeForm.querySelector('.btn-submit');
        submitBtn.innerText = 'Designing Your Itinerary...';
        submitBtn.disabled = true;

        const data = {
            _subject: "New Grand Holidays Concierge Inquiry",
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            journeyType: document.getElementById('journey-type').value,
            message: document.getElementById('notes').value
        };

        fetch("submit-booking.php", {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success || data.success === "true") {

            conciergeForm.style.display = 'none';
            formSuccess.style.display = 'flex';
        
            } else {
                alert("Server Message: " + (data.message || "Email service requires activation. Please check tours@godwinhotels.com for an activation link."));
                const submitBtn = bookingForm.querySelector('button[type="submit"]') || bookingForm.querySelector('.btn-sidebar-submit');
                if (submitBtn) {
                    submitBtn.innerText = 'Submit Reservation Request';
                    submitBtn.disabled = false;
                }
            }
        })
        .catch(err => {
            console.error(err);
            submitBtn.innerText = 'Error. Try Again.';
            submitBtn.disabled = false;
        });
    });

    // Newsletter Form
    const newsletterForm = document.getElementById('newsletterForm');
    const newsletterSuccess = document.getElementById('newsletterSuccess');

    newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailInput = document.getElementById('newsletterEmail');
        emailInput.disabled = true;
        newsletterForm.querySelector('.btn-newsletter-submit').disabled = true;
        
        setTimeout(() => {
            newsletterForm.style.opacity = '0.3';
            newsletterSuccess.style.display = 'block';
        }, 800);
    });

    // 7. Concept Explainer Modal Controls
    const conceptModal = document.getElementById('conceptModal');
    const playVideoBtn = document.getElementById('playVideoBtn');
    const closeConceptModalBtn = document.getElementById('closeConceptModalBtn');

    playVideoBtn.addEventListener('click', () => {
        conceptModal.classList.add('active');
        document.body.style.overflow = 'hidden';
    });

    closeConceptModalBtn.addEventListener('click', () => {
        conceptModal.classList.remove('active');
        document.body.style.overflow = 'auto';
    });

    conceptModal.addEventListener('click', (e) => {
        if (e.target === conceptModal) {
            conceptModal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });

    // 6. Mobile Dropdown Menu Toggle
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const parent = toggle.closest('.nav-dropdown');
                if (parent) {
                    parent.classList.toggle('active');
                }
            }
        });
    });
});
