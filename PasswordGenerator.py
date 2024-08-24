import string
import random
 
 
#letter = list(string.ascii_letters)
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
number = list(string.digits)
symbol = list(string.punctuation)

#x = letter + number + symbol

password = []

low = int (input ("Enter the number of lower case letters:"))
up = int (input ("Enter the number of upper case letters:"))
num = int (input ("Enter the number of numbers:"))
sym = int (input ("Enter the number of symbols:"))

for i in range (low):
    password += random.choice (lower)
    
for i in range (up):
    password += random.choice (upper)

for i in range (num):
    password += random.choice (number)

for i in range (sym):
    password += random.choice (symbol)

random.shuffle(password)

# in below code we are converting list to string

pas=""

for i in password:
    pas+= i

print ("The password is :", password)
 
print ("The password is :", pas)
