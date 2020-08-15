
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt 

# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 

# plotting the points 
for i in range(10):
    for j in range(3):
        x[j]=x[j]+1
        y[j]=y[j]+1
    plt.plot(x, y) 

# naming the x axis 
    plt.xlabel('x - axis') 
# naming the y axis 
    plt.ylabel('y - axis') 

# giving a title to my graph 
    plt.title('My first graph!') 

# function to show the plot 
plt.show() 


# In[9]:


import matplotlib.pyplot as plt
import time
import random
 
ysample = random.sample(range(-50, 50), 100)
 
xdata = []
ydata = []
 
#plt.show()
 
axes = plt.gca()
axes.set_xlim(0, 100)
axes.set_ylim(-50, +50)
line, = axes.plot(xdata, ydata, 'r-')
 
for i in range(100):
    xdata.append(i)
    ydata.append(ysample[i])
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.1)
 
# add this if you don't want the window to disappear at the end
    #plt.show()


# In[10]:


import matplotlib.pyplot as plt
# generate axes object
ax = plt.axes()

# set limits
plt.xlim(0,10) 
plt.ylim(0,10)

for i in range(10):        
     # add something to axes    
    ax.scatter([i], [i]) 
    ax.plot([i], [i+1], 'rx')

     # draw the plot
    plt.draw() 
    plt.pause(0.01) #is necessary for the plot to update for some reason

     # start removing points if you don't want all shown
    if i>2:
        ax.lines[0].remove()

