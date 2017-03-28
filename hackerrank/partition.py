#!/bin/python
def partition(ar):    
    pivot = ar[0]
    left = []
    right = []
    equal = []
    for x in ar:
        if x < pivot:
            left.append(x)
        if x > pivot:
            right.append(x)
        if x == pivot:
            equal.append(x)
    print " ".join(str(x) for x in left) + " " + " ".join(str(x) for x in equal) + " " + " ".join(str(x) for x in right)
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

