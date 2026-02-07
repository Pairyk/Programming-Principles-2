class Shape():
    def area():
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

length = int(input())
square = Square(length)
print(square.area())