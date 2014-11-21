from random import randint
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import sys
import timeit
import re

start = timeit.default_timer()
#Global Initialization
dimension,inp =(None,[])

def getInputData():
    for v in open(sys.argv[1]):
        inp.append([float(x) for x in v.split(" ")])

'''
k = number of cluster
'''
def kmeans(k):
    bestCost,bestCluster,cost=(0,[],0)
    bestrand = None
    for loop in range(1,101):
        cluster,already = ([],[])
        getRandomCentroid(k,cluster,already)
        rand =( cluster[0][0],cluster[1][0])
        kmean(cluster)
        cost = calculateCost(cluster)
        if bestCost > cost:
            bestCluster[:]=[]
            bestCluster = cluster[:]
            bestCost = cost
            bestrandom = rand
        elif bestCost == 0:
            bestCost = cost
            bestCluster = cluster[:]
            bestrandom = rand
    kmeanoutput(bestCluster)
    End = timeit.default_timer()
    print(End-start)
    
    
def kmeanoutput(bestCluster):
    i =0
    count = 0
    clust = len(inp)*[0]    
    for x in range(0,len(inp)):
        for i in range(0,k):
            if(x in bestCluster[i][5]):
                clust[count] = i
                break;
        count += 1
    print(clust)        
    
def getRandomCentroid(k,cluster,already):
    i=0
    while(i<k):
        x = randint(0,len(inp)-1)
        if x not in  already:
            cluster.append([inp[x][:],[],0,[],[],[]]) #centroid,list of elements , Previous centroid check , all the elements
            already.append(x)
            i += 1
        
def kmean(cluster):
    j = 0
    while(1):
        for a in cluster:
            a[3] = a[0]
            a[2] = 0
            a[1][:] = []
            a[4][:] = []
            a[5] = []
        calculateDistance(cluster)
        forall = calculateNewCentroid(cluster)
        if forall == 1:
            j += 1
        else:
            j = 0;
        if j>2:
            break
def calculateDistance(cluster):
    binary = 0
    for i in inp:
        minval,clustkey = (None,None)
        for key in cluster:
            d = math.sqrt(sumup(key[0],i))            
            if minval is None:
                minval,clustkey = (d,key)
            else:
                if minval >= d:  # IF TWO values let one is random cluster and
                    minval,clustkey = (d,key)           
        
        for jump in range(0,len(i)):
            if len(clustkey[1]) <= jump:
                clustkey[1].append(i[jump])
                clustkey[4].append(i[jump])
                clustkey[5].append(binary)
            else:
                clustkey[1][jump] = clustkey[1][jump] + i[jump]
                clustkey[4].append(i[jump])
                clustkey[5].append(binary)
        binary += 1
                

def calculateNewCentroid(cluster):
    forall = 0
    global dimension
    for key in cluster:
        temp,innercheck = (None,0)
        for i in range(0,len(key[1])):
            temp =  (key[1][i]/(len(key[4])/dimension))
            if temp == key[0][i]:
                innercheck = 1
            else:
                innercheck = 0
            key[0][i] = temp
            
        if( innercheck == 1):
            forall = 1
        else:
            key[3] = key[0]
            forall = 0   
    return forall                    

def calculateCost(cluster):
    cost = 0
    global dimension
    for  key in cluster:
        summ = 0.0 
        for elementIndex in range(0,len(key[4]),dimension):
            for i in range(0,dimension):
                summ = summ + ((key[0][i]-key[4][elementIndex+i])**2)

        cost = cost + summ 
        
    return cost

def sumup(key,i):
    jump = 0
    summ = 0
    while(jump < len(key)):
        summ = summ + ((key[jump]-i[jump])**2)
        jump += 1
    return summ

    
def averageLinkage(cluster):
    avgL,index = ([],0) 
    for x in inp[:]:
        avgL.append([[x],[index]])
        index += 1
    while(cluster != len(avgL)):
        avg,m1,m2 = (0,None,None)
        for i in range(0,len(avgL)):
            for j in range(i+1,len(avgL)):
                summall,count=processCluster(avgL,i,j)
                avg,m1,m2=selectedCluster(avg,summall,count,m1,m2,i,j)
        cleaningUp(avgL,m1,m2)        
    averageoutput(avgL)
    End = timeit.default_timer()
    print(End-start)
    
def processCluster(avgL,i,j):
    summall,count=(0,0)
    for k in range(0,len(avgL[i][0])):
        for l in range(0,len(avgL[j][0])):
           inner,summ = (0,0)
           while(inner<len(avgL[i][0][k])):
               summ = summ + ((avgL[i][0][k][inner]-avgL[j][0][l][inner])**2)
               inner += 1
           summall = summall + math.sqrt(summ)
           count += 1

    return(summall,count)

def selectedCluster(avg,summall,count,m1,m2,i,j):
    if avg > (summall/(count)):
        avg,m1,m2 = (summall/(count),i,j)
    elif avg == 0:
        avg,m1,m2 = (summall/(count),i,j)
    return(avg,m1,m2)

def cleaningUp(avgL,m1,m2):
    avgL[m1][0].extend(avgL[m2][0][:])
    avgL[m1][1].extend(avgL[m2][1][:])
    del(avgL[m2])

def averageoutput(bestCluster):
    i,count = (0,0)
    clust = len(inp)*[0]    
    for x in range(0,len(inp)):
        for i in range(0,k):
            if(x in bestCluster[i][1]):
                clust[count] = i
                break;
        count += 1
    print(clust)
    

        plt.show()     
        
if __name__ == "__main__":
    
    
    if len(sys.argv) == 4:
        
        getInputData()
        #k = int(sys.argv[2])
        k = int(sys.argv[2])
        dimension = len(inp[0])
        if sys.argv[3] == "kmeans":
            kmeans(k)
        elif sys.argv[3] == "average":
            averageLinkage(k)
        else:
            sys.exit
        stop = timeit.default_timer()    
    else:
        print("Enter Proper Command")
         
