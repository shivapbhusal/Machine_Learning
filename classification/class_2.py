# A python program to plot different equations and see the result
# [1] 5x+5y-1=0, [2] -x+y+1=0 and [3] x-10=0 

#import matplotlib.pyplot as plt
#import numpy as np


def check12(x,y):
	if 5*x+5*y-1>0:
		return True 
	else:
		return False 

def check23(x,y):
	if -x+y+1>0:
		return True
	else:
		return False 

def check13(x,y):
	if x-10>0:
		return True 
	else:
		return False 

def classify(x,y):
	if check12(x,y)and check13(x,y):
		return "Class 1"
	elif check23(x,y) and not check12(x,y):
		return "Class 2"
	elif not check13(x,y) and not check23(x,y):
		return "Class 3"
	else:
		return "Ambiguous"

count=0 
for i in range(-10, 10):
	for j in range(-10,10):
		if classify(i,j)=="Ambiguous":
			count=count+1 

print(count)

