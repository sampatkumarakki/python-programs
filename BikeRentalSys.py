
class CarRent :

    def __init__(s):
        s.stock = 100
        s.__price = 1000
        s.rent = 0

    def stocks (s):
        print ("The availble stock is ", (s.stock-s.rent))

    def rents (s):
        qty = int(input ("Enter the number of bikes to rent"))
        
        if ((s.stock-s.rent)>=qty):
            s.rent+=qty
            print ("The rent amount is ", (qty*s.__price))
            print ("The availble stock is ", (s.stock-s.rent))

        else :
            print ("The max availble stock is ", (s.stock-s.rent))


r=CarRent()

print ("Hello welcome to Rents", end = "********************************")
print ("********************************")
print ("********************************")
print ("********************************")


while(True):
    
    print ("1 - show available stocks")
    print ("2 - request for a bike")
    print ("3 - exit")

    num=int(input("enter your choice"))
    
    if num==1:
        r.stocks()

    elif num==2:
        r.rents()

    else :
        break

           
