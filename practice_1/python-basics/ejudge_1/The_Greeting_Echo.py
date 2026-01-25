"""
Problem 101: 503011. The Greeting Echo
Read a name from the input and print a greeting in the format “Hello, {name}!”.
"""


def say_hi(name) -> None:
    print(f"Hello, {name.strip()}!")


def main():
    name = input()
    say_hi(name)


if __name__ == "__main__":
    main()
