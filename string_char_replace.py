# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
l = raw_input().split()
print s[:int(l[0])] + l[1] + s[int(l[0])+1:]
