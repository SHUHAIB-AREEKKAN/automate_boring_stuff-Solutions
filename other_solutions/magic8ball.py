import random
def getAnswer(answernumber):
	if answernumber == 1:
		return 'its certain'
	elif answernumber == 2:
		return 'its is decidely do'
	elif answernumber == 3:
		return 'yes'


r = random.randint(1,3)
fortune = getAnswer(r)
print(fortune)
