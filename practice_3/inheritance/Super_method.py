# Example 1: Basic super() usage
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person.__init__ called for {name}")
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent's __init__
        self.student_id = student_id
        print(f"Student.__init__ called for {name}")
    
    def introduce(self):
        super().introduce()  # Call parent's introduce
        print(f"My student ID is {self.student_id}")

student = Student("Alice", 20, "S12345")
student.introduce()


# Example 2: super() vs direct parent call
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal constructor: {name}")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)  # Recommended way
        self.fur_color = fur_color
        print(f"Mammal constructor: {fur_color} fur")

class Bird(Animal):
    def __init__(self, name, can_fly):
        Animal.__init__(self, name)  # Old way (still works)
        self.can_fly = can_fly
        print(f"Bird constructor: can_fly={can_fly}")

print("Using super():")
mammal = Mammal("Lion", "golden")

print("\nDirect parent call:")
bird = Bird("Penguin", False)


# Example 3: super() in multilevel inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle: {brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        print(f"Car: {model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        print(f"ElectricCar: {battery_capacity}kWh battery")

tesla = ElectricCar("Tesla", "Model 3", 75)
print(f"\nFinal object: {tesla.brand} {tesla.model} ({tesla.battery_capacity}kWh)")


# Example 4: super() with methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Square has equal sides
    
    def diagonal(self):
        # Use parent's area method via super()
        area = super().area()
        return (2 * area) ** 0.5

square = Square(5)
print(f"Square side: 5")
print(f"Area (from parent): {square.area()}")
print(f"Perimeter (from parent): {square.perimeter()}")
print(f"Diagonal (child method): {square.diagonal():.2f}")


# Example 5: super() to extend parent functionality
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        # Extend parent's deposit with interest calculation
        super().deposit(amount)  # Call parent's deposit
        interest = amount * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")

savings = SavingsAccount("Alice", 1000, 0.03)
savings.deposit(500)


# Example 6: super() with multiple methods
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def annual_salary(self):
        return self.salary * 12
    
    def info(self):
        print(f"Employee: {self.name}")
        print(f"Monthly salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def annual_salary(self):
        # Use parent's calculation and add bonus
        base = super().annual_salary()
        return base + self.bonus
    
    def info(self):
        super().info()  # Call parent's info
        print(f"Annual bonus: ${self.bonus}")
        print(f"Total annual: ${self.annual_salary()}")

manager = Manager("Bob", 5000, 10000)
manager.info()