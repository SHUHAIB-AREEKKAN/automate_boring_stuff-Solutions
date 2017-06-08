birth={'Alice':'apr 1','Bob':'Dec 1','Carol':'Mar 4'}

while True:
	print("enter your name")
	name=input()
	if name == '':
		break


	if name in birth:
		print(birth[name] +' is the birthday of' +name)
	else:
		print("sory ur brth day doesn't exisist");
		print("what is your birthday ");
		bday=input()
		birth[name] = bday
		print('birthday up to date');
		print(birth);
	



