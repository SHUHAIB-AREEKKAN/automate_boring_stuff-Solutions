import re

phoneNumExp=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumExp.search('My number is.')
print("the number found :"+ mo.group())

