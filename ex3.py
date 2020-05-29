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

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\\Anna\\Desktop\\python\\history.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

# Test the logger
logger.info("Our second log")

# Test message
logger.debug("This is a harmless debug message.")
logger.info()
