import string

char = list(string.ascii_lowercase)

def encript (txt,shift):
    
    emsg = list()
    code = list()
    size = len(txt)
    
    for i in range (0,size):
        for j in range (0,26):
            
            # in char the values are stored in alphabetical order
            if txt[i] == char [j]:
                emsg.append(j)
                emsg[i] = int(emsg[i]) + shift
                print (emsg[i], txt[i])

                if emsg [i] > 25:
                    emsg [i] %= 26
                code.append(char[emsg[i]])

    print (emsg)
    print (code)

    '''#converting the char to a numerical value
    for i in range (0,size):
        emsg[i] = int(emsg[i]) + shift
        if emsg [i] > 25:
            emsg [i] = emsg [i] % 26
            print (emsg[i], txt[i])

    #code
    for i in range (0,size):
        
        code.append(char[emsg[i]])

    print (code)'''


       



a = "jenny"

encript(a,3)
        
        
        
