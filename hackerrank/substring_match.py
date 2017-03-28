# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
m = raw_input()
count=0
for i in range(0, len(s)):
    if s[i:i+len(m)] == m:
        count+=1

print count
    
