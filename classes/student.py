# student.py
import csv
import os
from classes.person import Person
the_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(the_path, '../data/students.csv')

class Student(Person):

    

    def __init__(self, name, age, school_id, password, role="Student"):
        super().__init__(name,age,password)
        self.role = role
        self.school_id = school_id

    def get_school_id(self):
        return self.school_id

    # def __repr__(self):
    #     return f'{self.name} is a {self.age} years old student who holds the {self.role} position. The student\'s id is {self.school_id}'
    
    def __str__(self):
        return f"""
        {self.name.capitalize()}
        --------------
        Age: {self.age}
        ID: {self.school_id}
        """
        

        

    @classmethod
    def all_students(cls):
        with open(path) as student_files:
            student_reader = csv.DictReader(student_files)
            student_arr = []
            for student in student_reader:
                student_arr.append(Student(student['name'], student['age'], student['school_id'], student['password'], student["role"]))
            return student_arr

# print(Student.all_students())
# linda = Student('Linda', 18, 'Teacher Assistant', 'xx', 28987789)
# print(linda)
# try:
   
            
# except Exception:
#     print(f'Sorry we don\'t have students')