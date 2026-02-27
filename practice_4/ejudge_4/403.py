n = int(input())

def only12(n):
    for i in range(0, n+1, 12):
        yield i

for num in only12(n):
    print(num, end = " ")