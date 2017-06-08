#!python3
#phoneAndEmail.py -to find email addres and number in  raw text
import re,pyperclip

phoneRegex=re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''',re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
	phoneNum='-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum+='x'+groups[8]
	matches.append(phoneNum)

emailRegex=re.compile(r'''(
        [a-ZA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})
        )''',re.VERBOSE)

for group in emailRegex.findall(text):
	matches.append(group[0])

if len(matches) >0:
	pyperclip.copy('\n'.join(matches))
	print('copied to clipboard')
	print('\n'.join(matches))
else:
	print(' No phone number or email addresses found')

