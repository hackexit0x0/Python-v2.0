# addition
Addition = lambda Userint1, Userint2: Userint1 + Userint2

# subtraction
Subtraction = lambda Userint1, Userint2: Userint1 - Userint2

# multiplication
Multiplication = lambda Userint1, Userint2: Userint1 * Userint2

# division
Division = lambda Userint1, Userint2: Userint1 / Userint2

# design
def design():
    print("- -"*6)

# function
def main():
    # user input
    Userint1 = input("Enter first number: ")
    if str(Userint1).upper() == "EXIT":
        print("Goodbye!")
        exit()
    #user input option oprator
    option = input("Enter operator: (+, -, *, /): ")
    # user input
    Userint2 = input("Enter second number: ")
    
    # if statement ccoll lambda function
    if option == "+":
        # addition output
        design()
        print("[+] Addition: ", Userint1, "+", Userint2, "=", Addition(Userint1, Userint2))
        print("[+] Total Value: ", Addition(Userint1, Userint2),"\n")
        # subtraction output
    elif option == "-":
        design()
        print("[+] Subtraction: ", Userint1, "-", Userint2, "=", Subtraction(Userint1, Userint2))
        print("[+] Total Value: ", Subtraction(Userint1, Userint2),"\n")
        # multiplication output
    elif option == "*":
        design()
        print("[+] Multiplication: ", Userint1, "*", Userint2, "=", Multiplication(Userint1, Userint2))
        print("[+] Total Value: ", Multiplication(Userint1, Userint2),"\n")
        # division output
    elif option == "/":
        design()
        print("[+] Division: ", Userint1, "/", Userint2, "=", Division(Userint1, Userint2))
        print("[+] Total Value: ", Division(Userint1, Userint2),"\n")
    else:
        print("Invalid input")
    


# while True:
while True:
    # call function
    main()
