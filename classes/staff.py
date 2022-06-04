#staff.py
import os
import csv

from classes.person import Person

the_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(the_path, '../data/staff.csv')

class Staff(Person):
    def __init__(self, name, age, employee_id, password, role = 'Staff'):
        super().__init__(name,age,password)
        self.role = role
        self.employee_id = employee_id

    def get_school_id(self):
        return self.employee_id

    # def __repr__(self):
    #     return f'{self.name} is a {self.age} years old student who holds the {self.role} position. The student\'s id is {self.employee_id}'

    @classmethod
    def all_staff(cls):
        with open(path) as staff_files:
            staff_reader = csv.DictReader(staff_files)
            staff_arr = []
            for staff in staff_reader:
                staff_arr.append(Staff(staff['name'], staff['age'], staff['employee_id'], staff['password'], staff['role']))
            return staff_arr

# print(Staff.all_staff())
# linda = Staff('Linda', 24, 'Librarian', 'xx' , 28990778)
# print(linda)