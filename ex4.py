"""
Ex.4
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that
reads the same forwards and backwards.)
"""
"""
MY SOLUTION
your_string = input('Please enter your word:')
your_string = your_string.replace(" ", "")

p = 0
is_palindrom = True
while p < len(your_string)/2 + 1:
    if your_string[p] != your_string[-p-1]:
        is_palindrom = False
        print('This word is not a palindrom')
        break
    p += 1

if is_palindrom:
    print('This word is palindrom')
 
 
 BETTER SOLUTION: (by using reverse)
 
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")   
    
"""

"""
Let’s say I give you a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list 
in it.
name = [expression for element in list_name if condition]
"""
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
only_even = [x for x in a if x % 2 == 0]

print(only_even)
"""

"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print 
out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

play = True
while play:
player1 = input('Player1 enter your choice:')
player2 = input('Player2 enter your choice:')
if player1 ==

