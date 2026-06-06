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

            fetch("https://formsubmit.co/ajax/book@godwinhotels.com", {
                method: "POST",
                headers: { 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(() => {
                contactForm.style.display = 'none';
                successMessage.style.display = 'flex';
            })
            .catch(err => {
                console.error(err);
                submitBtn.innerText = 'Error. Try Again.';
                submitBtn.disabled = false;
            });
        });
    }
});
