import csv

with open('grades.csv', mode='w') as grades:
    w = csv.writer(grades, quoting=csv.QUOTE_ALL)
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    exam1grade = input("Enter Grade from Exam 1: ")
    exam2grade = input("Enter Grade from Exam 2: ")
    exam3grade = input("Enter Grade from Exam 3: ")
    w.writerow([firstName, lastName, exam1grade, exam2grade, exam3grade])


input("Press Enter to Exit")
