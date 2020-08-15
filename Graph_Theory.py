
# coding: utf-8

# In[12]:


graph ={ 
1:[3], 
2:[4], 
3:[5], 
4:[1, 4], 
5:[2, 3] 
} 



def bfs(graph,s):
    
    visited=[0]*len(graph)
    q=[]
    q.append(s)
    if visited[s-1]==0:
        visited[s-1]=1
    
    while(q):
        t=q.pop(0)
        print(t)
        for i in graph[s]:
            if visited[i-1]==0:
                visited[i-1]=1
                q.append(i)

#graph['1']
bfs(graph,4)  
        
    
    


# In[13]:


# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# Function to print a BFS of graph 
	def BFS(self, s): 

		# Mark all the vertices as not visited 
		visited = [False] * (len(self.graph)) 

		# Create a queue for BFS 
		queue = [] 

		# Mark the source node as 
		# visited and enqueue it 
		queue.append(s) 
		visited[s] = True

		while queue: 

			# Dequeue a vertex from 
			# queue and print it 
			s = queue.pop(0) 
			print (s, end = " ") 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 
			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True

# Driver code 

# Create a graph given in 
# the above diagram 
graph ={ 
'a':['c'], 
'b':['d'], 
'c':['e'], 
'd':['a', 'd'], 
'e':['b', 'c'] 
} 
g=Graph()
print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS('a') 

# This code is contributed by Neelam Yadav 


# In[3]:


graph ={ 
'a':['c'], 
'b':['d'], 
'c':['e'], 
'd':['a', 'd'], 
'e':['b', 'c'] 
}




def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
print(graph)
bfs_connected_component(graph,'a') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
















# In[2]:


graph ={ 
'a':['c'], 
'b':['d'], 
'c':['e'], 
'd':['a', 'd'], 
'e':['b', 'c'] 
}

def dfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    stack = [start]
 
    # keep looping until there are nodes still to be checked
    while stack:
        # pop shallowest node (first node) from queue
        node = stack.pop(-1)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                stac.append(neighbour)
    return explored
dfs_connected_component(graph,'a') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']

