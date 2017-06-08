#! /usr/bin/python3
# removeCsvHeader.py - Removes the header from all csv files in current
# working directory

import csv,os

os.makedirs('headerRemoved',exist_ok=True)
#lopp through every file in the current working directory

for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
	print('removing header from '+csvFilename+'....')
	csvRows=[]
	csvFileObj=open(csvFilename)
	readerObj=csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num==1:
			continue #skipping first row
		csvRows.append(row)
	csvFileObj.close()
	# Write out the CSV file.
	csvFileObj=open(os.path.join('headerRemoved',csvFilename),'w',newline='')
	csvWriter=csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()


