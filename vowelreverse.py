import re
def rev(mystr):
	string = list(mystr)
	vowels = 'aeiou'
	print string
	i,j=0,len(string)-1
	while i<j:
		if string[i].lower() not in vowels:
			i += 1
		elif string[j].lower() not in vowels:
			j -= 1
		else:
			string[i],string[j]=string[j],string[i]
			i += 1
			j -= 1
			print("".join(string))
			break

rev('sidhu')
