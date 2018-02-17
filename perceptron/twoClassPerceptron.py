# Python implementation of a simple Perceptron 
# Author: Shiva Bhusal 

def calculateOutput(theta,weights, x,y):
    sum=x*weights[0]+y*weights[1]+weights[2]
    if sum>=theta:
        return 1.0
    else:
        return 0.0

THETA=0.1
INSTANCES=8
LEARNING_RATE=0.5
MAX_ITER=8 
X=[1,2.5,2,4,-1,-2.5,-2,-4]
Y=[1,2.5,3,5,-1,-2.5,-3,-5]

weights=[0.2,0.2,0.2] 
outputs=[0,0,0,0,1,1,1,1]
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

print(weights)    

print(calculateOutput(THETA,weights,3.5,3.5))
print(calculateOutput(THETA, weights,-3.5,-3.5))



# Acknowledgement:Perceptron discussion in Java: https://www.youtube.com/watch?v=4aksMtJHWEQ&t=623s
