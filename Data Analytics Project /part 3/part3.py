"""
PART 3: Map/Reduce
Sanket Lawangare
@01435026

Running Instructions:In Terminal Run: python part3.py >anyfilename.txt 
the ouput file named "outputpart3.txt" is attached 

"""



import sys
import csv
import numpy as np

# Mapper Code

Array = np.array([])
with open('solardata.csv', 'rb') as f:
	
	rows = csv.reader(f, delimiter= ',')
	for row in rows:
		arr = row[0].strip(), row[4].strip()  # Print column date and ETR, strip surrounding 


		Array = np.append(np.array([Array]),np.array([arr]))
Array = np.reshape(Array,(Array.shape[0]/2,2))
		
	


# Reducer Code
#Red = np.array([])

lastKey = None
sumVal = 0
count =  0

print "Date \t Average ETR"
for line in Array :
    #key, val = line.strip().split('\t')
   	if len(line) != 2:
   		continue

   	thisKey, thisVal = line

   	if lastKey and lastKey != thisKey:
   		avgETR = sumVal/count	

       		print lastKey, avgETR
       		lastKey = thisKey
       		count = 0
       		sumVal = 0
    	#sumVal += float(thisVal)
    	count += 1
    	lastKey = thisKey
    	sumVal += float(thisVal)

if lastKey != None:
       # print '%s\t%s' % (lastKey, sumVal / float(count))
    print lastKey, "\t", sumVal / count







