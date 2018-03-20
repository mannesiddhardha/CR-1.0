#!/usr/bin/python

#base class
class data:
	def __init__(self,name,age,location):
		self.name = name
		self.age = age
		self.location = location
	def fund(self):
		print 'my {} and {} in {}'.format(self.name,self.age,self.location)

#derived class
class idata(data):
    def __init__(self,name,age,location):
        data.__init__(self,name,age,location)
    def ifund(self):
        print 'my {} and {} in {}'.format(self.name,self.age,self.location)


mydata = data('sidhu',27,'mi')
toodata = idata('boby',27,'ga')

print(idata.ifund(toodata))
