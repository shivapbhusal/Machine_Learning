# A python program to plot different equations and see the result
# [1] 5x+5y-1=0, [2] -x+y+1=0 and [3] x-10=0 

#import matplotlib.pyplot as plt
#import numpy as np

def equ1(x,y):
	return 5*x+5*y-1

def equ2(x,y):
	return -x+y+1

def equ3(x,y):
	return x-10

def check12(x,y):
	if equ1(x,y)-equ2(x,y)>0:
		return True 
	else:
		return False 

def check23(x,y):
	if equ2(x,y)-equ3(x,y):
		return True
	else:
		return False 

def check13(x,y):
	if equ1(x,y)-equ3(x,y)>0:
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

print(classify(-10,0))
print(classify(0,20))
print(classify(5,0))
print(classify(12,-20))

