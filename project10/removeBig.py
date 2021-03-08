#! python
import os,shutil

folder=os.path.abspath(input('Enter the folder to search in: '))
os.chdir(folder)
for folderName,subFolders,fileNames in os.walk(folder):
	for fileName in fileNames:
		fileName=os.path.abspath(os.path.join(folderName,fileName))
		if os.path.getsize(fileName)/10**6 > 100:
			print(f'Deleting {fileName} size={os.path.getsize(fileName)} bytes')
			os.unlink(fileName)
