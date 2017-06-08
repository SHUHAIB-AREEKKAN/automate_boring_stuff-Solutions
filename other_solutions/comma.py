def commas(some):	
	add=' ,'
	ret=''
	temp=[]
	print(len(some))
	for i in  range(len(some)):
		if i == len(some)-2:
			ret=some[i]+add+'and'
			temp.append(ret);
			print(ret);
		else:	
			ret=some[i]+add
			temp.append(ret);
			print(ret)
	con_out=str(temp)		
	return con_out


spam=['a','b','c']

spm=commas(spam)
print(" origininal output");
print(spm);



