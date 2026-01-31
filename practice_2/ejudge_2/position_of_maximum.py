def main():
    num = list(map(int, input().split()))
    print(num.index(max(num)) + 1)


if __name__ == "__main__":
    main()
