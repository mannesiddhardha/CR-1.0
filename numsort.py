mystr = ['9.12.1.543.1233.77','7.21.3.99.572']

def numstring(mystr):
	for ele in mystr:
		sp = ele.split(".")
		#print sp
		result = sorted([int(i) for i in sp])
		#print result
		st = [str(i) for i in result]
		#print st
		print '.'.join(st)


numstring(mystr)
