def main():
    _ = input()
    nums = map(int, input().split())
    seen = set()

    for num in nums:
        if num in seen:
            print("NO")
        else:
            print("YES")
            seen.add(num)


if __name__ == "__main__":
    main()
