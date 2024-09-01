#! python3
# renameSQLFiles.py - Renames sql filenames by adding leading zero to file whose name contain one digit.

import shutil, os, sys, re

# Creating a regex that matches files names.
fileNamePattern = re.compile(r"""
    ^([a-zA-Z]+)                    # all alphabet characters before the numbers
    (\d)                            # one digit
    ([^\n]*)                        # one or more characters
    (\.sql)$                        # the '.sql' file extension
    """, re.VERBOSE)

# Looping over the file in the target directory.
argv = sys.argv

if len(argv) > 1:
    path = argv[1:][0]  # Extracting the path
    fullPath = os.path.abspath(path)
    for currentFileName in os.listdir(fullPath):
        matchObject = fileNamePattern.search(currentFileName)

        # Skipping files not containning sql pattern
        if matchObject == None:
            continue

        # Partitionning the filename.
        beforeNumberSection = matchObject.group(1)
        numberSection = matchObject.group(2)
        afterNumberSection = matchObject.group(3)
        extensionSection = matchObject.group(4)

        # Forming new filename.
        newFilename = beforeNumberSection + '0' + numberSection + afterNumberSection + extensionSection

        # Getting the full and absolute file paths.
        currentFileName = os.path.join(path, currentFileName)
        newFilename = os.path.join(path, newFilename)

        # Renaming the file
        print(f'Renaming "{currentFileName}" to "{newFilename}"...')
        shutil.move(currentFileName, newFilename)
    print('All files successfully renamed!')
