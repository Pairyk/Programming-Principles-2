def main():
    n = int(input())
    num_holder = {}

    for _ in range(n):
        number = input().replace("+", "")
        num_holder[number] = num_holder.get(number, 0) + 1

    count = 0
    for freq in num_holder.values():
        if freq == 3:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
