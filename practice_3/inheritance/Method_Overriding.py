# Example 1: Simple method overriding
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):  # Override parent's method
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    def speak(self):  # Override parent's method
        print(f"{self.name} meows: Meow!")

animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

animal.speak()  # Parent's method
dog.speak()  # Overridden method
cat.speak()  # Overridden method


# Example 2: Overriding with different behavior
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0  # Default implementation

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):  # Override with specific implementation
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self):  # Override with specific implementation
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"{circle.name} area: {circle.area():.2f}")
print(f"{rectangle.name} area: {rectangle.area()}")


# Example 3: Overriding __str__ method
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):  # Override built-in __str__
        return f"Product: {self.name}, Price: ${self.price}"

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author
    
    def __str__(self):  # Override __str__ with more details
        return f"Book: '{self.name}' by {self.author}, Price: ${self.price}"

product = Product("Generic Item", 10)
book = Book("Python Guide", 35, "John Doe")

print(product)  # Uses Product's __str__
print(book)  # Uses Book's __str__


# Example 4: Partial override (calling parent + adding functionality)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"Starting {self.brand} {self.model}...")
        print("Engine started")

class ElectricCar(Vehicle):
    def start(self):
        print(f"Starting electric {self.brand} {self.model}...")
        print("Battery check: OK")
        print("Electric motor started")  # Different implementation

class HybridCar(Vehicle):
    def start(self):
        super().start()  # Use parent's start
        print("Hybrid system activated")  # Add extra functionality

print("Regular vehicle:")
car = Vehicle("Toyota", "Camry")
car.start()

electric = ElectricCar("Tesla", "Model S")
electric.start()

hybrid = HybridCar("Toyota", "Prius")
hybrid.start()


# Example 5: Overriding with polymorphism
class PaymentMethod:
    def process_payment(self, amount):
        print(f"Processing ${amount} payment...")

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Credit Card")
        print("Card verified, payment approved")

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")
        print("PayPal account verified, payment sent")

class Crypto(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Cryptocurrency")
        print("Blockchain transaction initiated")

# Same method name, different implementations
payments = [CreditCard(), PayPal(), Crypto()]

for payment in payments:
    payment.process_payment(100)
    print()


# Example 6: Override with validation
class User:
    def __init__(self, username):
        self.username = username
    
    def set_email(self, email):
        self.email = email
        print(f"Email set to: {email}")

class SecureUser(User):
    def set_email(self, email):
        # Override with validation
        if '@' in email and '.' in email:
            super().set_email(email)
        else:
            print(f"Invalid email format: {email}")

user = User("alice123")
user.set_email("invalid-email")  # No validation

secure_user = SecureUser("bob456")
secure_user.set_email("invalid-email")  # Validation fails
secure_user.set_email("bob@email.com")  # Validation passes
