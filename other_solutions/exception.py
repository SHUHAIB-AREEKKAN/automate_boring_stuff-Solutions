def spam(inputs):
	try:	
		return 42 / inputs
	except ZeroDivisionError:
		print("occured zero division error")


print(spam(2))
print(spam(3))
print(spam(0))
print(spam(4))

