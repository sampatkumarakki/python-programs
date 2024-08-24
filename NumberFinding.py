import random

n = random.randint(0,100)

lvl = input ("enter the difficulty level (H - hard & E - easy) :")

if (lvl == "H"):
    life = 5
    
else:
    life = 10

while (life > 0):
    guess = int(input ("Enter your guess"))

    if guess == n:
        print ("you got it right")
        break

    elif guess > n:
        print ("your guess is high")
        life-=1
        
    else :
        print ("your guess is low")
        life-=1
    
