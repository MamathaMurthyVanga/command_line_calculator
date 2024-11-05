def add(x,y):
    return x+y


def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "cannot divide by zero"
    return x/y


def main():
    print("Welcome to command line calculator!")

    while True:
        print("\n Select Operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")


        choice = input("Enter choices (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: " ))

                if choice == "1":
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")   

                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

                elif choice == "4":
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

            except ValueError:
                print("Invalid input! please enter numbers only")

        elif choice == "5":
            print("Exiting the calculator")
            break

        else:
            print("Invalid choice. Please try again")



if __name__ == '__main__':
    main()




    