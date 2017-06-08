stuff={'rope':2,'torch':6,'gold coin':42,'dagger':1,'arrow':14}

def printInventery(Inv):
	print("the Inventery Details")
	item_total=0;
	for k,v in Inv.items():
		print(k+' '+str(v))
		item_total=item_total+v
	print('the total inventery '+str(item_total))
printInventery(stuff)
			
