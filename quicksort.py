#!/bin/python
# Note: algorithm is correct but it does not match the output exactly
def quickSort(ar):
    # Left side starts at zero, works up
    # Right side starts at last - 1, works down
    # At the end we swap the pivot at the end with the right most element in the right side    
    # Lists are mutable. 
    # Have this function call another function that takes array, start and end, this is what we will use to recurse
    # Print whole array after each recurse
    left = 0
    #right = last - 1
    last = len(ar)-1 # Switch it to zero index
    #pivot = ar[last]

    quickSortSub(ar,0,last)
    
def quickSortSub(ar,start,end):
    left = start    
    pivot = ar[end]
    for x in range(start,end): # From start to end - 1
        if (ar[x] < pivot):
            swap = ar[left]
            ar[left] = ar[x]
            ar[x] = swap
            left += 1
    # Move pivot value to middle            
    swap = ar[left] 
    ar[left] = ar[end]
    ar[end] = swap
    left -= 1 # adjust so we are talking about just numbers assigned to the left side
    # TODO - print list
    if (end - start > 1):
        print " ".join(str(x) for x in ar)
        #print " ".join(str(x) for x in ar),
        #print "  -> %d %d" % (start, end)
    #print "%d %d" % (start,left)
    if (left > start):
        quickSortSub(ar,start,left)
    if (left + 1 < end ):
        quickSortSub(ar,left+1,end)
    
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
