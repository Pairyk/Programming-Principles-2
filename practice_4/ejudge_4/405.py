n = int(input())

def count_down(n):
    for i in range(n, -1, -1):
        yield i

for num in count_down(n):
    print(num)