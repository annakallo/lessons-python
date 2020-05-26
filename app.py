

# Create a program that asks the user to enter their name and their age. Print out a message
# addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing
# out that many copies of the previous message. (Hint: order of operations exists in Python)
#
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

x = input("Please enter your name:")
y = int(input("How old are you?"))
z = input("When is your birthday?")
copy_number = int(input("Tell me a number:"))

now = datetime.datetime.today()
birth_day = datetime.datetime.strptime(z, "%m/%d").day
birth_month = datetime.datetime.strptime(z, "%m/%d").month

if birth_month == now.month and birth_day < now.day:
    birth_year = now.year - y
elif birth_month == now.month and birth_day > now.day:
    birth_year = now.year - y - 1
elif birth_month == now.month and birth_day == now.day:
    birth_year = now.year - y
    print("happy birthday!")
elif birth_month < now.month:
    birth_year = now.year - y
else:
    birth_year = now.year - y - 1

message = ""
while copy_number > 0:
    message = message + x + " you will turn 100 year old in " + str(birth_year + 100) + "; \n"
    copy_number = copy_number - 1

print(message)

