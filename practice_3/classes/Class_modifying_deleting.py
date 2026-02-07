# Example 1: Modifying instance attributes
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

car = Car("Toyota", "Camry", 2020)
print(f"Original: {car.brand} {car.model} ({car.year}) - {car.mileage} miles")

# Modify attributes
car.year = 2021
car.mileage = 15000
print(f"Modified: {car.brand} {car.model} ({car.year}) - {car.mileage} miles")


# Example 2: Adding new attributes dynamically
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(f"Initial attributes: name={person.name}")

# Add new attributes
person.age = 25
person.city = "New York"
person.occupation = "Developer"

print(f"After adding: {person.name}, {person.age}, {person.city}, {person.occupation}")


# Example 3: Deleting attributes with del
class Student:
    def __init__(self, name, grade, temporary_score):
        self.name = name
        self.grade = grade
        self.temporary_score = temporary_score

student = Student("Bob", "A", 95)
print(f"Before deletion: {student.name}, Grade: {student.grade}, Temp Score: {student.temporary_score}")

del student.temporary_score  # Delete attribute
print(f"After deletion: {student.name}, Grade: {student.grade}")
# print(student.temporary_score)  # Would cause AttributeError


# Example 4: Using delattr() function
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0.1

product = Product("Laptop", 1000)
print(f"Before: {product.name}, ${product.price}, Discount: {product.discount}")

delattr(product, 'discount')  # Alternative way to delete
print(f"After: {product.name}, ${product.price}")
# print(product.discount)  # Would cause AttributeError


# Example 5: Checking if attribute exists before accessing
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

account = Account("ACC123", 1000)

# Using hasattr() to check
if hasattr(account, 'balance'):
    print(f"Balance: ${account.balance}")

if hasattr(account, 'interest_rate'):
    print(f"Interest rate: {account.interest_rate}")
else:
    print("Interest rate not defined")

# Using getattr() with default value
overdraft = getattr(account, 'overdraft_limit', 0)
print(f"Overdraft limit: ${overdraft}")


# Example 6: Modifying attributes through methods (encapsulation)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction_count = 0
    
    def update_balance(self, amount):
        old_balance = self.balance
        self.balance += amount
        self.transaction_count += 1
        print(f"Balance updated: ${old_balance} → ${self.balance}")
    
    def reset_transaction_count(self):
        self.transaction_count = 0
        print("Transaction count reset")

account = BankAccount("Alice", 1000)
print(f"Initial: {account.owner}, ${account.balance}, Transactions: {account.transaction_count}")

account.update_balance(500)
account.update_balance(-200)
print(f"Transaction count: {account.transaction_count}")

account.reset_transaction_count()
print(f"Transaction count after reset: {account.transaction_count}")


# Example 7: Deleting entire objects
class TempFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"Created: {filename}")

temp1 = TempFile("temp1.txt")
temp2 = TempFile("temp2.txt")

print("Objects created")
del temp1  # Delete the object
print("temp1 deleted")
# print(temp1.filename)  # Would cause NameError
print(f"temp2 still exists: {temp2.filename}")
