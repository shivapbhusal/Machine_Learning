# A python program to plot different equations and see the result
# [1] 5x+5y-1=0, [2] -x+y+1=0 and [3] x-10=0 

#import matplotlib.pyplot as plt
#import numpy as np

def check1(x,y):
	if 5*x+5*y-1>0:
		return True 
	else:
		return False 

def check2(x,y):
	if -x+y+1>0:
		return True
	else:
		return False 

def check3(x,y):
	if x-10>0:
		return True 
	else:
		return False 

def classify(x,y):
	if check1(x,y)and not check2(x,y) and not check3(x,y):
		return "Class 1"
	elif not check1(x,y) and check2(x,y) and not check3(x,y):
		return "Class 2"
	elif not check1(x,y) and not check2(x,y) and check3(x,y):
		return "Class 3"
	else:
		return "Ambiguous"

print(classify(-10,0))
print(classify(0,20))
print(classify(5,0))
print(classify(12,-20))

