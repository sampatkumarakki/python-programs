import random

name = input ("Enter the names seperated by space :")

l = name.split(" ")

last = len(l)

n = random.randint(0,last-1)

print ("The random number generated is ",n)
print ("The bill will be paid by :", l[n])
