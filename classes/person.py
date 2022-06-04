# student.py
import csv
import os

class Person:
    the_path = os.path.abspath(os.path.dirname(__file__))
    
    def __init__(self, name, age, password):
        self.name = name
        self.age = age      
        self.password = password

    @property
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    

    
