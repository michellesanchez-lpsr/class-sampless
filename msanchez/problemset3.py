print("Welcome to PumaPix!")
print("Enter your 5 favorite TV shows.")

usersList = []

i = 0

while i <5:
	print("Enter a show name:")
	x = raw_input()
	i = i + 1
	usersList.append(x)
	
print("Ok, here's what you entered:")
print(usersList)
print(" We've added a couple of important ones. ")
usersList.append("CSI")
usersList.append("Breaking Bad")

for c in usersList:
	print(c)
