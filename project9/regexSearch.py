import re
from pathlib import Path as path
import os

folderPath=input('Enter the absolute path to the folder: ')
customRegex=re.compile(input('Enter the custom regex: '))
if folderPath:
	os.chdir(folderPath)
files=os.listdir()
files=[i for i in files if '.txt' in i]
for i in files:
	textFile=open(i,'r')
	lineCount=1
	for j in textFile.readlines():
		if	customRegex.findall(j):
			for i in customRegex.findall(j):
				print(f'Match found at line {lineCount} of file {i}:',j,sep='\n')
		lineCount+=1	
