"""UnitTest"""
import Square
import Subtraction

x = Square.square(10)
print("The square of 10 is: ", x)

y = Subtraction.subtraction(10, 20)
print('Y is equal to: ', y)

mySquare = Square
h = mySquare.square(7)
print('h = ', h)
print('mySquare is : ', mySquare)

z = Square.square(5) - (Subtraction.subtraction(12, 25))
print('This is a squared number subtracted by a number from another number:  ', z)

sidney = Square.square((5 - Subtraction.subtraction(1, 4)))
print('sidney\'s name equals: ', sidney)
# class MyTestCase(unittest.TestCase):
#   def test_something(self):
#       self.assertEqual(1, 1)

# if __name__ == '__main__':
#   unittest.main()

