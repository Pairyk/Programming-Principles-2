def main():
    _ = int(input())
    nums = list(map(int, input().split()))
    operations = int(input())

    for _ in range(operations):
        operation = input()

        if operation.startswith("abs"):
            absolute = lambda a: abs(a)
            nums = (absolute(num) for num in nums)
        elif operation.startswith("add"):
            _, x = operation.split()
            addition = lambda a, x=int(x): a + x 
            nums = [addition(num) for num in nums]
        elif operation.startswith("multiply"):
            _, x = operation.split()
            multiplication = lambda a, x=int(x): a * x 
            nums = [multiplication(num) for num in nums]
        else:
            _, x = operation.split()
            power = lambda a, x=int(x): a ** x 
            nums = [power(num) for num in nums]

    print(*nums)

if __name__ == "__main__":
    main()