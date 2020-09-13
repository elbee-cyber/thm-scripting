#!/bin/python

import base64

flag = open("b64.txt","r")
flag = str(flag.readlines())

print("Decoding flag..")
for i in range(0,50):
	flag = base64.b64decode(flag)

print("FLAG DECODED SUCCESSFULLY!")
print(flag[:-1])
