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

  // Swap Stations
  const swapBtn = document.getElementById('swapBtn');
  const fromStation = document.getElementById('fromStation');
  const toStation = document.getElementById('toStation');

  swapBtn.addEventListener('click', () => {
    const temp = fromStation.value;
    fromStation.value = toStation.value;
    toStation.value = temp;
    
    // Add brief animation
    swapBtn.style.transform = 'rotate(180deg) scale(1.1)';
    setTimeout(() => {
      swapBtn.style.transform = '';
    }, 300);
  });

  // Passenger Counter
  const decreaseBtn = document.getElementById('decreaseBtn');
  const increaseBtn = document.getElementById('increaseBtn');
  const passengerCountDisplay = document.getElementById('passengerCount');
  const passengerInput = document.getElementById('passengers');

  decreaseBtn.addEventListener('click', () => {
    let count = parseInt(passengerInput.value);
    if (count > 1) {
      count--;
      passengerInput.value = count;
      passengerCountDisplay.textContent = count;
    }
  });

  increaseBtn.addEventListener('click', () => {
    let count = parseInt(passengerInput.value);
    if (count < 6) { // Max 6 per booking normally
      count++;
      passengerInput.value = count;
      passengerCountDisplay.textContent = count;
    } else {
      alert('Maximum 6 passengers allowed per booking.');
    }
  });

  // Class Selection Chips
  const classChips = document.querySelectorAll('.class-chip');
  const classInput = document.getElementById('classPreference');

  classChips.forEach(chip => {
    chip.addEventListener('click', () => {
      // Remove active from all
      classChips.forEach(c => c.classList.remove('active'));
      // Add active to clicked
      chip.classList.add('active');
      // Update hidden input
      classInput.value = chip.dataset.value;
    });
  });

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
    const nameInput = document.getElementById('fullName');
    const nameError = document.getElementById('nameError');
    if (nameInput.value.trim().length < 3) {
      nameError.textContent = 'Please enter your full name';
      isValid = false;
    } else {
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
    if (!fromStation.value.trim() || !toStation.value.trim()) {
      isValid = false;
      if (!fromStation.value.trim()) fromStation.focus();
      else toStation.focus();
    } else if (fromStation.value.trim().toLowerCase() === toStation.value.trim().toLowerCase()) {
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
    passengerCountDisplay.textContent = '1';
    classChips.forEach(c => c.classList.remove('active'));
    document.getElementById('class-any').classList.add('active');
    classInput.value = 'any';
    
    window.scrollTo({top: 0, behavior: 'smooth'});
  });

});
