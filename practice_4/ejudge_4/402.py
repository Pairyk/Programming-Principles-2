n = int(input())

def even_gen(n):
    for i in range(0, n+1, 2):
        yield i

for num in even_gen(n):
    if num != 0:
        print(",", end ="")
    print(num, end ="")
