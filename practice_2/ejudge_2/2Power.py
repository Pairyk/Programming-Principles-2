def main():
    num = int(input())
    result = [2**i for i in range(num) if 2**i <= num]
    print(*result, sep=" ")


if __name__ == "__main__":
    main()
