#Write a program to create a child class Teacher that will inherit the properties of Parent class Staff
class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role: ", self.role)
        print("Department: ",self.dept)

#inherite from staff class
class Teacher(Staff):
    def __init__(self,name, age):
        self.name = name
        self.age  = age
        #initialize the parent class
        super().__init__("Teacher","Science",25000)

# teacher = Teacher('Mr. Tech',50)
# teacher.show_details()
teac = Teacher('Mr. Tech', 50)
teac.show_details()


#What would be the output of the following program?