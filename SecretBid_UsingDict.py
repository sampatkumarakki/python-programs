#Silent bidding

l={}

temp = "Y"

def bid ():
    # clear screen
    name = input("Please enter your name :")
    amt = input("Please enter your bid amount :")
    l[name] = amt


top = 0

while ( temp == "Y" or temp == "y"):
    bid()
    temp = input ("do you still have bidder?? (Y/N)")

for i in l:
    if (top == 0):
        top = i
        continue
    if (l[i] > l[top]):
        top = i

print (f"The top bidder is {top} & the amount is {l[top]}")
    
