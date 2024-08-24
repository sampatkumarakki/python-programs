#Silent bidding

import os

l= []

temp = "Y"

def bid ():
    # clear screen
    name = input("Please enter your name :")
    amt = input("Please enter your bid amount :")
    d = [name, amt]
    l.append(d)


top = 0

while ( temp == "Y" or temp == "y"):
    bid()
    temp = input ("do you still have bidder?? (Y/N)")
    #command to clear screen
    os.system('cls')

for i in range(0,len(l)):

    print (l[i][1])
    
    if (l[i][1] > l[top][1]):
        top = i

print (f"The top bidder is {l[top][0]} & the amount is {l[top][1]}")
    
