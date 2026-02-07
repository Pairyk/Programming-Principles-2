# Example 1: Positional arguments (order matters)
def describe_pet(animal, name, age):
    print(f"I have a {animal} named {name}, who is {age} years old")

describe_pet("cat", "Whiskers", 2)


# Example 2: Keyword arguments (order doesn't matter)
def create_account(username, email, password):
    print(f"Account created:")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)}")

create_account(email="john@email.com", password="secret123", username="john_doe")


# Example 3: Default arguments
def make_coffee(size="medium", sugar=1, milk=False):
    print(f"Making {size} coffee with {sugar} sugar(s)")
    if milk:
        print("Adding milk")

make_coffee()  # Uses all defaults
make_coffee(size="large", sugar=2, milk=True)  # Override all
make_coffee(milk=True)  # Override only milk


# Example 4: *args - variable number of positional arguments
def sum_all(*numbers):
    total = sum(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    return total

sum_all(10, 20, 30, 40, 50)


# Example 5: **kwargs - variable number of keyword arguments
def display_info(**info):
    print("Information received:")
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="Paris")
display_info(product="Phone", price=599, brand="TechCo", color="Black")


# Example 6: Mixing positional, *args, and **kwargs
def make_pizza(size, *toppings, **details):
    print(f"Pizza Order: {size} size")
    print(f"Toppings: {', '.join(toppings)}")
    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

make_pizza("Large", "Pepperoni", "Mushrooms", "Olives", 
           delivery=True, tip=5, special_instructions="Extra cheese")


# Example 7: Order of arguments (required, *args, default, **kwargs)
def complex_function(required, *args, default="default_value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function("must_provide", 1, 2, 3, default="custom", key1="val1", key2="val2")