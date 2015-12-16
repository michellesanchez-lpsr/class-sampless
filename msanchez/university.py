# print statements
print(" How many miles away do you live from richmond state?")
miles = raw_input()
miles = int(miles)

#if else and print statements
if miles <=30:
	print("You need atleast 2.5 gpa to get in")
else:
	print("You need atleast 2.0 gpa to get in")

print(" What is your gpa?")
gpa = float(raw_input())
gpa = int(gpa)

if miles <=30 <= 2.0:

	print("Great you have been accepted")
else:
	print("What is your act score?")
	act = (input())
	act = int(act)
	if miles >30 and gpa >= 2.5 and act >=18:
		print("Sorry you need all 3 to get in")
	else:
		print("Accepted")


	
