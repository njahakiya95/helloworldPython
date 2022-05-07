import calculator

#first and second store the two user input integer numbers respectively
first = int(input("Enter the first number(MUST be an integer!): "))
second = int(input("Enter the second number(MUST be an integer!): "))

#create a Calculator object using user input integer numbers 
user_numbers = Calculator(first, second)

#initialize choice to equal 0 to ensure loop runs at least once
choice = 0 

#print while loop with menu of operator options 
while (choice != 5):
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplicaiton")
    print("4. Division")
    print("5. Exit\n")

    #try-except user input and store valid option in choice 
    try:
        choice = int(input("Enter the operation you would like to perform: "))
    except ValueError:
        print("ERROR: Invalid choice! Input must be integer between 1 and 5.\n")

    #if-else loop performs calculations based on the value of choice 
    if choice == 1:
        print("\nThe addition of both numbers equals: ", user_numbers.addition())
    elif choice == 2:
        print("\nThe subtraction of both numbers equals: ", user_numbers.subtraction())
    elif choice == 3:
        print("\nThe multiplication of both numbers equals: ", user_numbers.multiplication())
    elif choice == 4:
        print("\nThe division of both numbers equals: ", user_numbers.division())
    elif choice == 5:
        print("\nExiting!\n")
    else:
        print("ERROR: Invalid choice! Input must be integer between 1 and 5.\n")