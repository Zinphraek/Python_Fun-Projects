#! python3
# renameDates.py - Renames filenames with American date format to European format.

import shutil, os, re

# Creating a regex that matches files with American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d{2})                  # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Looping over the file in the working directory.
for usFileName in os.listdir('.'):
    matchObject = datePattern.search(usFileName)

    # Skippig files not containning dates
    if matchObject == None:
        continue

    # Partitionning the filename.
    beforeDateSection = matchObject.group(1)
    monthSection = matchObject.group(2)
    daySection = matchObject.group(4)
    yearSection = matchObject.group(6)
    afterDateSection = matchObject.group(8)

    # Forming European-style filename.
    euFilename = beforeDateSection + daySection + '-' + monthSection + '-' + yearSection + afterDateSection

    # Getting the full and absolute file paths.
    absWorkingDir = os.path.abspath('.')
    usFileName = os.path.join(absWorkingDir, usFileName)
    euFilename = os.path.join(absWorkingDir, euFilename)

    # Renaming the file
    print(f'Renaming "{usFileName}" to "{euFilename}"...')
    # shutil.move(usFileName, euFilename)
