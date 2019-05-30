import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt
from numpy import linalg as la
import time
# the following data points we are creating are centered around centre1, centre2 and centre3
# centre1 = np.array([1,1])
# centre2 = np.array([5,5])
# centre3 = np.array([8,2])
# data_1 = np.random.randn(200,2) + centre1
# data_2 = np.random.randn(200,2) + centre2
# data_3 = np.random.randn(200,2) + centre3
#
# values = np.concatenate((data_1, data_2, data_3), axis = 0)

# the following line can be used to create data points if we want truly random set of points
values=np.random.randn(10000,5)

n = values.shape[0]
f = values.shape[1]
cum_sum=np.zeros(n)

map=np.zeros((19,2))
# you can set any k, I'm using 3 as we centred our data around 3 points
k=3
D=0
for k in range(2,21):
    start=time.time()
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
# avg=np.zeros((5,2))

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
    end=time.time()
    # plt.scatter(k,end-start,c='black')
    # avg[D,0]=D+1
    # avg[D,1]=np.sum(c-prev_c)/k
    map[D,0]=k
    map[D,1]=end-start
    D=D+1

# the following code is for plotting our data, the centroids are marked with '*'
# plt.ylim(0,5)
plt.xlim(2,20)
# plt.plot(avg[:,1],avg[:,0])
# plt.plot(map[:,0],map[:,1])
plt.xlabel("k")
plt.ylabel("running time")
plt.plot(map[:,0],map[:,1])
plt.show()
# you can see that the values printed from the next line are very close to the points we centred our data around
