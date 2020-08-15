
# coding: utf-8

# In[8]:


# DP approach
def co_sub_seq(x,y):
    m=len(x)
    n=len(y)
    if m==0:
        return n
    if n==0:
        return m
    t=[[0 for i in range(n)]for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            if x[i]==y[j]:
                t[i][j]=t[i-1][j-1]
            else:
                t[i][j]= 1+min(t[i-1][j],t[i][j-1],t[i-1][j-1])
    print(t)
    return t[m-1][n-1]

x='cat'
y='cut'
co_sub_seq(x,y)

