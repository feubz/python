#!/usr/local/bin/python3
from sys import argv

def find_mind(*args):
	print(min(*args))
	return min(*args)
	
print(find_mind(5,3,4,1) + 2)