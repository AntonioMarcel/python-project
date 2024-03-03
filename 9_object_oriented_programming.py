class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return sum((self.x, self.y))

    def subtract(self):
        return self.x - self.y

    def divide(self):
        return self.x / self.y

    def multiply(self):
        return self.x * self.y

    # def __str__(self):  # for printing object (for users)
    #     return f"I'm a Calculator and I will perform the selected operation on {self.x} and {self.y}."

    def __repr__(self):  # for representing object (debugging purposes for programmers)
        return f"<Calculator({self.x},{self.y})>"


calc = Calculator(1, 2)
print(calc)
