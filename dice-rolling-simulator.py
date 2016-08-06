from random import randint
while True:
	print(randint(1,6))
	choice = raw_input("Do you want to continue? : ")
	if choice not in ('yes','y','YES'):
		break