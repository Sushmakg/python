  # Taking input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Using if-elif-else to find the largest
if a >= b and a >= c:
    print(f"The largest number is {a}")
elif b >= a and b >= c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")

output
Enter first number: 5
Enter second number: 8
Enter third number: 3
The largest number is 8
