def collatz(number):
	if number % 2 == 0:
		return (number // 2)
	else:
		return (3 * number + 1)

print(" welcome to collatxz");

status=2

while status != 1:
	try:	
		print("enter int value for collatz")
		arg=int(input())
		status=collatz(arg)
		print(status)	
	except ValueError:
		print("enter valid Integer")
		continue
		

print("exit")

 
