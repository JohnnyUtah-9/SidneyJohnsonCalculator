from src import Addition
from src import Multiplication
from src import Square_Root
from src import Square
from src import Division
from src import Subtraction

class Calculator:
    result = 0

    def __init__(self):
        self.result = 1
        pass

    def add(self, a, b):
        self.result = Addition.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division.division(a, b)
        return self.result

    def square(self, a):
        self.result = Square.square(a)
        return self.result

    def square_root(self, a, b):
        self.result = Square_Root.sqrt(a, b)
        return self.result

