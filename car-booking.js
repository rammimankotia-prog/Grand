document.addEventListener('DOMContentLoaded', () => {

  // Navbar scroll effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // Set minimum date to today
  const dateInput = document.getElementById('journeyDate');
  const today = new Date().toISOString().split('T')[0];
  dateInput.min = today;

  

  // Nationality to Passport Logic
  const nationalitySelect = document.getElementById('nationality');
  const passportGroup = document.getElementById('passportGroup');
  const passportInput = document.getElementById('passportNumber');

  if (nationalitySelect && passportGroup && passportInput) {
    nationalitySelect.addEventListener('change', (e) => {
      if (e.target.value !== 'indian') {
        passportGroup.style.display = 'block';
        passportInput.required = true;
      } else {
        passportGroup.style.display = 'none';
        passportInput.required = false;
        passportInput.value = '';
      }
    });
  }

  // Form Validation and Submission
  const bookingForm = document.getElementById('mainBookingForm');
  const submitBtn = document.getElementById('submitBtn');
  
  // Modals
  const successModal = document.getElementById('successModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalRef = document.getElementById('modalRef');

  bookingForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Basic Validation Custom Styling
    let isValid = true;

    // Validate Name
    
    const fnameInput = document.getElementById('firstName');
    const lnameInput = document.getElementById('lastName');
    const fnameError = document.getElementById('firstNameError');
    const lnameError = document.getElementById('lastNameError');
    if (fnameInput && fnameInput.value.trim().length < 2) {
      fnameError.textContent = 'Enter first name';
      isValid = false;
    } else if (fnameError) {
      fnameError.textContent = '';
    }
    if (lnameInput && lnameInput.value.trim().length < 2) {
      lnameError.textContent = 'Enter last name';
      isValid = false;
    } else if (lnameError) {
      lnameError.textContent = '';
    }
 else {
      nameError.textContent = '';
    }

    // Validate Mobile
    const mobileInput = document.getElementById('mobileNumber');
    const mobileError = document.getElementById('mobileError');
    const mobileRegex = /^\+?[0-9\s\-]{6,20}$/;
    if (!mobileRegex.test(mobileInput.value.trim())) {
      mobileError.textContent = 'Enter a valid mobile number with country code';
      isValid = false;
    } else {
      mobileError.textContent = '';
    }

    // Validate Stations
    if (!pickupPoint.value.trim() || !droppingPoint.value.trim()) {
      isValid = false;
      if (!pickupPoint.value.trim()) pickupPoint.focus();
      else droppingPoint.focus();
    } else if (pickupPoint.value.trim().toLowerCase() === droppingPoint.value.trim().toLowerCase()) {
      alert("Source and destination cannot be the same.");
      isValid = false;
    }

    if (!isValid) return;

    // Simulate API Call
    submitBtn.classList.add('loading');
    submitBtn.disabled = true;

    setTimeout(() => {
      submitBtn.classList.remove('loading');
      submitBtn.disabled = false;
      
      // Generate random PNR / Ref
      const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      let ref = 'RY';
      for(let i=0; i<8; i++) {
        ref += chars.charAt(Math.floor(Math.random() * chars.length));
      }
      
      modalRef.textContent = `Ref: ${ref}`;
      successModal.classList.add('show');
      
    }, 2000);
  });

  modalCloseBtn.addEventListener('click', () => {
    successModal.classList.remove('show');
    bookingForm.reset();
    
    // Reset custom elements
    
    
    
    window.scrollTo({top: 0, behavior: 'smooth'});
  });

});
