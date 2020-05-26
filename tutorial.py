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

# Associative array - map - in Python dictionary
#used when you have key/value pairs of data - an input which is mapped
to an output
