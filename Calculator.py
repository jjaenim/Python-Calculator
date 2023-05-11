# Joshua Adrian O. Daet
# BSCpE 1-4
# Python Caluclator

# Operation Methods
def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\033[1;31mInvalid input! Please enter a valid number.\033[0m")