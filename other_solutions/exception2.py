def spam(inputs):
	return 42 / inputs
    
   
try:
	print(spam(2))
	print(spam(3))
	print(spam(0))
	print(spam(4))

except ZeroDivisionError:
                print("occured zero division error")


