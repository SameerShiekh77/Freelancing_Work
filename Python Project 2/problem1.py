import numpy as np
def mysum(x):
    num = 0
    for n in x:
        num = num + n
    return num
def mymax(x):
    maxNumber = 1
#Yourcodegoesfromheretocalculateandreturnthemaximumvalue
    for a in x:
        if a > maxNumber:
            maxNumber = a
    return maxNumber

def mymin(x):
    minNumber = 1    
#Yourcodegoesfromheretocalculateandreturntheminimumvalue
    for a in x:
            if a < minNumber:
                minNumber = a
    return minNumber
# x = [0,1,2,3,4,5,6,7,8,9]
x = range(10)
#   expected   result:sum= 45	max=9	min= 0
print("sum=",mysum(x),"	max=",mymax(x),"	min=",mymin(x))# x =[1,3,5,7,9]
x = range(1,10,2)
#  expected  result:sum=25	max=9	min=1
print("sum=",mysum(x),"	max=",mymax(x),"	min=",mymin(x))

# x = 100 random numbers, rand() is a function to generate random numbers from
#  standard uniform distribution. Use  help(rand) or ?rand or rand? to see  help page  on   #randfunctioninCanopy.Rememberkeyinqandpressreturntoquithelppage.
x = np.random.rand(100)
# print(x)
print("sum=",mysum(x),"	max=",mymax(x),"	min=",mymin(x))
# expected result: depending on the random values.
