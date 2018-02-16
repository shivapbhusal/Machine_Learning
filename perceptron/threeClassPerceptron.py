# Python implementation of a simple Perceptron 
#Author: Shiva Bhusal, BGSU  
# Acknowledgement: 

THETA=0
INSTANCES=8
LEARNING_RATE=0.5
MAX_ITER=8 

def calculateOutput(theta,weights, x,y):
    total=x*weights[0]+y*weights[1]+weights[2]
    return total

def classify(total):
    if total>THETA:
        return "Class A"
    else:
        return "class B"

def findWeights(X,Y):
    weights=[0.2,0.2,0.2] 
    outputs=[1,1,1,1,0,0,0,0]

    globalError=10
    iteration=0

    while globalError!=0 and iteration<=MAX_ITER:
        globalError=0
        for i in range(INSTANCES):
            output=calculateOutput(THETA,weights,float(X[i]),float(Y[i]))
            localError=float(outputs[i])-output
            weights[0]=float(weights[0])+LEARNING_RATE*localError*X[i]
            weights[1]=float(weights[1])+LEARNING_RATE*localError*Y[i]
            weights[2]=float(weights[2])+LEARNING_RATE*localError
            globalError=globalError+localError*localError
        iteration=iteration+1
    return weights    

XAB=[4.5,4,5.5,6,-2,-2.5,-2,-3]
YAB=[6,7,6,6.5,-2.5,-2.5,-3,-4.5]

XBC=[-2,-2.5,-2,-3,-6.5,-7,-6,-8]
YBC=[-2.5,-2.5,-3,-4.5,8,7.5,10,8.5]

XCA=[-6.5,-7,-6,-8,4.5,4,5.5,6]
YCA=[8,7.5,10,8.5,6,7,6,6.5]

NewPoints=[[]]

def findClass(x,y):
    if calculateOutput(THETA,findWeights(XAB,YAB),3.5,3.5)>calculateOutput(THETA,findWeights(XBC,YBC),3.5,3.5) and calculateOutput(THETA,findWeights(XAB,YAB),3.5,3.5)>calculateOutput(THETA,findWeights(XCA,YCA),3.5,3.5):
        print("Class A")
    elif calculateOutput(THETA,findWeights(XBC,YBC),3.5,3.5)>calculateOutput(THETA,findWeights(XAB,YAB),3.5,3.5) and calculateOutput(THETA,findWeights(XBC,YBC),3.5,3.5):
        print("Class B")
    else:
        print("Class C") 


NewPoints=[[4,6],[-3,-4],[-8,9.5]]

for x,y in NewPoints:
    findClass(x,y)
