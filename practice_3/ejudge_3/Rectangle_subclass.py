class Shape():
    def area():
        return 0
    
class Square(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length, width = map(int, input().split())
square = Square(length, width)
print(square.area())