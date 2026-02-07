class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self, pi = 3.14159):
        return self.radius**2 * pi
    
radius = int(input())
circle = Circle(radius)
print(f"{circle.area():.2f}")