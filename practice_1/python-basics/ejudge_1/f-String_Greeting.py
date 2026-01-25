"""
Problem 114: 503039. f-String Greeting
Read a name (string) and an age (int).
Print the message: "Hello, {name}.
You are {age} years old." using Python f-strings.
"""


def main():
    name = input()
    age = int(input())
    print(f"Hello, {name}. You are {age} years old.")


if __name__ == "__main__":
    main()
