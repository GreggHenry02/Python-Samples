# Student is a list, each entry is a 2 element long list 
# How to sort a list by an element of a sublist
import operator

n=int(raw_input())

students=[]
for i in range(n):
    name = raw_input()
    mark = float(raw_input())
    #print name, mark
    students.append([name,mark])

# sorts students by second element of the sub list
ssort=sorted(students, key=operator.itemgetter(1))





index = 0
lowest = ssort[0][1]
while ssort[index][1] == lowest:
    index+=1
sec_lowest = ssort[index][1]
result=[]
while ssort[index][1] == sec_lowest:    
    result.append(ssort[index][0])
    index +=1
result.sort()
for v in result:
    print v
