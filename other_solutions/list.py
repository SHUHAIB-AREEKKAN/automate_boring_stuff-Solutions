petName=[]
while True:
	print('enter the'+ str(len(petName)+1)+ 'petname or enter exitt')
	name=input();		
	if name=='exit':
		break
	petName=petName+[name]
	

print('the petnames');
for name in petName:
	print (' '+name);


	
	
