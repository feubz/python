#!/usr/local/bin/python3
class fruit():
	
	def __init__(self, name, color):
		self.name = name
		self.color = color
		fruit.whoami = "fruit"
	



	def print(self):
		print("Hey I'm a {} and my color is {} ".format(self.name,self.color))