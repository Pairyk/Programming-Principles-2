class Pair():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, new_a, new_b):
        print(f"Result: {self.a + new_a} {self.b + new_b}")

a, b, new_a, new_b = map(int, input().split())

pair = Pair(a, b)
pair.add(new_a, new_b)
