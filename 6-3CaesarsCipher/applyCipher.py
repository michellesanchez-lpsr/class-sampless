
# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesars Cipher
# 
# Author: rc.sanchez.michelle [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
print("Welcome to Contacts!!")

# empty list so you can add to it
contacts = {}
choice = 1
# loops for caesar's cypher
while choice != 0:
	print("What would you like to do?")
	print("1). Add a phone number.")
	print("2). Print the full list of contacts.")
	print("3). Enter a name to retrieve that contact's phone number.")
	print("4). Remove a contact.")
	print("5). Change the number of a contact.")
	print("0). Exit the Contacts app.")	
	choice = int(raw_input())
# This starts the if choices/options for each and every one of the options that there is	
	# This adds the name and number if choice entered equalls 1
	if choice == 1:
		print("What's the name of your contact?")
		name = raw_input()
		print("What's the number of your contact?")
		num = raw_input()
		contacts[name] = num
	# This prints all the contacts if choice is 2
	if choice == 2:
		print(contacts)
	
	#This will retrieve a certain number if choice is 3
	if choice == 3:
		print("Who's number would you like?")
		name = raw_input()
		print("OK, here's the number:")
		# calls for specific contact
		print(contacts[name])

	# this deletes a number if choice is 4
	if choice == 4:
		print("Who's number would you like to delete?")
		name = raw_input()
		print("OK, number has been deleted.")
		# deletes a number
		del contacts[name]

	# will change a number if choice entered is 5
	if choice == 5:
		print("Who's number would you like to change?")
		name = raw_input()
		print("Please enter new number:")
		num = raw_input()
		# changes 
		contacts[name] = num
		print("Number has been updated.")

	# the end of the program
