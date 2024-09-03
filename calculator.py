def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def divide(x, y):
      if y == 0:
        return "Invalid value for denominator, can't divide by 0!"
      else:
         return x / y

def multiply(x, y):
    return x*y


def square(x):
    return x*x


def power(x, y):
    return x**y


def sqrt(x):
     import math
     if x < 0:
       return "Square root is not defined for negative numbers."
     else:
       return math.sqrt(x)
