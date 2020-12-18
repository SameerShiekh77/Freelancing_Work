# itemgetter is used by the sorted() system function
from operator import itemgetter

def createDict(filename):
    # Your code goes from here to create and return a dictionary
    with open(filename ,'r') as f:
        para = f.read()
    words = para.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
    
    
myDict =createDict("bigdata.txt")
# sort the items of the dictionary by descending order of the second entry of each pair (i.e.value in the key-valuepair)
# note that the return value is a list which is assigned to sortedList

sortedList  =  sorted(myDict.items(),  key=itemgetter(1),  reverse  =  True) # print the top 10 entries in the sortedlist

for key,value in sortedList[:10]:
    print(key, value)
