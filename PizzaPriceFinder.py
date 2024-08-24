print ("""Enter your choice
       1-Small Pizza
       2-Medium Pizza
       3-Large Pizza""")

choice = int(input())
price = 0

if choice == 1:
    price += 50
elif choice == 2:
    price += 100
elif choice == 3:
    price += 200

fav = input ("Do you need Pepperoni? (Y/N)")

if fav == 'Y' or fav == 'y':

    if choice == 1:
        price+=30

    else :
        price+=50

fav = input ("Do you need Chesse? (Y/N)")
if fav == 'Y' or fav == 'y':
    price+=20

print ("The total price of you order is :", price)
print ("Thank you")
