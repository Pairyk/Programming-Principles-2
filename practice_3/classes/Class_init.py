# Example 1: Basic __init__() constructor
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

student1 = Student("Alice", 20)  # __init__() is called automatically
student2 = Student("Bob", 22)
print(f"Student 1: {student1.name}, {student1.age} years old")
print(f"Student 2: {student2.name}, {student2.age} years old")


# Example 2: Constructor with default parameters
class Book:
    def __init__(self, title, author, pages=100, available=True):
        self.title = title
        self.author = author
        self.pages = pages
        self.available = available

book1 = Book("Python 101", "John Doe")
book2 = Book("Advanced Python", "Jane Smith", pages=500, available=False)
print(f"Book 1: {book1.title} by {book1.author} ({book1.pages} pages)")
print(f"Book 2: {book2.title} - Available: {book2.available}")


# Example 3: Constructor with validation
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        if balance < 0:
            print("Warning: Balance cannot be negative. Setting to 0.")
            self.balance = 0
        else:
            self.balance = balance

account1 = BankAccount("ACC001", 1000)
account2 = BankAccount("ACC002", -500)  # Validation triggers
print(f"Account 1: {account1.account_number} - ${account1.balance}")
print(f"Account 2: {account2.account_number} - ${account2.balance}")


# Example 4: Constructor performing calculations
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width  # Calculate during initialization
        self.perimeter = 2 * (length + width)

rect = Rectangle(10, 5)
print(f"Rectangle: {rect.length}x{rect.width}")
print(f"Area: {rect.area}, Perimeter: {rect.perimeter}")


# Example 5: Constructor with complex initialization
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.total = 0
        print(f"Shopping cart created for {customer_name}")

cart = ShoppingCart("Alice")
print(f"Customer: {cart.customer_name}")
print(f"Items: {cart.items}")
print(f"Total: ${cart.total}")


# Example 6: Multiple objects with different initialization
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

emp1 = Employee("Alice", "Developer", 75000)
emp2 = Employee("Bob", "Designer", 65000)
emp3 = Employee("Charlie", "Manager", 85000)

employees = [emp1, emp2, emp3]
for emp in employees:
    print(f"{emp.name} - {emp.position}: ${emp.salary}")