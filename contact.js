document.addEventListener('DOMContentLoaded', () => {
    // 1. FAQ Accordion Handler
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Close all other items for a cleaner accordion effect
            faqItems.forEach(otherItem => {
                otherItem.classList.remove('active');
            });
            
            // Toggle current item
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });

    // 2. Contact Page Form Submit Handler
    const contactForm = document.getElementById('contactPageForm');
    const successMessage = document.getElementById('contactSuccessMessage');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const submitBtn = contactForm.querySelector('.btn-submit');
            submitBtn.innerText = 'Routing to Curation Desk...';
            submitBtn.disabled = true;

            const data = {
                _subject: "New Grand Holidays Contact Page Inquiry",
                name: document.getElementById('c-name').value,
                email: document.getElementById('c-email').value,
                phone: document.getElementById('c-phone').value,
                plannedBudget: document.getElementById('c-budget').value,
                message: document.getElementById('c-message').value
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

                contactForm.style.display = 'none';
                successMessage.style.display = 'flex';
            
            } else {
                alert("Server Message: " + (data.message || "Email service requires activation. Please check tours@godwinhotels.com for an activation link."));
                if (submitBtn) {
                    submitBtn.innerText = 'Submit Concierge Request';
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
    }

    // Mobile Dropdown Menu Toggle
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
