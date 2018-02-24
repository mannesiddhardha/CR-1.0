def cmpr(file1,file2):
	with open(file1,'r') as f1:
		with open(file2,'r') as f2:
			same = set(f1).intersection(f2)
			print same

