# Description
# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re

def stripWithRegex(unstriptedString, charactersToStrip = ' '):
    '''
        This function strips the leading and trailing characters from a string using regular expressions.
        By default, it strips spaces, but you can pass other characters as well.
    '''

    # Creating a regex pattern to match the characters to strip at the start and end of the string.
    regexPattern = rf'^[{re.escape(charactersToStrip)}]+|[{re.escape(charactersToStrip)}]+$'

    return re.sub(regexPattern, '', unstriptedString)


# Tests.
defaultStripTests = [
    ("  Hello World  ", "Hello World"),  # Leading and trailing spaces
    ("Hello World", "Hello World"),      # No leading or trailing spaces
    ("   Leading spaces", "Leading spaces"),  # Leading spaces only
    ("Trailing spaces   ", "Trailing spaces"),  # Trailing spaces only
    ("   ", ""),                        # Only spaces
    ("", ""),                           # Empty string
    ("NoSpaces", "NoSpaces"),           # No spaces at all
]

customStripTests = [
    ("$$$Hello World$$$", '$', "Hello World"),  # Strip $ characters
    ("###Hello World###", '#', "Hello World"),  # Strip # characters
    ("***Hello***World***", '*', "Hello***World"),  # Strip * characters
    ("&&&&Test&&&&", '&', "Test"),               # Strip & characters
    ("--==Test==--", "-=", "Test"),              # Strip both - and = characters
    ("abcHello Worldabc", 'abc', "Hello World"), # Strip 'a', 'b', and 'c' characters
    ("!!**Hello**!!", "!*", "Hello"),            # Strip ! and * characters
    ("@@123@@@", '@', "123"),                    # Strip @ characters
    ("###  Mixed  ###", '# ', "Mixed"),          # Strip # and space characters
    ("### 123 ###", '# ', "123"),                # Strip # and space characters
]

edgeCaseTests = [
    ("Hello World", "xyz", "Hello World"),  # No characters to strip
    ("@#@Hello World@#@", '@#', "Hello World"),  # Characters to strip from start and end
    ("!!!@@@###", '!@#', ""),              # Only characters to strip
    ("Hello@World@", "@", "Hello@World"),  # Only trailing @
    ("Hello World!", "!", "Hello World"),  # Only trailing special character
    ("12345", "5", "1234"),                # Only trailing number
    ("12345", "1", "2345"),                # Only leading number
    ("...Test...", '.', "Test"),           # Leading and trailing dots
    ("12345", "15", "234"),                # Strip specific digits
    ("     ", " ", ""),                    # Only spaces with custom strip character
]

def runTests():
    # Test default stripping (spaces)
    for original, expected in defaultStripTests:
        result = stripWithRegex(original)
        print(f"Original: '{original}' -> Stripped: '{result}' (Expected: '{expected}')")
        assert result == expected, f"Test failed for input '{original}'"

    # Test custom character stripping
    for original, charsToStrip, expected in customStripTests:
        result = stripWithRegex(original, charsToStrip)
        print(f"Original: '{original}' -> Stripped: '{result}' (Expected: '{expected}')")
        assert result == expected, f"Test failed for input '{original}' with strip characters '{charsToStrip}'"

    # Test edge cases
    for original, charsToStrip, expected in edgeCaseTests:
        result = stripWithRegex(original, charsToStrip)
        print(f"Original: '{original}' -> Stripped: '{result}' (Expected: '{expected}')")
        assert result == expected, f"Test failed for input '{original}' with strip characters '{charsToStrip}'"

runTests()
