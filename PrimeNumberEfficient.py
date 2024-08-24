def primenum (n):
    l = []
    for x in range (1,n+1):
        result = 1
        for i in range (2,x):
            if (i != x):
                if (x % i == 0):
                    result = 0
        if result == 1:
            print ("its a prime number")
            l.append(x)
        else :
            print ("its not a prime number")
            
            
    return (l)


x = int (input ("Enter a number :"))
print(primenum(x))
