import unittest
from Calculator import Calculator
from Csv_Reader import Csv_Reader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition_calculator(self):
        test_data = Csv_Reader("src/TestData/Addition.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction_calculator(self):
        test_data = Csv_Reader("src/TestData/Subtraction.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication_calculator(self):
        test_data = Csv_Reader("src/TestData/Multiplication.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division_calculator(self):
        test_data = Csv_Reader("src/TestData/Division.csv").data
        for row in test_data:
            result = round(float(row['Result']), 7)
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_calculator(self):
        test_data = Csv_Reader("src/TestData/Square.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.sqr(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt_method_calculator(self):
        test_data = Csv_Reader("src/TestData/SquareRoot.csv").data
        for row in test_data:
            result = round(float(row['Result']), 7)
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()

"""#x = Square.square(10)
#print("The square of 10 is: ", x)

#y = Subtraction.subtraction(10, 20)
#print('Y is equal to: ', y)

#mySquare = Square
#h = mySquare.square(7)
#print('h = ', h)
#print('mySquare is : ', mySquare)

#z = Square.square(5) - (Subtraction.subtraction(12, 25))
#print('This is a squared number subtracted by a number from another number:  ', z)

#sidney = Square.square((5 - Subtraction.subtraction(1, 4)))
#print('sidney\'s name equals: ', sidney)
# class MyTestCase(unittest.TestCase):
#   def test_something(self):
#       self.assertEqual(1, 1)

# if __name__ == '__main__':
#   unittest.main()"""
