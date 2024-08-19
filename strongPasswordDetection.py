# Description
# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit.
# You may need to test the string against multiple regex patterns to validate its strength.


import re

def isPasswordStrong(passwordString):
    '''A function checking whether a password is strong.
        A strong password is defined as one that is at least eight characters long,
        contains both uppercase and lowercase characters, at least one digit,
        and at least one special character from !@#$%^&*()-=+~.
    '''

    passwordRegex = re.compile(r'''
        ^(?=.*\d)       # Must contain at least one digit
        (?=.*[a-z])     # Must contain at least one lowercase letter
        (?=.*[A-Z])     # Must contain at least one uppercase letter
        (?=.*\W)        # Must contain at least one special character
        .{8,}$          # Must be at least 8 characters long
    ''', re.VERBOSE)

    return bool(passwordRegex.match(passwordString))


# Test

validPasswords = [
    "Aa1!abcd",         # Minimum length with all required elements
    "Str0ngP@ssword",   # Longer password with all required elements
    "Abc123!@",         # Contains uppercase, lowercase, digits, and special characters
    "P@ssw0rd2021",     # Contains all required elements with digits
    "Complex!1Word",    # Contains special character, digits, uppercase, and lowercase
    "12CharActer$",     # Exactly 8 characters with all required elements
]

invalidPasswords = [
    "abcdefg",          # No uppercase, digits, or special characters
    "ABCDEFGH",         # No lowercase, digits, or special characters
    "12345678",         # No letters or special characters
    "abcdEFGH",         # No digits or special characters
    "Abcdefgh",         # No digits or special characters
    "1234!@#$",         # No letters
    "ABCD!@#$",         # No lowercase or digits
    "abcd!@#$",         # No uppercase or digits
    "Short1!",          # Too short (7 characters)
    "NoSpecial1",       # No special characters
]


for password in validPasswords:
    result = isPasswordStrong(password)
    print(f"Testing '{password}': {'Valid' if result else 'Invalid'} (Expected: Valid)")

for password in invalidPasswords:
    result = isPasswordStrong(password)
    print(f"Testing '{password}': {'Valid' if result else 'Invalid'} (Expected: Invalid)")
