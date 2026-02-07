from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"({self.x}, {self.y})")

    def dist(self, other_x, other_y):
        distance = sqrt((other_x - self.x)**2 + (other_y - self.y)**2)
        print(f"{distance:.2f}")

x, y = map(int, input().split())
new_x, new_y = map(int, input().split())
dist_x, dist_y = map(int, input().split())


line1 = Point(x, y)
line1.show()
line1.move(new_x, new_y)
line1.dist(dist_x, dist_y)