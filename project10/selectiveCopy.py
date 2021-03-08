#! python
import os,shutil
folder=os.path.abspath(input('Enter the folder to search in: '))
fileType=input('File type: ')
destination=input('Enter destination path: ')
for folderName,subFolders, fileNames in os.walk(folder):
	for fileName in fileNames:
		if fileName.endswith(fileType):
			print(f'Found a {fileType} file: {fileName}')
			print(f'Copying {fileName} to {destination}...')
			shutil.copy(os.path.join(os.path.abspath(folderName),fileName),os.path.join(destination,fileName))
print('Done.')						
