'''
Python implementation of MaxMin Algorithm
'''
import random
import math

class MaxMin():
    def __init__(self):
    	print("MaxMin object created")

    def createClusters(self, data):
    	distances=[]
    	clusterCenter=[data[random.randrange(0,len(data)-1)]]
    	for points in data:
    		distances.append(self.findDistance(points,clusterCenter))
    	posOfMax=self.findPosOfMax(distances)
    	print(posOfMax)
    	

    def findPosOfMax(self, distances):
    	posMax=0
    	maxDist=0
    	for i in range(len(distances)):
    		if distances[i]>maxDist:
    			maxDist=distances[i]
    			posMax=i
    	return posMax

    def findDistance(self,p1, p2):
    	return 0.5

testData=[[1,1],[2,1],[3,1],[3,2],[10,10],[10,15],[12,15],[0,0],[90,10],[-1,-1]]

maxmin=MaxMin()
print(maxmin.createClusters(testData))


