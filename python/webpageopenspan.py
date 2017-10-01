import urllib2
import time

def webpage():
	pg = urllib2.Request("https://www.google.com/")
	response = urllib2.urlopen(pg)
	html = response.read()

def pagespan():
	t0 = time.time()
	webpage()
	t1 = time.time()
	diff = t1 - t0
	print diff

pagespan()
