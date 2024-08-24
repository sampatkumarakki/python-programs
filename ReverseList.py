n=int(input("enter how many numbers:"))

print ("enter the numbers:")

l = list ()

rl = list ()

# get input in a list

for i in range (0,n):
    print
    l.append(int(input()))

#reverse the list
count=0

while (count < n):
    rl.append(l[n-1-count])
    count+=1

print (rl)
