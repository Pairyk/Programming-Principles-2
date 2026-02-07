# Example 1: Basic multiple inheritance
class Flyer:
    def fly(self):
        print("Flying in the air")

class Swimmer:
    def swim(self):
        print("Swimming in water")

class Duck(Flyer, Swimmer):  # Inherits from both
    def __init__(self, name):
        self.name = name

duck = Duck("Donald")
print(f"{duck.name} can:")
duck.fly()  # From Flyer
duck.swim()  # From Swimmer


# Example 2: Multiple inheritance with __init__
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        print(f"Engine: {horsepower}hp")

class GPS:
    def __init__(self, gps_type):
        self.gps_type = gps_type
        print(f"GPS: {gps_type}")

class SmartCar(Engine, GPS):
    def __init__(self, brand, horsepower, gps_type):
        self.brand = brand
        Engine.__init__(self, horsepower)
        GPS.__init__(self, gps_type)

car = SmartCar("Tesla", 450, "Advanced Navigation")
print(f"Car: {car.brand}, {car.horsepower}hp, {car.gps_type}")


# Example 3: Method Resolution Order (MRO)
class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):  # Inherits from both B and C
    pass

d = D()
d.method()  # Which method is called?
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")
# MRO: D -> B -> C -> A -> object


# Example 4: Diamond problem solution
class Device:
    def __init__(self, brand):
        self.brand = brand
        print(f"Device: {brand}")

class PhoneFeature:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        print(f"Phone: {phone_number}")
    
    def make_call(self):
        print(f"Calling from {self.phone_number}")

class CameraFeature:
    def __init__(self, megapixels):
        self.megapixels = megapixels
        print(f"Camera: {megapixels}MP")
    
    def take_photo(self):
        print(f"Taking photo with {self.megapixels}MP camera")

class Smartphone(Device, PhoneFeature, CameraFeature):
    def __init__(self, brand, phone_number, megapixels):
        Device.__init__(self, brand)
        PhoneFeature.__init__(self, phone_number)
        CameraFeature.__init__(self, megapixels)
        print("Smartphone initialized")

smartphone = Smartphone("iPhone", "555-0123", 12)
smartphone.make_call()
smartphone.take_photo()


# Example 5: Mixins (common multiple inheritance pattern)
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class XMLMixin:
    def to_xml(self):
        xml = "<object>"
        for key, value in self.__dict__.items():
            xml += f"<{key}>{value}</{key}>"
        xml += "</object>"
        return xml

class Person(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(f"JSON: {person.to_json()}")
print(f"XML: {person.to_xml()}")


# Example 6: Multiple inheritance with super()
class Base:
    def __init__(self):
        print("Base.__init__")

class Left(Base):
    def __init__(self):
        super().__init__()
        print("Left.__init__")

class Right(Base):
    def __init__(self):
        super().__init__()
        print("Right.__init__")

class Child(Left, Right):
    def __init__(self):
        super().__init__()
        print("Child.__init__")
        
print("Constructor call order with super():")
child = Child()
print(f"MRO: {[cls.__name__ for cls in Child.__mro__]}")
