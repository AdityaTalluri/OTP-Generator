# 🔐 Random OTP Generator (Python)

A  Python script that generates a **numeric One-Time Password (OTP)** with 4 or 5 digits. Perfect for testing auth flows, simulating 2FA, or learning how random number generation works.

---

## 📦 Features

- ✅ Generates 4- or 5-digit OTPs
- 🔢 Only uses numeric characters (0–9)
- 🎲 Random length on each run
- 🧼 No third-party dependencies
- 🐍 Pure Python 3.x

---

## 🚀 How to Use

### 1. Save the script as `otp_generator.py`

### 2. Run it in your terminal:
```bash
python otp_generator.py

### 3. Use this Source Code:
```python
import random


def make_OTP():
    # Get a list of all possible numbers
    all_chars = '1234567890'

    # Choose a length for the OTP
    length = random.randint(4, 5)

    # Make a OTP by picking random characters
    OTP = ''
    for i in range(length):
        OTP += random.choice(all_chars)

    return OTP


# Make a OTP and print it
print("Your OTP is:",make_OTP())
