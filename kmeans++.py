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
# values=np.random.randn(303,2)

n = values.shape[0]
f = values.shape[1]
cum_sum=np.zeros(n)
# you can set any k, I'm using 3 as we centred our data around 3 points
k=3
# c is our set of centroids
c=np.zeros((k,f))
prev_c=np.zeros((k,f))
c[0,:]=values[3,:]
# function to calculate eucildean distance between two point
def distance(x,y):
    a=la.norm(np.subtract(x,y))
    return a
# min_dist finds the distance between the given point x and the centre which is closest to it
def min_dist(x,c):
    min=distance(c[0,:],x)
    for count,ele in enumerate(c):
        d=distance(x,ele)
        if d<min :
            min=d
    return min
# the following code is to assign centres
for x in range(1,k):
#     cum_sum holds the cumulative sum of the squares of D where D= distance between  the point and its closest centre

    prev=0
    for i in range(n):
        cum_sum[i]=np.square(min_dist(values[i,:],c)) + prev
        prev=cum_sum[i]

    total=prev
#     with the next step, we make sure cum_sum holds only values from 0 to 1
    cum_sum = cum_sum/total
# "random" is a random number between 0 and 1
    random = np.random.random()
    for i in range(n):
        if cum_sum[i]>random:
            c[x,:]=values[i,:]
            break
# the centres initialised with the kmeans++ method are plotted in green
plt.scatter(c[:,0], c[:,1],marker='*', c='green', s=150)
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
plt.scatter(values[:,0],values[:,1],c='yellow',s=20)
plt.scatter(c[:,0], c[:,1],marker='*', c='orange', s=150)
plt.show()

