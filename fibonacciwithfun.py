# -*- coding: utf-8 -*-
"""fibonacciwithfun.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YPBPQBwePLAHSnO5ngz8grQPV4eydBof
"""

from typing import List

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = int(input("Enter the number of terms: "))
print(fibonacci(terms))