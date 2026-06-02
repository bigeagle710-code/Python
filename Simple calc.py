def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!!")
    return x / y
def calculator():
    print("-----Function Calculator-----")
    print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide")
    try:
        choice = input("Enter choice (1/2/3/4):")
        if choice not in ['1','2','3','4']:
            print("invalid input!")
            return
        num1 = float(Input("Enter 1st no.:"))
        num2 = float(Input("Enter 2nd no.:"))
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")  
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")         
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
        print("Unexpected error!!")