import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt
from numpy import linalg as la
import time
start=time.time()
# the following data points we are creating are centered around centre1, centre2 and centre3
centre1 = np.array([1,1])
centre2 = np.array([5,5])
centre3 = np.array([8,2])
data_1 = np.random.randn(200,2) + centre1
data_2 = np.random.randn(200,2) + centre2
data_3 = np.random.randn(200,2) + centre3

values = np.concatenate((data_1, data_2, data_3), axis = 0)

# the following line can be used to create data points if we want truly random set of points
# values=np.random.randn(300,2)

n = values.shape[0]
f = values.shape[1]

# you can set any k, I'm using 3 as we centred our data around 3 points
k=3
# c is our set of centroids
c=np.random.randn(k,f)
prev_c=np.zeros((k,f))
# function to calculate eucildean distance between two point
def distance(x,y):
    a=la.norm(np.subtract(x,y))
    return a

dist=np.zeros(k)
classify=np.zeros(n)

error=la.norm(c-prev_c)


while error>0.0001 :
    #the following loop creates a n*1 array which stores the centroid each point is closest to
    for i in range(n):
        for l in range(k):
            dist[l]=distance(values[i,:],c[l,:])
            classify[i]=np.argmin(dist)

    prev_c=c.copy()

    # the following code updates the centroids by taking means of each cluster
    for i in range(k):
        d=0
        a=np.zeros(f)
        for j in range(n):
            if classify[j]==i:
                a=a+values[j,:]
                d=d+1
        c[i,:] =a/d

    error=la.norm(c-prev_c)
# the following code is for plotting our data, the centroids are marked with '*'

# you can see that the values printed from the next line are very close to the points we centred our data around
print(time.time()-start)
