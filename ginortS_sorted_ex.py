# Enter your code here. Read input from STDIN. Print output to STDOUT
import string # Needed for method 2
inp=raw_input()

# Method 1
#order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
# Method 2
order= string.ascii_letters + '1357902468'
print reduce(lambda x,y: x+y, sorted(inp, key=order.index))
# Method 3 - has an issue?
#lambda c: (c.isdigit() - c.islower(), c in '02468', c)
# Method 4 - also has an issue
#key=lambda c: (-ord(c) >> 5, c in '02468', c)
