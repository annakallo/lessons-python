print("Hello World")

# VARIABLES
# DATA TYPES - string, numbers, Boolean

# character_name = "Tom"
# character_age = 50.895
# is_male = True
# is_female = False


# WORKING WITH STRINGS

newline: "\n"
quotation mark: "\""
concatenation: "" + ""

#FUNCTIONS
phrase = "Giraffe Academy"

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())     - checkes if it entirely uppercase
print(len(phrase))          - shows the length
print(phrase[0])            - first character
print(phrase.index("a"))    - index function
print(phrase.replace("Giraffe", "elefant"))     - replace a part

# NUMBERS
#int, floats e = 2.7..., complex numbers j
10 % 3                      - modulus operation
16//5  result 3
print(str(my_num))          - transfroming into string

# FUNCTIONS
print(abs(my_num))          - absolute value
print(pow(3,2))             - hatvany (3*3)
print(max(3,2))

#help
print(dir())
print(dir(__builtins__))
help(pow)

#Booleans
bool(0) --> False
every other number is True
bool(" ") --> True
bool("")   --> False
trivial     --> False
non-trivial --> True
int(True)  --> 1
int(False)  --> 0

# Dates and Times

import datetime
print(dir(datetime))
print(help('datetime'))

gvr = datetime.date(1956, 1, 31)

now = datetime.datetime.today()
print(now)

# Functions

def ping():
    return "Ping!"
print(ping())

2 types of Arguments:
- Keyword (if it has an =) - this arguments must come last
- Required
"""Adds up a number""" - its called a docstring - its like a comment

def g(y, x = 0):
    """Adds up a number"""
    return x + y

g(5)
g(7, x = 3)

# SETS
example = set()

example = set()
example.add(42)
example.add(3.14)
example.add(True)


print(example)
#it has elements, the order does not matter, no duplicates are allowed
print(len(example))
example.remove(42)  - it gives an error if you try to remove something which
is not in the set
example.discard(42) - gives no error
ex2 = set([28,True, "Helium"])
ex2.clear() - to clear all elements

odds = set([1, 3, 5, 7, 9])
even = set([2, 4  6, 8, 10])
primes = set([2, 3, 5, 7])

odds.union(evens)
evens.union(odds)
odds.intersection(primes)
2 in primes   - testing if 2 is in the set of the primes
print(2 not in primes)

# LISTS - here order matters (its like an array)
ex = list()
ex = []
primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes[0]
the last item is primes[-1]
primes[2:5]     - slicing includes the begining but not the end
numbers + letters  - concatenation


#DICTIONARIES
# Associative array - map - in Python dictionary
#used when you have key/value pairs of data - an input which is mapped
#to an output

# FriendFace post
# user_id = 209
# message = "D5 E5"
# language = "English"
# datetime = "202597863"
# location = (44.590533, -104.715556)

post = {"user_id":209, "message":"D5 E5", "language":"English", "datetime":"202597863",
"location":(44.590533, -104.715556)}

#"keys":"values"
print(type(post))
# class 'dict'

post2 = dict(message = "SS Cotopaxi", language = "English")
print(post2)

# print(post["user_id"])
# print(post["datetime"])
post2["user_id"] = 209
post2["datetime"] = "687884126"

print(post2)

if 'location' in post2:
    print(post2['location'])
else:
    print('no location')


#other possible way to handle if it doesnt exist
try:
    print(post2['location'])
except KeyError:
    print('well well well')

#other possible way to handle if it doesnt exist
loc = post2.get('location', None)
print(loc)

# a way to iterate through the dict
for key in post.keys():
    value = post[key]
    print(key, "=", value)


# other way to iterate through the dict
for key, value in post.items():
    print(key, '=', value)

# to remove data
post2.pop('message')
print(post2.pop('message')) # it deletes the key and returns the value of it
# deletes the last one
post2.popitem()
print(post2.popitem()) # it also returns the key + value


#TUPLES
#list
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

#tuple
perfect_squares = (1, 4, 9, 16, 25, 36, 49)

#same things
len(perfect_squares)

for p in perfect_squares:
    print(p)

# differences
# lists have more functionalities so they occupy more space then tuples

list_eg = [1, 2, 3, 4, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, 4, "a", "b", "c", True, 3.14159)

print(sys.getsizeof(list_eg))
#72
print(sys.getsizeof(tuple_eg))
#64

# in lists you can add, remove, change data, unlike in tuples
'immutable'

empty_tuple = ()
test1 = ("a",) # without the comma its just a string

# Alternative Construction of Tuples
test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3

# (age, country, knows_python)
survey = (27, "vietnam", True)

age = survey[0]
country = survey[1]

print('Age = ', age)

#works the same way:
survey2 = (21, "USA", False)
age, country, knows_python = survey2

print('Age = ', age)

# Logging
# Purpose: Record progress and problems..
# Levels: Debug, Info, Warning, Error, Critical
# Constants are all MAJUS, classes are Capitalized,
# methods are starting in lowercase

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
logger.info("just some info")
logger.warning("i cant do that")
logger.error("come on...")
logger.critical("the internet is down...")

# CSV DATA

path = "C:\\Users\\Anna\\Desktop\\python\\google_stock_data.csv"
lines = [line for line in open(path)]

print(lines[0].strip()) # the strip removes any leading or trailing empty space
print(lines[1])

print(lines[0].strip().split(',')) # dividing the string in smaller pieces,
# particioning with this character ','

#better like this
dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])

#using csv module
path = "C:\\Users\\Anna\\Desktop\\python\\google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # the first line is the header
data = [row for row in reader] # Read the remaining data
print(header)
print(data[0])

# LIST COMPREHENSTION
list = [1, 2, 3]
list2 = [4*x for x in list]
name = [expression for element in list_name if condition]

# CLASSES
# Capitalize all the words in the name of a class
class User:
    pass

user1 = User() # user1 is an "instance " or "object" of User
user1.first_name = "Dave"
user1.last_name = "Bowman" # a data attached to an object is a field

print(user1.first_name)
print(user1.last_name) # fields are lowercase, separated by underline

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"
print(user2.first_name, user2.last_name )

user1.age = 37
user.fav_book = "2001: A Space Odyssey"
# a function inside a class is a method
# init method = short for initialization aka Constructor



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