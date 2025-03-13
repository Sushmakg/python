Sushma K G 
"""day3task3.py
"""

def display():
  print("hello python!")
display()

def add():
  a=int(input("enter a"))
  b=int(input("enter b"))
  c=a+b
  print(c)
add()

#factorial with function
def fact():
  n=int(input("enter a number"))
  fact=1
  for i in range (1,n+1):
    fact=fact*i
  print(fact)
fact()

def isprime():
    n = int(input("Enter a number: "))
    if n < 2:
        print("Not prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")

isprime()

from typing import List
def fibonacci(n):
  sequence=[]
  a, b = 0,1
  for i in range(n):
    sequence.append(a)
    a , b = b , a+b
  return sequence

print(fibonacci(10))

def show():
  a=int(input("enter a"))
  b=int(input("enter b"))
  c=int(input(" enter c"))
  if a>b and a>c:
    print("a is greater")
  elif b>a and b>c:
      print("b is greater")
  else:
    print("c is greater")
show()

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))

def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    sum_of_digits = sum(int(digit) ** power for digit in num_str)
    return sum_of_digits == num

print(is_armstrong_number(153))
print(is_armstrong_number(123))

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))

def simple_calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

print(simple_calculator(5, 3, "+"))
print(simple_calculator(5, 0, "/"))

def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(is_even_or_odd(4))
print(is_even_or_odd(7))

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The GCD of", a, "and", b, "is:", find_gcd(a, b))

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The LCM of", a, "and", b, "is:", find_lcm(a, b))

def reverse_string(s):
    return s[::-1]

s = input("Enter a string: ")

print("The reversed string is:", reverse_string(s))

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

s = input("Enter a string: ")

print("The number of vowels in the string is:", count_vowels(s))

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = int(input("Enter a number: "))

print("The sum of digits is:", sum_of_digits(num))

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

name = input("Enter your name: ")
print(greet(name))
print(greet(name, "Hi"))

def sum_of_numbers(*args):
    return sum(args)

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

print("The sum of the numbers is:", sum_of_numbers(*numbers))

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25, city="New York")

import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
factorial = math.factorial(int(num)) if num.is_integer() and num >= 0 else "Factorial is not defined for non-integer or negative numbers"
sine_value = math.sin(math.radians(num))

print(f"Square root of {num} is: {square_root}")
print(f"Factorial of {int(num)} is: {factorial}")
print(f"Sine of {num} (in degrees) is: {sine_value}")

import random

def generate_random_number(start, end):
    return random.randint(start, end)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Random number between", start, "and", end, "is:", generate_random_number(start, end))

square = lambda x: x ** 2

num = float(input("Enter a number: "))
print("The square of", num, "is:", square(num))

tuples_list = [(1, 4), (3, 2), (5, 1), (2, 3)]

sorted_list = sorted(tuples_list, key=lambda x: x[1])

print("Sorted list based on second element:", sorted_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_even_numbers = map(lambda x: x ** 2, even_numbers)
result = list(squared_even_numbers)
print(result)

import mymath

x = 10
y = 5

print(f"{x} + {y} = {mymath.add(x, y)}")
print(f"{x} - {y} = {mymath.subtract(x, y)}")
print(f"{x} * {y} = {mymath.multiply(x, y)}")

10 + 5 = 15 
10 - 5 = 5 
10 * 5 = 50