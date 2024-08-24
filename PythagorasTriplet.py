import math

n = int(input ("enter the last"))

for i in range (1,n+1):
    
    for j in range (i,n+1):
        
        a = i**2
        b = j**2
        c = a + b
        
        for k in range (i, n+1):
            """ The value of k cannot be greater than n+1"""
            if ((k**2) == c):
                
                print (i, j, k)


print ("***************************")
print ("***************************")
print ("***************************")


for i in range (1,n+1):
    
    for j in range (i,n+1):
        
        a = i**2
        b = j**2
        c = a + b

        k = int(math.sqrt (c))
        """ The value of k is irrespective of n+1 & it can be greater than n+1 in this case"""

        if (c / k == k):

            print (i,j,cube)

    

