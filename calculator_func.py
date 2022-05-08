"""
calculator.py is a module that calculates the value of 
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
        if (self.number2 == 0):
            print("Error, cannot divide an integer by 0!")
        else:
            return (self.number1 / self.number2)