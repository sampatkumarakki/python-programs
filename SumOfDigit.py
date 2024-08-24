n = input ("Enter a number")
l = len (n)
sum = 0

for i in range(l):
    sum+=int(n[i])

print ("The sum of digit is ",sum)
