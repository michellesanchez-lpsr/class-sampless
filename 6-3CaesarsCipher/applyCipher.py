# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher
# 
# Author: mflax [at] leadps.org
#
#
# makes a mapping of encoded alphabet to decoded alphabet
#
# arguments: key
# returns: dictionary of mapped letters

import string 

def createDictionary(key):
	up = string.ascii_uppercase
	low = string.ascii_lowercase
	alphaDict = {}
	count = 0 
	for letter in up:
		alphaDict[letter] = up[(key + count) % 26]		
		count = count + 1
	for letter in low: 
		alphaDict[letter] = low[(key + count) % 26]
		count = count + 1
	return alphaDict 
	
#gets the encrypted message from user
# arguments: 
#returns: encoded msg
def getMessage(message):
	return message

# for each letter in the message, decodes and records &  records the decoded letter
# arguments: encoded message and dictionary
# return: decoded message
def decodeMessage(message, dictionary):
	newMsg = ''
	for k in message:
		eachL = dictionary[k]
		newMsg = newMsg + eachL				
	return newMsg

# outputs the message to the terminal
#a\rguments: decoded message
# returns:
def printMessage(decodedMessage):
	print(decodedMessage)


# where the execution starts
try:

# ask the user for key
	print("What key would you like to decode?")
	key = int(raw_input())
	
	dictionary = createDictionary(key)
	
	print("What message would you like to decode?")
	message = raw_input()

# saves message
	encodedMessage = getMessage(message)
	
# decodes message
	decodeMessage = decodeMessage(encodedMessage, dictionary)
	print("Here's the decoding of your message:")
	printMessage(decodeMessage)

except:
	print("Sorry, this code cannot be accepted.")
