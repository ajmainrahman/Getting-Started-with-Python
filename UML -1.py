class Rectang:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

rec = Rectang(5, 4)
print(rec.calculate_area())
print(rec.calculate_perimeter())