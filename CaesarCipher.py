import string

char = list(string.ascii_lowercase)

def encode (txt,shift):
    emsg = list()
    code = list()
    size = len(txt)
    
    for i in range (0,size):
        for j in range (0,26):
            
            #converting the char to a numerical value
            if txt[i] == char [j]:
                emsg.append(j)
    
    #encoding
    for i in range (0,size):
        print (i)
        emsg[i] += shift
        if emsg [i] > 25:
            emsg [i] %= 26
            print (emsg[i], txt[i])

    for i in range (0,size):
        code.append(char[emsg[i]])

    print (emsg)
    print (code)


       
def decode (txt, shift):

    dmsg = list()
    code = list()
    size = len(txt)
    
    for i in range (0,size):
        for j in range (0,26):
            
            #converting the char to a numerical value
            if txt[i] == char [j]:
                dmsg.append(j)

    #Decoding
    for i in range (0,size):
        dmsg[i] -= shift

        if dmsg[i] <= 0:
            dmsg [i] += 26
            
    for i in range (0,size):
        code.append(char[dmsg [i]])

    print (code)



dec = 1
while (dec):
    print ('''what you want to do
1: Encode
2: Decode
3: Exit''')
    temp = int(input())

    if (temp == 1):
        msg = input("enter the message to encode :")
        sft = int(input("enter the encoding value :"))
        encode(msg,sft)
    
    elif (temp == 2):
        msg = input("enter the message to encode :")
        sft = int(input("enter the encoding value :"))
        decode(msg,sft)
    
    else :
        break
