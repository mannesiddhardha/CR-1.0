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
