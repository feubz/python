from random import randint
numbers = randint(1,6)
choice = 0
while True:
	try:
		choice = int(raw_input("What is your guess? : "))
	except ValueError:
			print("Oopps, this is not a number")
	if choice == numbers:
		print ("You won")
		break