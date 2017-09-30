import re

def validation(pwd):
	while True:
		if len(pwd) < 8:
			print "invalid length"
			break
		elif re.search('[@]', pwd) is None:
			print "invalid or no symbol"
			break
		elif re.search('[a-z]', pwd) is None:
			print "no lower case"
			break
		elif re.search('[A-Z]', pwd) is None:
			print "no upper case"
			break
		elif re.search('[0-9]', pwd) is None:
			print "no numericals"
			break
		else:
			print "valid password", pwd
			break


validation("SIdhu@1233")
