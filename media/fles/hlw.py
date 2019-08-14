#! /usr/bin/python3

employers = open("employ.txt","a")
employers.write("linkon")
employers = open("employ.txt","r")
print(employers.readlines()[1])
employers= open("employ.txt","r")
for emp in employers.readlines():
	print(emp)
employers.close()
