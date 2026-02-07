# Example 1: Basic function with no parameters
def say_hello():
    print("Hello, World!")

say_hello()


# Example 2: Function with parameters
def greet_user(name):
    print(f"Welcome, {name}!")

greet_user("Bob")


# Example 3: Function performing calculations
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(100, 250)


# Example 4: Function with statements
def check_temperature(temp):
    if temp > 30:
        print(f"{temp}°C is HOT!")
    elif temp < 10:
        print(f"{temp}°C is COLD!")
    else:
        print(f"{temp}°C is moderate")

check_temperature(22)


# Example 5: Function calling other functions
def get_discount_price(price):
    return price * 0.8

def show_pricing(product, original_price):
    discounted = get_discount_price(original_price)
    print(f"{product}:")
    print(f"Discounted: ${discounted}")

show_pricing("Laptop", 1000)


# Example 6: Function with loop
def print_countdown(start):
    for i in range(start, 0, -1):
        print(i, end=" ")

print_countdown(5)