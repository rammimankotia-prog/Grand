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

            // Simulate secure API post
            setTimeout(() => {
                contactForm.style.display = 'none';
                successMessage.style.display = 'flex';
            }, 2000);
        });
    }
});
