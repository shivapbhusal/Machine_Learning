'''
Python Implementation of K Means Algorithm 
Author : Shiva Bhusal 
'''
import math 
import sys
import time
def findDistance(list1, list2):
    distance=math.sqrt(pow((list1[0]-list2[0]),2)+pow((list1[1]-list2[1]),2))
    return distance

def findNewCenter(cluster):
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
    
testData=[[1,1],[2,1],[3,1],[3,2],[10,10],[10,15],[12,15],[0,0],[90,10],[-1,-1]]
c1=[1,1]
c2=[1.5,1]
newc1=[0,0]
newc2=[1,0]

while (newc1!=c1 and newc2!=c2):
    cluster1=[]
    cluster2=[]
    c1=newc1
    c2=newc2
    for points in testData:
        dist1=findDistance(points,c1)
        dist2=findDistance(points, c2)
        if dist1<dist2:
            cluster1.append(points)
        else:
            cluster2.append(points)
    
    newc1=findNewCenter(cluster1)
    newc2=findNewCenter(cluster2)

    print(cluster1)
    print(cluster2)

    #time.sleep(2)

    

print(cluster1)
print(cluster2)
