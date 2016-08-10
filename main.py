#!/usr/local/bin/python3
from myclass import fruit

fruit1 = fruit("apple","red")
fruit2 = fruit("banana","yellow")
fruit1.print()
fruit2.print()
print("That class represent: A {}".format(fruit.whoami))

