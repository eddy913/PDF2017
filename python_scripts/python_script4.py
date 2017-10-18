#!/usr/bin/python3
import sys
num = float(sys.argv[1])
mes1 = "the number is smaller than 0"
mes2 = "the number is larger than 50"
mes3 = "the number is smaller than 50"
mes4 = "And is divisible by 3"
mes5 = "And is even"

if num <0:
  print(mes1)

elif num > 50:
  print(mes2)
  if num%3 == 0:
    print(mes4)

elif num < 50:
  print(mes3)
  if num%2 == 0:
    print(mes5)  
