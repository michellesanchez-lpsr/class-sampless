


# teamManager.py This Class allows you to create your own soccer team
class Player(object):
	def __init__( self, name, age, goals, jersey, position):
		self.name = name
		self.age = age
		self.goals = goals
		self.jersey = jersey
		self.position = position
# here I wrote a function in my player
	def printStats(self):
                print("Name:" + self. name)
                print("age:" + str(self.age))
                print("Goals:" + str(self.goals))
		print("Jersey Number:" + str(self.jersey))
		print("Position:" + self.position)

def saveTeam(list, filename):
	file = open((filename), "a")
	# write to the file
	for b in listt:
		file.write(b.name + " " + str(b.age)+ " " + str(b.goals) + " " + str(b.jersey) + " " + b.position + '\n' )
	# close the file
	file.close()
 

def loadTeam(filename):
	# create an empty list
	myList = []
	# open the file
	f = open('puma.tmd', 'w')
	# split each line and create a file from it (use a loop)
	l = myList.split()
	# split each line into a list of variables
	while ltr != "":
		sSplitter = ltr.split()
		list.append(Player(sSplitter[0], sSplitter[1], sSplitter[2], sSplitter[3], sSplitter[4]))
		ltr = file.readline()
	# close the file
		file.close()	
	return myList





print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or an existing team?")
print("Enter the number of your choice and press enter")
print("(1) Start with a new team")
print("(2) open a file for an existing team")
OneOrTwo = raw_input()

if OneOrTwo == "1" or OneOrTwo == "2"
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension")
	fileName = raw_input()



user_choice = int(raw_input())

if user_choice == 2:
	print("What's the filername for your existing team? Enter the whole name, inclusing its .tmd extension.")
	filename = raw_input()
	my_player = loadTeam(filername)
else:
	my_players = []	

	
def saveTeam(playerlist, filename):
	pass


# make your list of players
myPlayers = [] 
print("(1) add player")
print("(2) to see the list of players.")
print("(3) print average number of goals for all players")
print("(4) save your player lis to a file")
print("(0) Leave the program")
# write a function that lets the user add players
choice = raw_input()
c  = 0 
while choice != "0":
	if choice == "1":
# lets the user create a player for the players name
		print("Enter Name:")
		name = raw_input()
# for players age
		print("Enter Age:")
		age = raw_input()
# for goals made
		print("Enter Goals:")
		goals = raw_input()
		c = c + 1
# for jersey number
		print("Enter your Jersey number:")
		jersey = raw_input()
# for position
		print("Enter your Position:")
		position = raw_input()
		
		myPlayers.append(Player( name, age, goals, jersey, position))
		print("You have just added a player to the list")
		print("(1) add player")
		print("(2) to see list of players")
		print("(3) Print average number of goals for all players")
		print("(4) Save your player list to a file")
		print("(0) to exit program")
		choice = raw_input()
	elif choice == "2":
		for p in myPlayers:
			print(" ")
			p.printStats()
			print(" ")
		print("(1) add player")
		print("(2) see list of players")
		print("(3) Print average number of goals for all players")
		print("(4) save your player list to a file")
		print("(0) to exit program")

		choice = raw_input() 
myPlayers.append(Player(name, age, goals, jersey, position))
