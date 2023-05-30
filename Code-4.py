#Write a Program to create a class and, using the class instance, print all the writable attributes of that object.
class Staff:
    def __init__(self,role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_output(self):
        print("Name: ",self.name)
        print("Age: ",self.name)
        print("Role: ",self.name)
        print("Salary: ",self.name)

class Teacher(Staff):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Teacher","CSE",45000)

teacher = Teacher("Ajmain",23)
print(teacher.__dict__)