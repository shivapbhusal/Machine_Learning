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

    	clusterCenter.append(data(posOfMax))
    	newCluster=clusterCenter[0]
    	while(True):
    		newCluster=findPotentialCenter(data, centers)
    		if distance(newCluster)>getAvgDist(distances):
    			if newCluster in clusterCenter:
    				break
    			else:
    				if self.findDistance(newCluster,data[0])>0.5*self.getAvgDist(clusterCenter):
    					clusterCenter.append(newCluster)

    def getAvgDist(clusterCenter):
    	count=0
    	totalDist=0
    	for i in range(len(clusterCenter)):
    		for j in range(i,len(clusterCenter)):
    			totalDist=totalDist+findDistance(clusterCenter[i], clusterCenter[j])
    	return totalDist/count

    def findPotentialCenter(data, centers):
    	dist=[]
    	for patterns in data:
    		temp=[]
    		for c in centers:
    			temp.append(self.findDistance(data,c))
    		minPos=findPosOfMin(temp)
    		dist.append(data[minPos])
    		#Find the center as well.
    	posOfMax=self.findPosOfMax(dist)
    	return data[posOfMax]

    def findPosOfMax(self, distances):
    	posMax=0
    	maxDist=0
    	for i in range(len(distances)):
    		if distances[i]>maxDist:
    			maxDist=distances[i]
    			posMax=i
    	return posMax

    def findPosOfMin(self, distances):
    	posMin=0
    	minDist=0
    	for i in range(len(distances)):
    		if distances[i]<minDist:
    			minDist=distances[i]
    			posMin=i
    	return posMin

    def findDistance(self,p1, p2):
    	return 0.1

    def getMinimum(self, val1, val2):
    	if val1>val2:
    		return val2
    	else:
    		return val1

testData=[[1,1],[2,1],[3,1],[3,2],[10,10],[10,15],[12,15],[0,0],[90,10],[-1,-1]]

maxmin=MaxMin()
print(maxmin.createClusters(testData))


