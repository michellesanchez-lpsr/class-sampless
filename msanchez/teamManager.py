# teamManager.py
# This Class allows you to create your own soccer team
class Player(object):  
	def __init__( self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals

# here I wrote a function in my player
	def printStats(self):
                print("Name:" + self. name)
                print("age:" + self.age)
                print("Goals:" + self.goals)

# make your list of players
myPlayers = []
print("To add players press 1. To see list of players press 2.")

# write a function that lets the user add players
choice = raw_input()

c = 0
while choice != "0":
	if choice == "1":
# lets the user create a player
# for the players name
		print("Enter Name:")
		name = raw_input()
# for players age
		print("Enter Age:")
		age = raw_input()
# for goals made
		print("Enter Goals:")
		goals = raw_input()
		c = c + 1
		myPlayers.append(Player(name, age, goals))
		print("You have just added a player to the list")
		print("To add players press 1. To see list of players press 2.")
		choice = raw_input()
	elif choice == "2":
		for p in myPlayers:
			print(" ")	
			p.printStats()
			print(" ")
		print("To add players press 1. To see list of players press 2.")
		choice = raw_input()
myPlayers.append(Player(name, age, goals))











