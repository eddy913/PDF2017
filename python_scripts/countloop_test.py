#!usr/bin/env python3
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

# print numbers in range based on command line input
# for num in range(a,b+1):
#	print(num)
# print("done")

for num in range(a,b+1):
        if num%2>0:
	print(num)
print("done")
