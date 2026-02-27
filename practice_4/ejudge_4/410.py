def repeater(iter_list, repeats):
    for _ in range(repeats):
        for num in iter_list:
            yield num
    
iter_list = input().split()
repeats = int(input())

for num in repeater(iter_list, repeats):
    print(num, end =" ")