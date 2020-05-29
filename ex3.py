# Ex6
# Ask the user for a string and print out whether this string is a palindrome
# or not. (A palindrome is a string that reads the same forwards and backwards.)

# word = input("Your word to check:")
#
# def is_palindrome(word):
#     print(len(word))

#list
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

#tuple
perfect_squares = (1, 4, 9, 16, 25, 36, 49)


import logging

# print(dir(logging))
# print(help(logging))


# path = "C:\\Users\\Anna\\Desktop\\python\\google_stock_data.csv"
# lines = [line for line in open(path)]
# print(lines[0].strip())
# print(lines[0].strip().split(','))
# print(lines[1])
#
# dataset = [line.strip().split(',') for line in open(path)]
# print(dataset[0])

import datetime

class User:
    """
    A member of blablabla
    """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        # Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """
        Return the age
        """
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return(age_in_years)



user = User("Dave Bowman", "19711223")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

print(user.age())