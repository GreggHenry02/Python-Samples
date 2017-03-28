import string

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input().strip().replace(" ","") # Strip removes extraneous whitespace, Replace deletes spaces
sset = list(set(s.lower())) # Turns lower case string into a set for uniqueness then back into a sortable list
sset.sort()
if "".join(sset) == string.ascii_lowercase:
    print "pangram"
else:
    print "not pangram"
