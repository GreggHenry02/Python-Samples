import sys
import string
import re
import math


if len(sys.argv) == 1:
	print " #Successes, #Trials, #Probability of Success"
	print " #Successes - an integer or the letter X"

#print sys.argv[1]
#print sys.argv[2]
#print sys.argv[3]

if sys.argv[1].isdigit():
	r = int(sys.argv[1])
elif sys.argv[1].upper() == "X":
	r = sys.argv[1].upper()
else:
	print "invalid success number"
	sys.exit(0);

if sys.argv[2].isdigit():
	n = int(sys.argv[2])

if n < r and isinstance(r,int):
	print "More Successes than Trials, invalid numbers"
	sys.exit(0);

try:
	if '/' in sys.argv[3]:
		Ps=float(sys.argv[3].split('/')[0]) / float(sys.argv[3].split('/')[1])
	elif '\\' in sys.argv[3]:
		Ps=float(sys.argv[3].split('\\')[0]) / float(sys.argv[3].split('\\')[1])
	elif '.' in sys.argv[3]:
		Ps=float(sys.argv[3])
except ValueError:
	print "Invalid Probability given"

if Ps > 1.0 or Ps < 0.0:
	print "Invalid Probability given"
	sys.exit(0);
Pf = 1 - Ps

#r = int(sys.argv
#n = 

#C(n,r) = n! / ( r!(n - r)! )
#C = math.factorial(n) / (math.factorial(r)*math.factorial(n-r))
#print "%s Combinations, Ps=%s, Pf=%s" % (C,Ps,Pf)
bernoulli={}

Ptotal=0.0
Pless=0.0
Plessequal=0.0
Pequal=0.0
Pgreater=0.0
Pgreaterequal=0.0
for i in range(0,n+1):
	C = math.factorial(n) / (math.factorial(i)*math.factorial(n-i))
	bernoulli[i]=C*math.pow(Ps,i)*math.pow(Pf,n-i)
	#print "%s Combinations, Ps=%s, Pf=%s" % (C,Ps,Pf)
	#bern=C*math.pow(Ps,i)*math.pow(Pf,n-i)
	print "C(%d,%d) %f" % (n,i,bernoulli[i]),
	Ptotal += bernoulli[i]
	if isinstance(r,int):
		print
		if i <  r: Pless += bernoulli[i]
		if i <= r: Plessequal += bernoulli[i]
		if i == r: Pequal += bernoulli[i]
		if i >  r: Pgreater += bernoulli[i]
		if i >= r: Pgreaterequal += bernoulli[i]
	elif r=="X":
		Pequal += bernoulli[i]
		print "  Pi = %f   Pd = %f" % (Pequal,1.0-Pequal)

#print "-----"
#print Ptotal
print

if isinstance(r,int):
	print "The probability of:"
	print "Having less than       %d successes: %f" % (r,Pless)
	print "Having less than or    %d successes: %f" % (r,Plessequal)
	print "Having exactly         %d successes: %f" % (r,Pequal)
	print "Having greater than    %d successes: %f" % (r,Pgreater)
	print "Having greater than or %d successes: %f" % (r,Pgreaterequal)
