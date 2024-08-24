l = input ("Enter the number list seperated by space :")
s = l.split(" ")


for i in range (0,len(s)):
    s[i]=int(s[i])
    

for i in range (0,len(s)):
    small = s[i]
    for j in range (i, len(s)):
        if small > s[j]:
            small = s[j]
            s[j] = s[i]
            s[i] = small
    

print ("The sorted format is :",s)
