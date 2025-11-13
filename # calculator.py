def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2

def divide(n1, n2):
    """
    Divides two numbers.
    Includes a check for division by zero.
    """
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

def calculator():
    """Main function to run the command-line calculator"""
    
    print("---------------------------------")
    print(" Welcome to the Python CLI Calculator ")
    print("---------------------------------")
    
    # --- 3. Loop until user chooses to exit ---
    while True:
        # Display operation choices
        print("\nPlease select an operation:")
        print("  1. Add (+)")
        print("  2. Subtract (-)")
        print("  3. Multiply (*)")
        print("  4. Divide (/)")
        print("  5. Exit")
        
        # --- 2. Take user input ---
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if user wants to exit
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break  # Exits the while loop

        # Check if the choice is one of the valid operations
        if choice in ('1', '2', '3', '4'):
            try:
                # Get the numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            
            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter numbers only.")
                continue  # Skips the rest of the loop and asks for a new choice

            # --- 1. Use functions for each operation ---
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        
        else:
            # Handle invalid menu choices (e.g., '6', 'a', etc.)
            print("Invalid choice. Please select an option from 1 to 5.")

# Standard Python entry point
if __name__ == "__main__":
    calculator()
