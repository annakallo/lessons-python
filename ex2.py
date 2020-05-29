# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
#
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one
# number to divide by (check). If check divides evenly into num, tell that
# to the user. If not, print a different appropriate message.

# num = int(input("Tell me a number:"))
# check = int(input("Is it dividable by:"))
#
# def is_div(num, check):
#     if num % check == 0:
#         return("Number is dividable by " + str(check))
#     else:
#         return("Number is not dividable by " + str(check))
#
# print(is_div(num, check))

# Ex. 3
# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements
# less than 5 from this list in it and print out this new list.
# Write this in one line of Python.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!???????????
# Ask the user for a number and return a list that contains only elements from the original
# list a that are smaller than that number given by the user.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_a = []
# num = int(input("Say a number:"))
#
# for i in a:
#     if i < num:
#         new_a.append(i)
#
# print(new_a)

# Ex4
# Create a program that asks the user for a number and then prints
# out a list of all the divisors of that number. (If you don’t know what
# a divisor is, it is a number that divides evenly into another number.
#     For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# num = int(input("Tell me your number:"))

# def divisors(a):
#     """Will check all divisors"""
#     div = 1
#     div_list = []
#     while div < a:
#         if a % div == 0:
#             div_list.append(div)
#         div = div + 1
#     return div_list
#
# print(divisors(num))

# Ex5
# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program works
# on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this
# point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 11]

# c = set(a)
# d = set(b)
# print(c)
# print(d)
# print(c.intersection(d))

# def intersect(a, b):
#     comparision = []
#     for i in a:
#         for j in b:
#             if i == j:
#                 comparision.append(i)
#     return comparision
#
# def cut_repeat(a):
#     trans = set(a)
#     return list(trans)
#
#
# print(intersect(a, b))
# print(cut_repeat(intersect(a, b)))
# print(type(cut_repeat(intersect(a, b))))

def intersect(a, b):
    comparision = []
    for i in a:
        if i in b and i not in comparision:
            comparision.append(i)
    return comparision

print(intersect(a, b))