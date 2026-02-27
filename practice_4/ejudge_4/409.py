n = int(input())
iter_two = (2**i for i in range(n+1))

for num in iter_two:
    print(num, end = " ")