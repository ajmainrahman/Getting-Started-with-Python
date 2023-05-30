class Squre:
    def __init__(self,length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width
    def perimeter(self):
        return  2*(self._length + self._width)

square = Squre(9,3)

print(square.area())
print(square.perimeter())