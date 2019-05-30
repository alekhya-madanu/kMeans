from random import *
import random
import math
def euclidean0_1(vector1, vector2):
    '''calculate the euclidean distance, no numpy
    input: numpy.arrays or lists
    return: euclidean distance
    '''
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))

    return dist

def centroid(multi_arr1,multi_arr2,clust_num,col_num):
        res_list1 = [0 for i in range(col_num)]
	res_list=[]
	for j in range(clust_num):
		res_list.append([])
        for row in range(clust_num) :
                res_list1 = [0 for i in range(col_num)]
        	for col in range(len(multi_arr2[row])) :
                        ele = multi_arr2[row][col]

                        res_list1 = [sum(j) for j in zip(res_list1, multi_arr1[ele])]
                res_list1 = [x / len(multi_arr2[row]) for x in res_list1]
                for i in range(col_num):
                	res_list[row].append(res_list1[i])


        return res_list


row_num = int(input("Input number of rows: "))#n
col_num = int(input("Input number of columns: "))# d
clust_num = int(input("Input number of clusterss: "))#k
multi_list1 = [[randint(1,1000) for col in range(col_num)] for row in range(row_num)]
print(multi_list1)# contains points

choices = list(range(row_num-1))
random.shuffle(choices)








cluster_list=[]
#[[-1 for col in range(row_num)] for row in range(clust_num)]#[-1 for col in range(clust_num)]

for j in range(clust_num):
	cluster_list.append([])


#used to randomly allot representatives(centroids)
mean_arr = [choices.pop() for i in range(clust_num)]
print(mean_arr)

multi_list2 = [[0 for col in range(col_num)] for row in range(clust_num)]# (centroids)representatives of respective clusters
for row in range(clust_num):
    i = mean_arr.pop()
    for col in range(col_num):
        multi_list2[row][col]= multi_list1[i][col]

print(multi_list2)
dist2 = 2
count = 0
while dist2 != 0  and count<9999 :
        count = count+1
	for row in range(row_num):

		vector1 = multi_list1[row]
		min_dist = 9999999999999999999999999999999
		index = -1
        	for num in range(clust_num):
                		vector2 = multi_list2[num]
                        	dist = euclidean0_1(vector1, vector2)
                        	if min_dist > dist  :
                        		min_dist = dist
                        		index = num

                cluster_list[index].append(row)




	dist2 = 0
	multi_list3 = centroid(multi_list1,cluster_list,clust_num,col_num)


	for row in range(clust_num):
        	vector1 = multi_list2[row]
        	vector2 = multi_list3[row]
		dist2 = dist2 + euclidean0_1(multi_list2[row],multi_list3[row])
        multi_list2 = multi_list3

print(multi_list3)
