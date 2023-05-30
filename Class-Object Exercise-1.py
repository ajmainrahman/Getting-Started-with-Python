#Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.
class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
#create object
s = Students('Ajmain',22,3.73)
