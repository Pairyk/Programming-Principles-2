def main():
    _ = input()
    students = set()

    while True:
        try:
            student = input()
            students.add(student)
        except EOFError:
            break

    print(len(students))


if __name__ == "__main__":
    main()
