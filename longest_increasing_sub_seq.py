
# coding: utf-8

# In[2]:


#Using_DP_

def LIS(arr):
    t=len(arr)
    lis=[1]*(t)   
    for i in range(1,t):
        for j in range(0,i):
            if arr[i]>arr[j] and lis[i]< lis[j]+1:
                lis[i]=lis[j]+1
    return max(lis)
            
arr = [10, 22, 9, 33, 21, 50, 41, 60]   
LIS(arr)

