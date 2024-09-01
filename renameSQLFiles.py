#! python3
# renameSQLFiles.py - Renames SQL filenames by adding a leading zero to files whose names contain one digit.
#
# Usage:
#   python renameSQLFiles.py <directory_path>
#
#   <directory_path> - The path to the directory containing the SQL files to be renamed.
#
# Description:
#   This script scans the specified directory for SQL files that have a single digit in their filename.
#   It then renames those files by adding a leading zero before the digit. For example, a file named
#   'basic9_grouping.sql' would be renamed to 'basic09_grouping.sql'.
#
# Requirements:
#   - Python 3
#   - The 'shutil', 'os', 'sys', and 're' modules are part of the standard Python library.

import shutil, os, sys, re

# Creating a regex that matches file names.
fileNamePattern = re.compile(r"""
    ^([a-zA-Z]+)                    # all alphabet characters before the numbers
    (\d)                            # one digit
    ([^(\n|\d)]*)                   # any characters except line feed and digit
    (\.sql)$                        # the '.sql' file extension
    """, re.VERBOSE)

def rename_files_in_directory(path):
    fullPath = os.path.abspath(path)

    if not os.path.exists(fullPath):
        print(f"Error: The directory {fullPath} does not exist.")
        return

    for currentFileName in os.listdir(fullPath):
        matchObject = fileNamePattern.search(currentFileName)

        # Skipping files not containing the sql pattern
        if matchObject is None:
            continue

        # Partitioning the filename.
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
        try:
            shutil.move(currentFileName, newFilename)
        except Exception as e:
            print(f"Error renaming {currentFileName}: {e}")

    print('All files successfully renamed!')

if __name__ == "__main__":
    argv = sys.argv

    if len(argv) > 1:
        path = argv[1]  # Extracting the path
        rename_files_in_directory(path)
    else:
        print("Usage: python renameSQLFiles.py <directory_path>")
