def main():
    n = int(input())
    first_occurrence = {}

    for i in range(1, n + 1):
        string = input()
        if string not in first_occurrence:
            first_occurrence[string] = i

    # Sort by string (lexicographically) and print
    for string in sorted(first_occurrence.keys()):
        print(f"{string} {first_occurrence[string]}")


if __name__ == "__main__":
    main()
