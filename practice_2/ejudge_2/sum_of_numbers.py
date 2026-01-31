def main():
    n = int(input())
    num = input().split()
    sum_result = sum(int(x) for x in num)
    print(sum_result)


if __name__ == "__main__":
    main()
