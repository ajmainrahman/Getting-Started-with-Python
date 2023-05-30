# #Parent Class, Super Class, Base Class
# #Child Class, Sub Class
# class phone:
#     def call(self):
#         print('You can call me')
#     def message(self):
#         print('You can message')
#
# class Apple:
#     def call(self):
#         print('I am the boro bhai!')
#     def message(self):
#         print('You can call me Boss')
#     def batter(self):
#         print('So SAD!')
# class Samsung(Apple,phone):
#     def photo(self):
#         print('I am the boss of Mobile photography Industry')
#
# s = Samsung()
# s.call()
# s.message()
# s.batter()
# print(issubclass(Samsung,Apple))
#
#

class Robot:
    # def __init__(self, name, version):
    #     self.name = name
    #     self.version = version

    def move_right(self):
        print('I am moving forward')
    def move_left(self):
        print(f'{self.name} is moving left')
    def move_forward(self):
        print(f'{self.name} is moving forward')
    def move_backward(self):
        print(f'{self.name} is moving backward')

class HouseBot(Robot):
    # def __init__(self, name, version, area_covered):
    #     super().__init__(name, version)
    #     self.area_covered  = area_covered
    def message(self):
        print('You can message me')
    def talk(self):
        print('you can use me')

# hBot = HouseBot('hBot',1.1, 40)
# print(hBot)
# hBot.move_forward()

r = Robot() #instance
r.move_right()


h = HouseBot()
h.talk()