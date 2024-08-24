l = input ("Enter the number list seperated by space :")
s = l.split(" ")


for i in range (0,len(s)):
    s[i]=int(s[i])
    print (type(s[i]))


small = s[0]

for i in range (1,len(s)):
    if small > s[i]:
        small = s[i]
    

print ("Smallest is :",small)
