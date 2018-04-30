from random import *

def monty():
	goal = randint(0, 2) #Choose the door
	print goal+1
	doors = [True, True, True]
	#Assign values to the doors
	for i in range(0,3):
		if i == goal:
			doors[i] = True
		else:
			doors[i] = False

	choice = getChoice();
	#if user enters invalid door number
	if(choice == -1):
		print "Sorry, that isn't a valid door, the prize was in door %s" % (goal+1)
		return

	print "You chose door %s, for fun, lets open another door" % (choice+1)

	reveal = randint(0,2)
	while(reveal == choice) or (reveal == goal):
		reveal = randint(0,2)

	print "Door %d has nothing behind it. Now you have the oppurtunity to switch doors" % (reveal+1)
	switch = switchChoice()

	if(switch == 'n'):
		if(goal == choice):
			print "Congrats! You guessed right, the prize was behind door %d" % (goal+1)
		else:
			print "Sorry, the prize was behind door %d, better luck next time" % (goal+1)
	else:
		if(goal != choice):
			print "Congrats! You guessed right, the prize was behind door %d" % (goal+1)
		else:
			print "Sorry, the prize was behind door %d, better luck next time" % (goal+1)


def getChoice():
    choice = input("Choose one of the four doors by entering either 1, 2, or 3 (as an integer): ")
    if(choice == 1):
    	return 0
    elif(choice == 2):
    	return 1
    elif(choice == 3):
    	return 2
    else:
    	return -1



def switchChoice():
	switch = raw_input("Would you like to switch doors?(Y/N): ")
	if(switch == 'Y') or (switch == 'y'):
		return 'y'
	elif(switch == 'N') or (switch == 'n'):
		return 'n'
	else:
		print "You entered an invalid choice, I will take that to mean you don't want to switch"
		return 'n'



monty()
