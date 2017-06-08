allGuest={'Alice':{'apples':5,'pretzels':12},
	  'Bob':{'ham sandwich':3,'apples':2},
	  'Carol':{'cups':3,'apple pies':1}}

def totalBrought(guest, item):
	numBrought=0;
	for k,v in guest.items():
		numBrought=numBrought+v.get(item,0)
	return numBrought

print("The No of items and numbers Brought")
print(' - Apples  '+ str(totalBrought(allGuest,'apples')))
print(' - Cups    '+str(totalBrought(allGuest,'cups')))
print(' - Pretzels  '+ str(totalBrought(allGuest,'pretzels')))
print(' - Aplle pie  '+ str(totalBrought(allGuest,'apple pies')))
print(' - Hand Sandwiches '+ str(totalBrought(allGuest,'ham sandwich')))

	
