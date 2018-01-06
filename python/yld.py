def ret():
	yield "s-1"
  yield "s-2"
  yield "s-3"
        
def test():
	tst = ret()
	for i in range(3):
		print tst.next()
    
test()
