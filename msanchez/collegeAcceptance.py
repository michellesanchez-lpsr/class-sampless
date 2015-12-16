print("How old are you?")
age= int(raw_input())

print("What is your gpa?")
GPA = float(raw_input())

# if GPA is over 3.0 and age is over 16, accept
if GPA > 3.0 and age > 16:
	print("Congrats, you're been accepted to Columbia!")
else:
	print("Sorry, guess you'll have to go to Harvard instead.")
