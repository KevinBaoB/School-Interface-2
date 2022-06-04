from classes.school import School 
# from classes.student import Student

school = School('Ridgemont High') 

# print(school.name)


start_up = True

while start_up:

    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
    elif mode == '5':
        start_up = False
    else:
        pass
