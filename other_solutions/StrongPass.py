#! /usr/bin/python3
# strong password 

import re

def checkPass():
	user_pass=input("enter the pass for check  ")
	print(user_pass)
	if re.match(r'[A-Za-z0-9@#$%^&+=()_]{8,}',user_pass):
		print("Its good password")
	else:
		print("try new strong pass")

checkPass()







