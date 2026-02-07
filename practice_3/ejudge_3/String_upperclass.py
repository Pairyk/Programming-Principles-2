class StringHandler():
    def __init__(self):
        self.value = self.getString()

    def getString(self):
        return input()
    
    def printString(self):
        print(self.value.upper())

s = StringHandler()
s.printString()

