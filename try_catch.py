#!/bin/python

S = raw_input().strip()
try:
    i = int(S) # python will error if it can make the specified conversion
    print i
except Exception as msg: # msg holds the exception description
    #e = sys.exc_info()[0] # Gets the first line of the error message, may have to 'import sys'
    #write_to_page( "<p>Error: %s</p>" % e )
    print "Bad String"

"""
import math
#Write your code here
class Calculator:
    def power(self,n,p):       
        if any((n < 0, p < 0)):
            raise ValueError('n and p should be non-negative')
        return int(math.pow(n,p))
       
myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e               
"""
