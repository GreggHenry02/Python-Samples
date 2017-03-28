# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
line=raw_input()
strings=line.split()
numbers=map(int,strings)

condition=True
palindrome=False
for x in numbers:
    if x <= 0:
        condition=False
if condition==True:
    for s in strings:
        if s == s[::-1]:
            palindrome=True
            
if all((condition,palindrome)):
    print "True"
else:
    print "False"

"""
How to do the above in three lines
N = int(input())
input_list = list(map(int, input().split()))
print(any(all(x > 0 for x in input_list) and str(x)[::-1] == str(x) for x in input_list))
"""
