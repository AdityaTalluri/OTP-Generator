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
