#Christopher Kiernan
#CIS129 Module 11 Lab
#11-22-24

# This code writes the grade values and stores them in 'grades.txt' (For 9.1)
loop = 1
grades = open("grades.txt", "w")
while not loop == 0:
    name1 = input("Enter First Name: ")
    name2 = input("Enter Last Name: ")
    grade1 = input("Enter Grade from Exam 1: ")
    grade2 = input("Enter Grade from Exam 2: ")
    grade3 = input("Enter Grade from Exam 3: ")
    grades.write(name1 + " " + name2 + " " + grade1 + " " + grade2 + " " + grade3 + "\n")
    loop = input("Press Enter to Continue Adding More Data or 0 to Finish.")
    if loop == '0':
        break

# This code reads 'grades.txt' and puts the values into a table (For 9.2)
with open('grades.txt', mode='r') as grades:
    print(f'{"First":<10}{"Last":<10}{"Grades":<30}{"Average":>10}')
    for record in grades:
        name1, name2, grade1, grade2, grade3 = record.split()
        total = int(grade1) + int(grade2) + int(grade3)
        tests = 3
        average = float(total / tests)
        average = str(round(average, 2))
        print(f'{name1:<10}{name2:<10}{grade1:<10}{grade2:<10}{grade3:<10}{average:>10}')
input("Press Enter to Exit")
