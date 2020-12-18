import numpy as np
import math

def getNorm(x):
    #Yourcodegoesfromheretocalculateandreturnthenorm
    num = 0
    for i in x:
        num = (i*i) + num
    norm = math.sqrt(num)
    return norm

def getInnerProd(x, y):
# Your code goes from here to calculate and return the inner product
    return np.dot(x, y)
def getDist(x, y):
    # Your code goes from here to calculate and return the distance
    distance = math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) +((x[2]-y[2])**2)+((x[3]-y[3])**2)+((x[4]-y[4])**2) )
    return distance

# xVec= [0,1,2,3,4]
xVec =range(5)

# yVec= [4,3,2,1,0]
yVec=range(4,-1,-1)

#  expected  result:  norm(x)=  5.4772	norm(y) =5.4772
print("norm(x)=",getNorm(xVec),"norm(y) =",getNorm(yVec))

#expectedresult:innerprod(x,y)=10
print("innerprod(x,y) =" ,  getInnerProd(xVec,   yVec)) 

#expected result: distance(x,y) = 6.3246
# print("distance(x,y) =", getDist(xVec,yVec))
getDist(xVec,yVec)

# Generate  two  random  vectors  of  length  10  and  calculate  their  distance.  # Your code goes from here. Use rand() to generate randomvectors.
x = np.random.rand(10)
y = np.random.rand(10)
print("xvector=", x,"\nyvector=",y,"\n")
print("distance(x,y) =", getDist(x,y))
