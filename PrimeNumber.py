n = int(input ("enter the last number"))
l = []

for i in range (1,n+1):
    count = 0
    
    for j in range (1,i+1):
        if (i % j == 0):
            count += 1

    if (count == 1 or count == 2):
        l.append(i)     
        
print (l)
