#!/bin/python
def insertionSort(ar):    
    insert_index=-1
    # indexes are 0 based, length is 1 based
    length = len(ar)    
    for i in range(length-1):
        if (insert_index == -1) and (ar[i] > ar[length-1]):            
            insert_index = i 
    if insert_index==-1:
        insert_index=length-1
    #print insert_index    
    arc = ar
    ival = ar[length-1]
    bubble = length - 2

    #for i in range(length-1):
    last_line = False
    while last_line == False:
        arc[bubble+1] = arc[bubble]
        if bubble+1 == insert_index:
            arc[bubble+1] = ival
            last_line = True
        print " ".join(str(x) for x in ar)
        bubble -= 1
        
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
