""" 
https://www.hackerrank.com/challenges/string-validators/forum/comments/83656
First version (most Compact)

# uses all five string methods on each character in input string
# prints True if at least one character made the method return True
print "\n".join([str(i) for i in (any(i) for i in (list(zip(*[[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in raw_input()]))))])



Second Version (more readable)

# user input
s = raw_input()

# uses all 5 methods on each character and creates a list for each,
# containing the results of each method used on the character.
newList = [[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]

# rotates lists clockwise to get lists of each method instead
rotated = list(zip(*newList))

# prints whether or not a True is present for each List
print "\n".join([str(i) for i in (any(i) for i in rotated)])




