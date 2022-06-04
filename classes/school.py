from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.students= Student.all_students()
        self.staff = Staff.all_staff()

    def list_students(self):
        for id, student in enumerate(self.students):
            print(f"{id + 1}. {student.name} {student.school_id}")
    
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
            return f"There s no student with the ID of: {student_id}"


    @property
    def get_name(self):
        return self.name

    @property
    def get_staff(self):
        return self.staff
    
    @property
    def get_students(self):
        return self.students
    
    def __repr__(self):
        return f"The school {self.name}."

