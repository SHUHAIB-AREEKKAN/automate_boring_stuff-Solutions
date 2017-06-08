def printPicnic(itemDict,left,right):
	print('PICNIC ITEMS'.center(left+right,'-'))
	for k,v in itemDict.items():
		print(k.ljust(left,'.')+str(v).rjust(right))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 10)
