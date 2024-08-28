#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):

    # Obtaining the absolute path of the provided folder
    # regardless of its type (absolute or relative).
    folder = os.path.abspath(folder)

    # Forming the filename based on the existing ones
    fileVersion = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(fileVersion) + '.zip'
        if not os.path.exists(zipFilename):
            break
        fileVersion = fileVersion + 1

    # Creating the zip file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walking through the entire folder tre and compressing the files in each folder.
    for foldername, subfolders, filnames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Adding the current folder to the ZIP file.
        backupZip.write(foldername)

        # Adding all files in 'foldername' to the ZIP file.
        for filename in filnames:
            newBaseName = os.path.basename(folder) + '_'
            if filename.startswith(newBaseName) and filename.endswith('.zip'):
                continue # Do not back up the ZIP files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
