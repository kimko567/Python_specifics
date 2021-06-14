grades = {}

def addGrade(grades):
    course = input("input course: ")
    grade = int(input("input grade: "))
    grades[course] = grade

def printGrades(grades):
    print('all grades:')
    for c, g in grades.items():
        print(c + "\t" + str(g))

def average(grades):
    summ=0
    for c, g in grades.items():
        summ += g
    print('average grade: ' + str(round(summ/len(grades),3)))

def fail(grades):
    print('failed courses:')
    for c, g in grades.items():
        if g < 4:
            print(c)

while True:
    command = input("command: ")
    command = command.lower()
    
    if command == 'add':
            addGrade(grades)
    elif command == 'print':
            printGrades(grades)
    elif command == 'average':
            average(grades)
    elif command == 'fail':
            fail(grades)
    elif command == 'done':
            break
print("DONE")
    
