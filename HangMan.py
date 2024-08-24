# Hang Man Game

import random

l = ["bannana","apple","pineapple","mango","grape"]
#pick random item form list
compchoice = list(random.choice(l));

countlet = 0
word = list()

display = ""


print (display)

for i in compchoice:
    countlet+=1

for i in range (countlet):
    word+="_"


print (word)


life = 6

while (life > 0):

    print("Begning of the while loop")
    track = 0
    print()
    
    print ("Guess the word :")
    guess = input()

        
    for i in range (0,countlet):
        if guess == compchoice[i]:
            word[i] = compchoice[i]
            track = 1

    
    if word == compchoice:
        print ("you got the word right")
        print ("The word was :", word)
        break

    
    if track == 1:
        pass
    else :
        life -= 1

    print ("At the end of while loop")
    
    print ("life left :", life)        
    print ("The word at the end of while :", word)
