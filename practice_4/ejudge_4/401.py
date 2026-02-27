n = int(input())
squared_nums = (i * i for i in range(1, n+1))
for num in squared_nums:
    print(num)