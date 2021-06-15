# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:40:35 2021

 * LIST COMPREHENSIONS
 * LAMBDAS
 * GENERATORS
 * ITERATORS
 * CLOSURES

"""

"""
LIST COMPREHENSIONS

"""
x_squared = [item * item for item in range(1, 5)]
print(x_squared)

row = [1, 2, 3]
matrix = [[int(elem) + ((int(elem1)*2//3)*3) for elem in row]
          for elem1 in row]
print(matrix)

list_1 = [7, 2, 6, 2, 5, 4, 3]
list_2 = [x * x for x in list_1 if (x % 2 == 0)]
print(list_2)


"""
LAMBDAS
    * map() and filter() both return generators
"""
nums = [item for item in range(1, 11)]
squares = list(map(lambda x: x*x, nums))
print(squares)

odds = list(filter(lambda x: x % 2, nums))
print(odds)

evens = tuple(filter(lambda x: x % 2 == 0, nums))
print(evens)

"""
GENERATORS

"""
# Example 1: Generator Expression
for x in (el * 2 for el in range(5)):
    print(x, end=' ')


# Example 2: Generator Function
def gen(x):
    for i in range(x):
        yield i * 2


for q in gen(5):
    print(q, end=' ')


# Example 3: Generator Class
class CustomIter:
    def __init__(self, n):
        self.__n = n
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i == self.__n:
            raise StopIteration
        v = self.__i * 2
        self.__i += 1
        return v


for x in CustomIter(5):
    print(x, end=" ")


"""
CLOSURES
    * Closures return the object rather than
      the calling the function.
    * Benefits:
        - No need to use global variables. Provides
          data hiding.
        - If only one method, then easier programming
          versus classes.
        - Closures permit Python decorators.
        - Closures permit function invocation outside
          its scope.
"""


def to_the_power_of(n):
    def power(x):
        return x ** n
#   return power() <- WRONG
    return power  # Right, returning the object


# Sqaured
squared = to_the_power_of(2)

# Cubed
cubed = to_the_power_of(3)

# Output 64
print(squared(8))

# Output 64
print(cubed(4))
