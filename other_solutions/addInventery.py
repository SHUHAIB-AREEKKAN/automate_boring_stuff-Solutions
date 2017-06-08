stuff={'rope':2,'torch':6,'gold coin':42,'dagger':1,'arrow':14}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def add_to_Inv(inv,additem):
	
	for i in additem:
		if i in inv.keys():
			inv[i]+=1
		else:
			inv[i]=1

def printInventery(Inv):
	print("the Inventery Details")
	item_total=0;
	for k,v in Inv.items():
		print(k+' '+str(v))
		item_total=item_total+v
	print('the total inventery '+str(item_total))

add_to_Inv(stuff,dragonLoot)
printInventery(stuff)

	
