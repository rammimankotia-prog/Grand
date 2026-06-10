import re

with open('train-booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace general Train text with Car
html = html.replace('title>Book Indian Railway Tickets | RailYatra', 'title>Book Private Car & Driver | DriveIndia')
html = html.replace('Rail<span class="logo-accent">Yatra</span>', 'Drive<span class="logo-accent">India</span>')
html = html.replace('🚄', '🚘')
html = html.replace('Instantly book your Indian train tickets', 'Instantly book your private car and driver')
html = html.replace('Indian railway booking', 'India private car booking')
html = html.replace('train-booking.html', 'car-booking.html')
html = html.replace('PNR Status', 'Fleet Options')
html = html.replace('https://www.confirmtkt.com/pnr-status', '#')
html = html.replace('Train Schedule', 'Rental Rates')
html = html.replace('https://www.confirmtkt.com/train-schedule', '#')

# Hero section
html = html.replace('All India Train Network', 'All India Car Rental Network')
html = html.replace('With Every Train', 'With A Private Driver')
html = html.replace('Book tickets for any train, any class, any route', 'Book private vehicles for any route across India')
html = html.replace('<span class="stat-num">13,000+</span>\n          <span class="stat-label">Trains</span>', '<span class="stat-num">500+</span>\n          <span class="stat-label">Vehicles</span>')
html = html.replace('<span class="stat-num">8,000+</span>\n          <span class="stat-label">Stations</span>', '<span class="stat-num">All</span>\n          <span class="stat-label">India Destinations</span>')
html = html.replace('Ticket Booking', 'Car Booking')
html = html.replace('Book Your Train Journey', 'Book Your Private Car')
html = html.replace("we'll find the best trains for your route", "we'll arrange the perfect vehicle and driver for you")

# Form Replacement
# We want to replace the entire <form id="mainBookingForm" novalidate> ... </form> section.
# The user wants specific fields. I'll craft a custom form block that perfectly matches the existing design system.

form_html = """
      <form class="booking-form" id="mainBookingForm" novalidate>

        <!-- ── JOURNEY DETAILS ── -->
        <div class="form-card" id="journey-card">
          <div class="card-header">
            <div class="card-icon">🗺️</div>
            <div>
              <h3 class="card-title">Journey Details</h3>
              <p class="card-desc">Where would you like to travel?</p>
            </div>
          </div>
          <div class="card-body">

            <!-- Route Row -->
            <div class="form-row two-col">
              <div class="field-group">
                <label for="pickupPoint" class="field-label required">Pickup Point</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">🏁</span>
                  <input type="text" id="pickupPoint" name="pickupPoint" class="field-input" placeholder="Enter pickup city or hotel" required/>
                  <div class="input-glow"></div>
                </div>
              </div>

              <div class="field-group">
                <label for="droppingPoint" class="field-label required">Dropping Point</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">📍</span>
                  <input type="text" id="droppingPoint" name="droppingPoint" class="field-input" placeholder="Enter drop-off city or hotel" required/>
                  <div class="input-glow"></div>
                </div>
              </div>
            </div>

            <!-- Destination -->
            <div class="form-row">
              <div class="field-group">
                <label for="destinations" class="field-label required">Destination(s) to be Visited</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">🛣️</span>
                  <input type="text" id="destinations" name="destinations" class="field-input" placeholder="e.g. Delhi, Jaipur, Agra, Udaipur..." required/>
                  <div class="input-glow"></div>
                </div>
              </div>
            </div>

            <!-- Date & Passengers -->
            <div class="form-row two-col">
              <div class="field-group">
                <label for="journeyDate" class="field-label required">Date of Journey</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">📅</span>
                  <input type="date" id="journeyDate" name="journeyDate" class="field-input" required/>
                  <div class="input-glow"></div>
                </div>
              </div>
              <div class="field-group">
                <label for="passengers" class="field-label required">Number of Pax (Guests)</label>
                <div class="passenger-counter">
                  <button type="button" class="counter-btn" id="decreaseBtn">−</button>
                  <span class="counter-value" id="passengerCount">1</span>
                  <input type="hidden" id="passengers" name="passengers" value="1"/>
                  <button type="button" class="counter-btn" id="increaseBtn">+</button>
                  <span class="counter-label">Person(s)</span>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- ── CONTACT DETAILS ── -->
        <div class="form-card" id="contact-card">
          <div class="card-header">
            <div class="card-icon">👤</div>
            <div>
              <h3 class="card-title">Passenger &amp; Contact Information</h3>
              <p class="card-desc">Required for booking confirmation</p>
            </div>
          </div>
          <div class="card-body">

            <!-- Name -->
            <div class="form-row two-col">
              <div class="field-group">
                <label for="firstName" class="field-label required">First Name</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">🧑</span>
                  <input type="text" id="firstName" name="firstName" class="field-input" placeholder="First Name" required/>
                  <div class="input-glow"></div>
                </div>
                <span class="field-error" id="firstNameError"></span>
              </div>
              <div class="field-group">
                <label for="lastName" class="field-label required">Last Name</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">🧑</span>
                  <input type="text" id="lastName" name="lastName" class="field-input" placeholder="Last Name" required/>
                  <div class="input-glow"></div>
                </div>
                <span class="field-error" id="lastNameError"></span>
              </div>
            </div>

            <!-- Contact -->
            <div class="form-row two-col">
              <div class="field-group">
                <label for="mobileNumber" class="field-label required">Mobile Number</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">📱</span>
                  <input type="tel" id="mobileNumber" name="mobileNumber" class="field-input" placeholder="Include country code" required/>
                  <div class="input-glow"></div>
                </div>
                <span class="field-error" id="mobileError"></span>
              </div>
              <div class="field-group">
                <label for="emailId" class="field-label required">Email Address</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">✉️</span>
                  <input type="email" id="emailId" name="emailId" class="field-input" placeholder="your@email.com" required/>
                  <div class="input-glow"></div>
                </div>
                <span class="field-error" id="emailError"></span>
              </div>
            </div>

            <!-- Nationality -->
            <div class="form-row">
              <div class="field-group">
                <label for="nationality" class="field-label required">Nationality</label>
                <div class="input-wrap icon-left">
                  <span class="input-icon">🌍</span>
                  <input type="text" id="nationality" name="nationality" class="field-input" placeholder="Enter your nationality" required/>
                  <div class="input-glow"></div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- TERMS & SUBMIT -->
        <div class="form-footer">
          <label class="terms-label" for="whatsappConsent">
            <input type="checkbox" id="whatsappConsent" name="whatsappConsent" checked/>
            <span class="custom-check"></span>
            <span>I consent to receive booking updates via WhatsApp</span>
          </label>

          <label class="terms-label" for="termsCheck">
            <input type="checkbox" id="termsCheck" name="terms" required/>
            <span class="custom-check"></span>
            <span>I agree to the <a href="#" class="terms-link">Terms & Conditions</a> and <a href="#" class="terms-link">Privacy Policy</a></span>
          </label>

          <button type="submit" class="submit-btn" id="submitBtn">
            <span class="btn-text">🔍 Search &amp; Book Vehicle</span>
            <span class="btn-spinner" id="btnSpinner"></span>
          </button>
        </div>

      </form>
"""

# Extract the old form and replace it
form_pattern = re.compile(r'<form class="booking-form" id="mainBookingForm" novalidate>.*?</form>', re.DOTALL)
html = form_pattern.sub(form_html, html)

# Replace modal text
html = html.replace("we've received your train booking request", "we've received your car booking request")

with open('car-booking.html', 'w', encoding='utf-8') as f:
    f.write(html)
