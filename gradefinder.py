grade = {}

student = {"Ram" : 60, "Sham" : 99, "Kumar" : 75, "abhi" : 10}

for i in student:
    print (i)


for i in student:
    
    if student[i] > 90:
        grade[i] = "A"
        
    elif student[i] > 60:
        grade[i] = "B"
        
    elif student[i] > 30:
        grade[i] = "C"

    else:
        grade[i] = "F"


print(grade)
