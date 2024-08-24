# Calculator

ops = { "+" : add, "-" : substract, "*" : multiply, "/" : divide}

def add(a,b):
    print(a+b)

def substract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a/b)

print ("enter two numbers")
a = int(input())
b = int(input())

print ("please select the operaiton")
for i in ops:
    print (i)

sym = input()

fns = ops [sym]

print (fns)

fns(a,b)
