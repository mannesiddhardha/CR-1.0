def fileparser():
	fileopen = open("/Users/mannesiddhardha/Desktop/study/python_learning/log files/one.txt", "r")
	pattern = re.compile(r"(500)")
	for line in fileopen:
		result = pattern.findall(line)
		print result
