# Description
# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12,
# and the years range from 1000 to 2999. Note that if the day or month is a single digit,
# it’ll have a leading zero.
# 01-09, 10-19, 20-29, 30-31

import re

def isValidDate(dateString):
    """A regex function to identify valid date"""

    dateRegex = re.compile(r'''(
        ^(0[1-9]|[12][0-9]|3[01])/          # Day group
        (0[1-9]|1[0-2])/                    # Month group
        ((1|2)\d{3})$                       # Year group
    )
    ''', re.VERBOSE)
    matchedDateObject = dateRegex.match(dateString)
    if not matchedDateObject:
        return False

    day, month, year = matchedDateObject.group(2), matchedDateObject.group(3), matchedDateObject.group(4)
    # print(f"day: {day}, month: {month}, year: {year}")

    isLeapYear = (int(year) % 100 == 0 and int(year) % 400 == 0) or (int(year) % 4 == 0)

    if month == '02' and isLeapYear and int(day) > 29:
        return False

    if (month in ['04', '06', '09', '11'] and day == '31') or (month == '02' and not isLeapYear and int(day) > 28):
        return False

    return True


# Tests

validDates = [
    "01/01/2020",  # Regular valid date
    "29/02/2020",  # Leap year valid date
    "31/01/2021",  # End of January
    "30/04/2021",  # End of April, a month with 30 days
    "28/02/2021",  # Non-leap year February
    "31/12/2099",  # End of the valid century range
    "15/07/1500",  # Middle valid date
    "10/10/1000",  # Start of the valid century range
]

invalidDates = [
    "32/01/2020",  # Invalid day (32 doesn't exist)
    "00/01/2020",  # Invalid day (00 doesn't exist)
    "29/02/2021",  # Invalid leap year day
    "31/04/2021",  # April has only 30 days
    "31/06/2021",  # June has only 30 days
    "31/09/2021",  # September has only 30 days
    "31/11/2021",  # November has only 30 days
    "30/02/2020",  # February has at most 29 days in a leap year
    "30/02/2021",  # February has only 28 days in a non-leap year
    "15/13/2020",  # Invalid month (13 doesn't exist)
    "15/00/2020",  # Invalid month (00 doesn't exist)
    "31/12/0999",  # Year out of range (before 1000)
    "01/01/3000",  # Year out of range (beyond 2999)
    "31-12-2020",  # Invalid format (hyphens instead of slashes)
    "2020/12/31",  # Invalid format (year first)
]

for date in validDates:
    result = isValidDate(date)
    print(f"Testing {date}: {'Valid' if result else 'Invalid'} (Expected: Valid)")

for date in invalidDates:
    result = isValidDate(date)
    print(f"Testing {date}: {'Valid' if result else 'Invalid'} (Expected: Invalid)")
