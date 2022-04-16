"""
Python Calculator calculates the value of 
adding, subtraction, mulitplication and division
of two user-input numbers

"""

#Calculator class constructor method
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1; 
        self.number2 = number2; 
    
    #addition() class method adds two numbers 
    def addition(self):
        return (self.number1 + self.number2)
    
    #subtraction() class method subtracts two numbers 
    def subtraction(self):
        return (self.number1 - self.number2)

    #mulitplication() class method multiplies two numbers 
    def multiplication(self):
        return (self.number1 * self.number2)
    
    #division() class method divides two numbers 
    def division(self):
        return (self.number1 - self.number2)


#first and second store the two user input integer numbers respectively
first = int(input("Enter the first number(MUST be an integer!): "))
second = int(input("Enter the second number(MUST be an integer!): "))

#create a Calculator object using user input integer numbers 
user_numbers = Calculator(first, second)

#initialize choice to equal 0 to ensure loop runs at least once
choice = 0  

#print while loop until user enters a five
while (choice != 5):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplicaiton")
    print("4. Division")
    print("5. Exiting calculator.py")

    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print("The addition of both numbers equals: ", user_numbers.addition())
    elif choice == 2:
        print("The subtraction of both numbers equals: ", user_numbers.subtraction())
    elif choice == 3:
        print("The multiplication of both numbers equals: ", user_numbers.multiplication())
    elif choice == 4:
        print("The division of both numbers equals: ", user_numbers.division())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")