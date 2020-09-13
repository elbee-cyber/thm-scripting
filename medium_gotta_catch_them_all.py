#!/bin/python
import requests
from bs4 import BeautifulSoup
import time

url = "http://10.10.15.91:"

#TRY FOR A START PORT THEN SET NEXT PORT TO STAGE1
print("Waiting for server!")
while True:
	try:
		a=requests.get(url+"1337/")
		print(str(a.text))
		if "2" in str(a.status_code):
			print("SERVER UP!")
		break
	except:
		time.sleep(0.1)

print("Setup complete!")
num = 0.0
first = True
a=requests.get(url+"1337")
prt=""
while prt != "9765":
	if first:
		print("First loop")
		first = False
	else:
		bool = True
		while bool:
			try:
				a=requests.get(url+prt)
				print("Next port.."+str(url+prt))
				if "2" in str(a.status_code):
					bool = False
			except:
				time.sleep(0.1)
				pass
	if "add" in a.text:
		print("Adding..")
		temp = str(a.text)
		stuff=temp.split()
		num = num+float(stuff[1])
		prt = str(stuff[2])
		print("Number: "+str(num)+" Port: "+prt)
	if "minus" in a.text:
		print("Subtracting..")
		temp = str(a.text)
		stuff=temp.split()
		num = num-float(stuff[1])
		prt = str(stuff[2])
		print("Number: "+str(num)+" Port: "+prt)
	if "multiply" in a.text:
		print("Multiplying..")
		temp=str(a.text)
		stuff=temp.split()
		num = num*float(stuff[1])
		prt = str(stuff[2])
		print("Number: "+str(num)+" Port: "+prt)
	if "divide" in a.text:
		print("Dividing..")
		temp=str(a.text)
		stuff=temp.split()
		num=num/float(stuff[1])
		prt=str(stuff[2])
		print("Number: "+str(num)+" Port: "+prt)

		
print("COMPLETED EXPLOIT!")
		
print("KEY IS "+str(num))
time.sleep(1)
print("Process completed!")

