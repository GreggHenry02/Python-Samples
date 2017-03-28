class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    """ Some one else's example
    def insert(self,head,data): 
        if head == None:
            self.head = Node(data)
        else:         
            n = self.head
            while n.next != None:
                n = n.next
            n.next = Node(data)
        return self.head   
    """
        
    def insert(self,head,data): 
    #Complete this method            
        if (head == None):
            self.head=Node(data)            
        else:
            current = self.head
            while current.next != None:
                #print current.data
                current = current.next
            current.next = Node(data)
        return self.head			

mylist= Solution()
T=int(input())
head=None
for i in range(T):
	data=int(input())
	head=mylist.insert(head,data)    
	mylist.display(head);	
