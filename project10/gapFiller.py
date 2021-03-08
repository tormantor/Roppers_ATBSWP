import os, shutil,re
from pathlib import Path as path

folder=input('Absolute path to folder: ')
os.chdir(folder)
prefix='spam_'
suffixRegex=re.compile(r'^(spam_)(\d+)(.txt)$')
files=[i for i in os.listdir(path.cwd()) if path.is_file(path(i)) and suffixRegex.search(i)]
suffixLength=len(suffixRegex.search(files[0]).groups()[1])
fileSuffixes=[int(suffixRegex.search(i).groups()[1]) for i in files]
missingSuffixes=[]
for i in range(max(fileSuffixes)):
	if i+1 not in fileSuffixes:
		missingSuffixes.append(i+1)
newMax=(max(fileSuffixes)-len(missingSuffixes))
for i in range(newMax):
	shutil.move(path.cwd()/files[i],path.cwd()/f'spam_{str(i+1).zfill(suffixLength)}.txt')	
