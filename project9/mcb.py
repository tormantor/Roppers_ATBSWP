import sys
import shelve
from pyperclip import copy
from pyperclip import paste
from pathlib import Path as path

keywords=shelve.open('keywords')
if len(sys.argv)==3:
	if sys.argv[1]=='save':
		keywords[sys.argv[2]]=paste()
	elif sys.argv[1]=='delete' and sys.argv[2] in keywords:
		del keywords[sys.argv[2]]
elif len(sys.argv)==2:
	if sys.argv[1]=='list':
		copy(str(list(keywords.keys())))
	elif sys.argv[1] in keywords:
		copy(keywords[sys.argv[1]])
	elif sys.argv[1]=='delete':
		for i in keywords.keys():
			del keywords[i]					
