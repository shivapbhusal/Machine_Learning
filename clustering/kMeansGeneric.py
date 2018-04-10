'''
A generic K means clustering algorithm

python kMeansGeneric.py 2 

This will give two clusters

Created By: Shiva Bhusal, BGSU

'''

import sys
import math
import time

def findCenter(cluster):
    x=0
    y=0
    count=0
    for points in cluster:
        x=x+points[0]
        y=y+points[1]
        count=count+1
    if count!=0:
        x=x/count 
        y=y/count 
    return [x,y]

def findDistance(point, center):
    x, y=point
    c1, c2=center
    distance=math.sqrt(pow((x-c1),2)+pow((y-c2),2))
    return distance

def getNearestCluster(point, centers):
    x,y=point
    minDist=findDistance(point, centers[0])
    clusterIndex=0
    for i in range(1,len(centers)):
        tempDist=findDistance(point, centers[i])
        if tempDist<minDist:
            minDist=tempDist
            clusterIndex=i
    return clusterIndex

def kMeans(data, k):
    clusters=[]
    centers=[]

    for i in range(k):
        centers.append(data[i])
        clusters.append([])

    newCenters=[]
    count=0
    while newCenters!=centers:
        newCenters=[]
        for c in centers:
            newCenters.append(c)
        count=count+1
        for point in data:
            j=getNearestCluster(point, centers)
            clusters[j].append(point)

        for i in range(len(clusters)):
            centers[i]=findCenter(clusters[i])

        print(str(count)+" iterations.")
        print(centers)
        print(newCenters)
        #time.sleep(0.5)

    return clusters

testData=[[1,1],[2,1],[3,1],[3,2],[10,10],[10,15],[12,15],[0,0],[90,10],[-1,-1]]

k=sys.argv[1]

print(kMeans(testData, int(k)))
