'''
Python implementation of MaxMin Algorithm
'''
import random
import math

class MaxMin():
    def __init__(self):
    	print("MaxMin object created")

    def createClusters(self, data):
    	clusterCenter=[data[random.randrange(0,len(data)-1)]]
    	for points in data:
    		print(self.findDistance(points, clusterCenter[0]))

    def findDistance(self,p1, p2):
    	return math.sqrt(pow((p1[0]-p2[0]),2)+pow((p1[0]-p2[0]),2))

testData=[[1,1],[2,1],[3,1],[3,2],[10,10],[10,15],[12,15],[0,0],[90,10],[-1,-1]]

maxmin=MaxMin()
print(maxmin.createClusters(testData))


