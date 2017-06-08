import re

reg1=re.compile(r'^\s+')
reg2=re.compile(r'\s+$')
newstr=''

def newStrip(first,second=''):
	if second == '' :
		newstr=reg1.sub('',first)
		newstr2=reg2.sub('',newstr)
		return newstr2
		
		
	else:
		print('new execution arg2 present')
		print(first)
		print(second)
		reg3=re.compile(second)
		return reg3.sub('',first)


 
name=' the best ext solution for the ext random value '
sec='ext'
sec2=''

print('Before stripping input:'+name)
print(' After stripping input:'+newStrip(name,sec2))

print("the second method")
newstr3=newStrip(name,sec)

print('after stripping ext '+newstr3)
