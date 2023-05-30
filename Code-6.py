class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age

        #private attribute
        self.__salary = salary

    def show_details(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

    #access private arrtibute
        print("Salary: ",self.__salary)
teacher  = Teacher("Ajmain",23, 35000)
# teacher.show_details()
print(teacher.name)
print(teacher.age)
