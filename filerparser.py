#!/usr/bin/python
#sample python program
import re
import subprocess
file = open("/Users/mannesiddhardha/Desktop/study/python_learning/logfiles/one.txt",'r')

pattern = re.compile(r"(404|500|200)")

for line in file:
    result = pattern.findall(line)
    print result,