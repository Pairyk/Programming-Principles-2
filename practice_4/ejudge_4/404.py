a, b = map(int, input().split())

def be_there_or_be_squared(a, b):
    for i in range(a, b + 1):
        yield i * i

for num in be_there_or_be_squared(a, b):
    print(num)