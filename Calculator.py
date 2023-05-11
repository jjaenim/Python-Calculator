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

# Asks the user to choose what math operation will be used (Addition, Subtraction, Multiplication and Division)
operations = {
    1: ("(+) Addition", add),
    2: ("(-) Subtraction", subtract),
    3: ("(x) Multiplication", multiply),
    4: ("(/) Division", divide),
}
response = "Y"
while response == "Y":
    print("Choose an operation:")
    for operation_num, (operation_name, _) in operations.items():
        print(f"({operation_num}) {operation_name}")

    while True:
        try:
            operation = int(input("Enter 1 / 2 / 3 / 4: "))
            if operation not in operations:
                raise ValueError("\033[1;31mInvalid operation! Please enter a valid operation number (1-4).\033[0m")
            break
        except ValueError as error:
                print(error)