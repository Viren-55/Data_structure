
# coding: utf-8

# In[19]:


#DP_approach

def co_sub_seq(x,y):
    m=len(x)
    n=len(y)
    
    t=[[0 for i in range(n)]for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            if x[i]==y[j]:
                t[i][j]= 1+ t[i-1][j-1]
            else:
                t[i][j]= max(t[i-1][j],t[i][j-1])
    print(t)
    return t[m-1][n-1]
    
co_sub_seq('abcdef','acef')


# In[35]:


#Recursion_way
def co_sub_seq(x,y):
    m=len(x)
    n=len(y)
    if m==0 or n==0:
        return 0
    if x[m-1]==y[n-1]:
        return 1+co_sub_seq(x[:m-1],y[:n-1])
    else:
        return max(co_sub_seq(x[:m-1],y[:n]),co_sub_seq(x[:m],y[:n-1]))
    
co_sub_seq('abc','abc')
    


# In[33]:


x='abc'
y='ab'

m=len(x)
n=len(y)
x[:m-1]


