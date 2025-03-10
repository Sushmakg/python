
# A simple Python program that uses indentation

def greet_user():
    name = input("Enter your name: ")  # Indented inside the function
    age = int(input("Enter your age: "))  # Indented inside the function
    print("Hello, " + name + "!")  # Indented inside the function
    print("You are " + str(age) + " years old.")  # Indented inside the function

# Calling the function to greet the user
greet_user()  # No indentation needed here as it's at the root level
