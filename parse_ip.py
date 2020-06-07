import sys
import os

filepath = 'log'
lis = []
with open(filepath) as fp:
	for line in fp:
		var = line.split()
		#print(var)

		if(var!=[] and var[-1][0:3]=='192'):
			print(var[-1])
			lis.append(var[-1])

print(len(lis))