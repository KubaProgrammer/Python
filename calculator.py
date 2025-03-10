def calculator():
    bool = True
    while bool:
        a = float(input("Give the firs number: "))
        b = float(input("Give the second number: "))
        print("\nWhat would you like to do?")
        print("1. Add;")
        print("2. Subtract;")
        print("3. Multiply;")
        print("4. Devide;")
        print("5. Abort.")
        operation = int(input())
        match operation:
            case 1: 
                print(f"{a} + {b} = {a + b}")
            case 2: 
                print(f"{a} - {b} = {a - b}")
            case 3: 
                print(f"{a} * {b} = {a * b}")
            case 4:
                while b == 0:
                    b = float(input("You cannot devide by 0. Choose another second number than 0.\n"))
                print(f"{a} / {b} = {a/b}")
            case 5: 
                bool = False
            case _: return "Unknown operation"

calculator()

