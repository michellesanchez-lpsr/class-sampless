print("Welcome to Alisons Quest")
print("Enter the name of your character")
name =(raw_input())


print("Enter Strength (1-10)")
strength = int(raw_input())
strength = str(strength)


print("Enter health (1-10)")
health = int(raw_input())
health = str(health)


print("Enter luck (1-10)")
luck = int(raw_input())
luck = str(luck)


if int(health) + int(luck) + int(strength) >15:
# add the statements and if they are bigger than 15 then print 
	print(" You have give your character too many points!")
	print(" Default values have ben assigned, " + name + ": strength - 5, health - 5, luck - 5.")
elif int(health) + int(luck) + int(strength) <=15:
# tell them their health luck and strength
	if int(health) + int(luck) + int(strength) <=15:
		print(" Ok your health is " + health + " and your luck is " + luck + "and  your strength " +strength )
print(" Your character has come to a fork in the road. ")
print(" Do you want to go right or left? Enter 'right' or 'left' . ")

leftOrRight = str(raw_input())


if  leftOrRight == "left":
	print( name + ", you've met your dragon!")
	if int(health) <=5:
		print(" Oh no " + name + "!Your health wasn't high enough to survive its fire breath. You lost the game. ")
if leftOrRight == "left":
	print( name + " , you've met your dragon!")
	if int(health) >=5:
		print( " Yay " + name + " you have won the game. ")

if leftOrRight == "right":
	print( name + " you've come across a hill ")
	if int(strength) <=5:
		print( " Oh no " + name + "!Your strength wasn't high enough to survive going up the hill. You lost:(")
if leftOrRight == "right":
	print( name + " you've come across a hill ")
	if int(strength) >=5:
		print(" Yay " + name + " you have won the game . ")



