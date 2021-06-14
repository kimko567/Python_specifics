students = {}
courses = []

def addStudent():
    grades = {}
    fname = input("input first name: ")
    lname = input("input last name: ")
   
    for c in courses:
        grades[c] = input("grade for " + c + ": ")

    students[lname, fname] = grades

def addCourse():
    course = input("input study course: ")
    courses.append(course)
    
    if len(students) > 0:
        print('input ' + course + ' grades:')

    for student, grades in students.items():
        msg = student[1] + ' ' + student[0] + ': '
        grades[course] = input(msg)
                   

def printGrades():
    print("list of students:")
    
    print('{:20} {:20}'.format("first","last"), end='')
    for course in courses:
        print('{:20}'.format(course), end='')
    print()
        
    for student, grades in students.items():
        print('{:20} {:20}'.format(student[1], student[0]), end='')
        for course in courses:
            print('{:20}'.format(grades[course]), end='')
        print()
    
def fail():
    print('last names of students who failed:') #uzdevumā prasīts izvadīt uzvārdus (nekas papildus)
    for course in courses:
        for student, grades in students.items():
            if int(grades[course]) < 4:
                print(student[0])

while True:
    print()
    command = input("command:> ")
    command = command.lower()
    
    if command == 'addstud':
        addStudent()
    elif command == 'addcourse':
        addCourse()
    elif command == 'print':
        printGrades()
    elif command == 'fail':
        fail()
    elif command == 'done':
        break
print("DONE")
