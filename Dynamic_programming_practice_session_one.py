
# coding: utf-8

# In[2]:


def fib(n):
    if n == 1 or n== 2:
        return (1)
    else:
        return fib(n-1)+ fib(n-2)


# In[3]:


fib(5)


# In[5]:


fib(35)


# In[13]:


def fib(n):
    memo=[0]*(n+1)
    memo[0]=1
    memo[1]=1
    if n ==1 or n ==2:
        return n
    elif memo[n-1]==0 or memo[n-2]==0:
        memo[n-1]=fib(n-1)
        memo[n-2]=fib(n-2)
    memo[n]=memo[n-1]+memo[n-2]
    return memo[n]
        
    
        
    


# In[14]:


fib(5)


# In[55]:


# Fibonacci Series using Dynamic Programming 
def fibonacci(n): 
    
	# Taking 1st two fibonacci nubers as 0 and 1 
	FibArray = [0, 1]
	
	while len(FibArray) < n + 1: 
		FibArray.append(0)
	print(FibArray)
	if n <= 1: 
		return n 
	else: 
		if FibArray[n - 1] == 0: 
			FibArray[n - 1] = fibonacci(n - 1) 

		if FibArray[n - 2] == 0: 
			FibArray[n - 2] = fibonacci(n - 2) 
			
	FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
	return FibArray[n] 
	
print(fibonacci(5)) 


# In[9]:


#Bottom_up_approach

def fib(n):
    if n<0:
        return -1
    f_arr=[0]*(n+1)
    f_arr[0]=0
    f_arr[1]=1 
    for i in range(2,n+1):
        f_arr[i]=f_arr[i-1]+f_arr[i-2]
    return f_arr[n]

fib(35)

