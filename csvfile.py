import csv

with open("/Users/mannesiddhardha/Desktop/test.csv",'r') as fr:
	cr = csv.DictReader(fr)
	for line in cr:
		print(line['lastname'],line['email'])
    
    
# csv.reader(fr, delimiter=',')

# csv.reader(fr)
# we can get output in list format, parse with the index's

#csv.DictReader(fr)
#output in dictionary format, parse with the keys


# 2nd column 2nd row element in a csv file

with open('/Users/mannesiddhardha/Desktop/test.csv','r') as fr:
	cr = csv.reader(fr)
	# indexes parse the columns first
	result = [line[2] for line in cr]
	# once you have the list go to the specific row number you want

	print result[2]
	
