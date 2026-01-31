def main():
    _ = int(input())
    num = input().split()
    sum_result = sum(1 for x in num if int(x) > 0)
    print(sum_result)


if __name__ == "__main__":
    main()
