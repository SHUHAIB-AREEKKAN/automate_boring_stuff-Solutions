#! /usr/bin/python3
# multi clip board save and loads of text to the clipboard
#Usage:python3 MultipclipBoard.py save <keyword> -saves clipboard to keyword
#      python3 MultipclipBoard.py <keyword> -Loads keyword to clipboard
#      python3 MultipclipBoard.py list -Loads all keywords to clipboard

import shelve,pyperclip,sys

mcbshelf =shelve.open('mcb')

if len(sys.argv) == 2 and sys.argv[1].lower()=='delete':
	del mcbshelf[sys.argv[2]]
elif len(sys.argv) ==1 and sys.argv[1].lower()=='deleteall':
	mcbshelf.clear()




if len(sys.argv) == 3 and sys.argv[1].lower()== 'save':
	mcbshelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv) ==2:
	#list keyword and load content
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbshelf.keys())))
	elif sys.argv[1] in mcbshelf:
		pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()



