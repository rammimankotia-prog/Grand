import re

# 1. Read script.js and modify it for car-booking.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace variables
js = js.replace('fromStation', 'pickupPoint')
js = js.replace('toStation', 'droppingPoint')
js = js.replace('fromStation.value', 'pickupPoint.value')
js = js.replace('toStation.value', 'droppingPoint.value')

# Remove swap logic (doesn't make as much sense for multi-city routing or can be buggy)
js = re.sub(r'// Swap Stations.*?}\);', '', js, flags=re.DOTALL)

# Remove class chips logic
js = re.sub(r'// Class Selection Chips.*?// Nationality to Passport Logic', '// Nationality to Passport Logic', js, flags=re.DOTALL)
js = re.sub(r'classChips\.forEach.*?classInput\.value = \'any\';', '', js, flags=re.DOTALL)

# Remove passenger counter JS logic since we're switching to native input
js = re.sub(r'// Passenger Counter.*?// Nationality to Passport Logic', '// Nationality to Passport Logic', js, flags=re.DOTALL)
js = js.replace("passengerCountDisplay.textContent = '1';", "")

# Fix name validation to handle firstName and lastName
js = re.sub(r'const nameInput = document\.getElementById\(\'fullName\'\);.*?\}', '''
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
''', js, flags=re.DOTALL)

with open('car-booking.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Fix car-booking.html
with open('car-booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Point to car-booking.js
html = html.replace('<script src="script.js"></script>', '<script src="car-booking.js"></script>')

# Replace custom counter with native input
custom_counter = """<div class="passenger-counter">
                  <button type="button" class="counter-btn" id="decreaseBtn">−</button>
                  <span class="counter-value" id="passengerCount">1</span>
                  <input type="hidden" id="passengers" name="passengers" value="1"/>
                  <button type="button" class="counter-btn" id="increaseBtn">+</button>
                  <span class="counter-label">Person(s)</span>
                </div>"""

native_counter = """<div class="input-wrap icon-left">
                  <span class="input-icon">👥</span>
                  <input type="number" id="passengers" name="passengers" min="1" max="16" value="2" class="field-input" required/>
                  <div class="input-glow"></div>
                </div>"""

html = html.replace(custom_counter, native_counter)

with open('car-booking.html', 'w', encoding='utf-8') as f:
    f.write(html)
