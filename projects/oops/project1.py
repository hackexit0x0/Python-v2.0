class Myfunction:
    def __init__(self):
         print("Welcome to Python OOP Calculator")

    def UserInput(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def addition(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2
    
    def line(self):
         print("-----"*5)

    def exute(self):
        while True:
            option = str(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\nEnter your choice: "))
            if option == "5":
                print("Exiting the calculator. Goodbye!")
                exit()
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            self.UserInput(num1, num2)

            if option == "1":
                self.line()
                print("Your Input:", num1, "+", num2)
                print("Result:", self.addition())
                self.line()
            elif option == "2":
                self.line()
                print("Your Input:", num1, "-", num2)
                print("Result:", self.subtraction())
                self.line()
            elif option == "3":
                self.line()
                print("Your Input:", num1, "*", num2)
                print("Result:", self.multiplication())
                self.line()
            elif option == "4":
                print("Your Input:", num1, "/", num2)
                print("Result:", self.division())
            else:
                print("Invalid choice. Please choose a valid option.")



exuted = Myfunction()
exuted.exute()