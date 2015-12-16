# number 1
# ask user their age
# if they are over 18 can’t use swings
# if they are over 5 they can use the baby swings
# if they are over 10 they can use the big swings
# if they aren’t doing between that age then they just push a kid on the swings

print("Hi! How old are you?")
age = int(input())

if age >= 18:
  print("Sorry, you're too old to use the swingset!")
else:
  if age < 5:
    print("Welcome to the park! Use the baby swings.")
  elif age < 10:
    print("Welcome to the park! Use the big swings.")
  else:
    print("Welcome to the park! Push a little kid on the swings.")
