#!/use/bin/env python


def fun1(*args):
	for arg in args:
		print(arg),
		print(len(args))


def fun(**kwargs):
	for key,value in kwargs.items():
		print("key={} and vaule={}".format(key,value))


fun(name='sidhu',id=1233) #dictionary

fun1('sidhu',1233) #list
