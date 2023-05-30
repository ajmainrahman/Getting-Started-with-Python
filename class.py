# class Student:
#     roll = ''
#     gpa = ''
#     university = ''
#
#     def __init__(self, roll, gpa, university):
#         self.roll = roll
#         self.gpa = gpa
#         self.university = university
#
#     def display(self):
#         print(f"Roll: {self.roll}\nGPA: {self.gpa}\nUniversity: {self.university}")
#
#
# rahim = Student(101,3.75,'Bangladesh University\n')
# rahim.display()
#
# fahim = Student(102,3.90,'Dhaka University')
# fahim.display()

class StoryBook:
    #CLASS VARIABLE
    no_of_books = 0

    discount = 0.5
    # a special method is used for setting the instance variables
    def __init__(self, name, price, author_name, author_born, no_of_pages):
        #instance Variable
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishing_year = 2000
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books = 1

    #Regular Method
    def get_book_info(self):
        print(f'The Book name: {self.name}, price: {self.price}, pages: {self.no_of_pages}')

    # Regular Method 2
    def get_author_info(self):
        print(f'The author name: {self.author_name}, Born: {self.author_born}')

    # applying discount to an instance
    def apply_discount(self):
        self.price = int(self.price - self.price * self.discount)


#creating object//instance
book_1 = StoryBook('Hamlet', 350,'Shakespeare',1564,500)
book_2 = StoryBook('The_Kite_runner', 200, 'Khaled Hosseini', 1965, 500)
# book_1.name = 'Lolipop'


print(book_2.price)
book_2.apply_discount()
print(book_2.price)
# print(book_1.no_of_books)
# print(book_2.no_of_books)
# book_1.get_book_info()
# StoryBook.get_author_info()
# book_1.get_author_info()

# print(book_1.name)
# print(book_1.author_born)
# print(book_1.publishing_year)

#instance Variable
# book_1.name = 'Hamlet'
# book_1.pricr = 350
# book_1.author = 'Shakespeare'
# book_1.author_born = 1564
#
# book_2.name = 'The_kite_runner'
# book_2.price = 200
# book_2.author  = 'Khaled Hossain'
# book_2.author_born = 1965
#
# print(f'First Book name is = {book_1.name}')
# print(f'Second Book name is = {book_2.name}')