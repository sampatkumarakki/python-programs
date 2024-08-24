import random

data = [
    {"name" : "abc", "country" : "usa", "follow" : 100},

    {"name" : "mno", "country" : "india", "follow" : 250},

    {"name" : "pqr", "country" : "uk", "follow" : 500},

    {"name" : "xyz", "country" : "kailasa", "follow" : 1000}
    ]


life = 1


while (life):

    c1 = random.choice(data)
    c2 = random.choice(data)
    same = 1

    print("First choice c1:",c1)
    print("First choice c2:",c2)
    
    while (same):
        if c1 == c2:
            c2 = random.choice(data)
            print("new c2 is :",c2)
        if c1 != c2:
            break

    
    print (f" 1 - Name : {c1['name']}, country : {c1['country']}")
    print()
    print("vs")
    print()
    print (f" 2 - Name : {c2['name']}, country : {c2['country']}")
    print()
    num = int(input ("Please enter who has more followers?? (1 - 2): "))

    if ( num == 1):
         
        if ( c1["follow"] > c2['follow'] ):
            print ("you got it right")
            continue
        else :
            print("you lost")
            break
    
    if ( num == 2):
         
        if ( c2["follow"] > c1['follow'] ):
            print ("you got it right")
            continue
        else :
            print("you lost")
            break
