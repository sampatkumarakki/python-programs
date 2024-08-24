n=int(input ("enter the year"))

if n%4 == 0:
    if n%100 == 0:
        if n%400 == 0:

            print (n," is a leap year")
            print ("*****************")

        else : 
            print(n, "is not a leap year")
            print ("3")
    else :
        print(n," is a leap year")
        print ("2")
else :
    print (n," is not a leap year")
    print ("1")
