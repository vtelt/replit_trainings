#functions training

def hello(name):
  print(f"Hello {name}!")

hello("Vicky")

def add_numbers(num1, num2):
  print(num1+num2)

add_numbers(4,8)

def double(number):
  return number*2

new_number = double(3)
print(new_number)

def uppercase(text):
  return text.upper()

print(uppercase("nick"))

names = ["vick", "Jane", "Lily"]

for name in names:
  print(uppercase(name))

#input

user_text = input('Enter some text: ')

upper_or_lower = input('Enter 1 to uppercase or 2 to lowercase: ')
if upper_or_lower == "1":
  print(user_text.upper())
else:
  print(user_text.lower())


#print(user_text.upper())

user_number = input("Enter a number you want to double: ")

print(int(user_number)*2)

