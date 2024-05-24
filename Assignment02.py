# WAP to Create a simple calculator which can perform simple arithmetic operations like add, subtract, division, multiplication etc
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y

while True:
    print("\n----Select operation----")
    print("1.Add\t 2.Subtract\t 3.Multiply\t 4.Divide\t 5. Exit")
    choice = input("\nEnter your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid Input")