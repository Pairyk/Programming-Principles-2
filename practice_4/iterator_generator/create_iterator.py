# ============================================================================
# TOPIC 3: CREATE AN ITERATOR
# ============================================================================

# Example 1: Simple iterator class
print("\n1. Iterator class counting up to N")
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = CountUp(3)
for num in counter:
    print(f"Count: {num}")


# Example 2: Iterator for Fibonacci sequence
print("\n2. Fibonacci iterator")
class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a <= self.limit:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result
        else:
            raise StopIteration

fib = Fibonacci(20)
print(f"Fibonacci numbers up to 20: {list(fib)}")


# Example 3: Iterator that reverses a list
print("\n3. Reverse iterator class")
class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

reverse = ReverseList([10, 20, 30, 40])
print(f"Reversed: {list(reverse)}")


# Example 4: Iterator that filters even numbers
print("\n4. Iterator that filters even numbers")
class EvenNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration

evens = EvenNumbers([1, 2, 3, 4, 5, 6, 7, 8])
print(f"Even numbers: {list(evens)}")


# Example 5: Iterator for string repetition
print("\n5. Iterator that repeats a string N times")
class RepeatString:
    def __init__(self, text, times):
        self.text = text
        self.times = times
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.times:
            self.count += 1
            return self.text
        raise StopIteration

repeater = RepeatString("Hello", 3)
for msg in repeater:
    print(f"Message: {msg}")


# Example 6: Iterator for dictionary values with transformation
print("\n6. Iterator that transforms dictionary values")
class DoubleValues:
    def __init__(self, dictionary):
        self.items = list(dictionary.items())
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.items):
            key, value = self.items[self.index]
            self.index += 1
            return key, value * 2
        raise StopIteration

prices = {'apple': 1, 'banana': 2, 'cherry': 3}
doubled = DoubleValues(prices)
print(f"Doubled prices: {list(doubled)}")