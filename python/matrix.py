
#!/usr/bin/python

import re


def matrix(n):
for row in range(1,n+1):
print('\t'.join(str(row*col) for col in range(1,n+1)))


matrix(9)
