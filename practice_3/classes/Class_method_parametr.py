# Example 1: Simple instance method
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self): 
        self.count += 1
    
    def get_count(self):
        return self.count


counter = Counter()
print(f"Initial count: {counter.get_count()}")
counter.increment()
counter.increment()
counter.increment()
print(f"After 3 increments: {counter.get_count()}")


# Example 2: Methods with parameters
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):  # self + parameter
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)  # Insufficient funds


# Example 3: Methods calling other methods
class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
    def display_all(self):  # Method calling other methods
        print(f"Celsius: {self.celsius}°C")
        print(f"Fahrenheit: {self.to_fahrenheit():.2f}°F")
        print(f"Kelvin: {self.to_kelvin():.2f}K")

temp = TemperatureConverter(25)
temp.display_all()


# Example 4: Understanding self
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, I'm {self.name}!")
    
    def introduce(self, other_person):
        print(f"Hi {other_person.name}, I'm {self.name}!")

person1 = Person("Alice")
person2 = Person("Bob")

person1.greet()
person2.greet()
person1.introduce(person2)  


# Example 5: Methods returning values
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def circumference(self):
        import math
        return 2 * math.pi * self.radius
    
    def diameter(self):
        return 2 * self.radius

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area():.2f}")
print(f"Circumference: {circle.circumference():.2f}")
print(f"Diameter: {circle.diameter()}")


# Example 6: Methods modifying object state
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added: {task}")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Removed: {task}")
        else:
            print(f"Task not found: {task}")
    
    def show_tasks(self):
        print("Todo List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"  {i}. {task}")

todo = TodoList()
todo.add_task("Buy groceries")
todo.add_task("Write code")
todo.add_task("Exercise")
todo.show_tasks()
todo.remove_task("Write code")
todo.show_tasks()
