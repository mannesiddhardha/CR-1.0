import re
import os

operation = ['add','sub','mult','div']

for i in operation:
    print "these are the list of operations available:::",i
    
result = input("enter the operation:::")
num1 = int(raw_input("enter first number:::"))
num2 = int(raw_input("enter second number:::"))
if (result is 'add' and result in operation):
    print("addition::",num1+num2)
elif (result is 'sub' and result in operation):
    print("substraction::",num1-num2)
elif (result is 'mult' and result in operation):
    print("multiplication::",num1*num2)
elif (result is 'div' and result in operation):
    print("division::",float(num1)/float(num2))
else:
    print "invalid entry"