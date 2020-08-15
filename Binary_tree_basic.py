
# coding: utf-8

# In[22]:


class Person:
    
    def __init__(self):
        self.name=''
        self.age=0
        self.salary=0
        
    def Pay(self):      
        self.salary+=100
        return self.salary
    
    def Cut(self,x):
        self.salary-=x
        return self.salary
    
person1= Person()
person1.name='Birendra'
person1.salary=100

print(person1.Pay())
print (person1.Cut(30))


# In[20]:


class Node():
    
    def __init__(self,key):
        self.left=None
        self.right=None 
        self.val=key
    
    #def add_right(self):
        #if self.next=None:
            #self.right=self.next    
        
    #def add_left(self):
        #if self.left=None:
            #self.left=self.next
            
    def size(self):
        if self.val is None:
            return 0
        else:
            return (1+size(self.left)+size(self.right))
        
        
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)
print(root.size())



        
        


# In[19]:


# Python Program to find the X of binary tree 

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Computes the number of nodes in tree 
def X(node): 
	if node is None: 
		return 0
	else: 
		return (X(node.left)+ 1 + X(node.right)) 


# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print ((X(root)))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

