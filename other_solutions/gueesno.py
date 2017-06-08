import random

print("i am think of number between 1 t0 20 \n"+"Take a guess")
sec_value=random.randint(1,20);
print(sec_value);
for i in range(1,7):
	print("please enter guess for the "+str(i))
	guess_value=int(input())
	if sec_value > guess_value:
		print("the seceret  value is higher");
	elif sec_value < guess_value:
		print("the secret value is low");
	else:
		break



if sec_value == guess_value:
	print("guess is right and the no of attempts"+str(i));
else:
	print("Guess is not right  "+str(sec_value)+"\tis the secret value");






