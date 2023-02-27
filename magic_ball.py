import random

print(random.randint(1, 10))

print(random.random())

#Magic 8 ball that prints yes, no or maybe each time you ask
answer = random.randint(1, 3)

if answer == 1:
  print("Yes")
if answer == 2:
  print("No")
if answer == 3:
  print("Maybe")
