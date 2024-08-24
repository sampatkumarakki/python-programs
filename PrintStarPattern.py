n = int (input ("enter the number :"))

for i in range (n):
    
    for j in range (n-i,0,-1):

        print (end = " ")
    
    for k in range (i):
            
        print (end = " *")

    print()


# Below code will print the * in downward direction


for i in range (n):
    
    for j in range (i):

        print (end = " ")
    
    for k in range (n-i,0,-1):
            
        print (end = " *")

    print()

# Below code will print a rignt angle triangle

for i in range (n):
    
    for k in range (i):
            
        print (end = " *")

    print()
