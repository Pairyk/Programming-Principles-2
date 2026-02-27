n = int(input())

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        if i == n-1:
            yield a
        else:
            yield f"{a},"
        a, b = b, a+b


for num in fibonacci(n):
    print(num, end="")
