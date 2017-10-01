def fileparser():
	fileopen = open("/Users/mannesiddhardha/Desktop/study/python_learning/log files/ips.rtf", "r")
	pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
	for line in fileopen:
		result = pattern.findall(line)
		print result
