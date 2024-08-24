class Bank:

    def __init__(self, num):
        self.acc = num
        self.balance = 0
        self.name = input("Please enter your full name :")
        self.pin = int(input("Please enter your pin for safety :"))

    
def withdraw():
    check = False
    acc = int(input ("Please enter account number :"))
    for i in range(len(SBI)):
        if (SBI[i].acc == acc):
            check = True
            break

    if (check == True):
        x = int(input ("Please enter 4 digit pin :"))
        if (SBI[i].pin == x):
            w = int( input ("Please enter the amount to withdraw :"))
            if (SBI[i].balance >= w):
                SBI[i].balance -= w
                print ("The remaining balance in your account is :", SBI[i].balance)
            else:
                print ("you dont have sufficient money")
        else:
            print ("you have entered a wrong pin")
    else:
        print ("You have entered a wrong account number")
       
            
def deposit():
    check = False
    acc = int(input ("Please enter account number :"))
    for i in range(len(SBI)):
        if (SBI[i].acc == acc):
            check = True
            d = int( input ("Please enter the amount to deposit :"))
            if (d > 0):
                    SBI[i].balance += d
                    print ("The current balance in your account is :", SBI[i].balance)
            else:
                print ("Deposite amount should be greater than 0")
    if (check == False):
        print ("You have entered a wrong account number")


def display():
    for i in range(len(SBI)):

        print("------------------------------------------------------------------")
        print(i+1)
        print()
        print ("The name of account holder is :", SBI[i].name)
        print ("The account number is :", SBI[i].acc)
        print ("The current balance in account is :", SBI[i].balance)
        print()
    print("------------------------------------------------------------------")


SBI = list()
choice = 0
                   
while (choice<5):
    print()
    print("******************************************************************")
    print ("1. Create a new account")
    print ("2. Deposite money")
    print ("3. Withdraw money")
    print ("4. Display balance")
    print ("5. Exit")
    choice = int( input("Enter your choice :"))
    if (choice == 1):
        S = Bank((len(SBI)+100))
        SBI.append(S)

    elif (choice == 2):
        deposit()
        
    elif (choice == 3):
        withdraw()

    elif (choice == 4):
        display()

    else :
        break
            

    

    
