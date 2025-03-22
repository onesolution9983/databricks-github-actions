# ==============================================================================
# File Name: add_numbers.py
# Author: Surendra
# Date: 22 March 2025
# Description: This script provides a function to add two numbers and demonstrates 
#              its usage. The script is designed with proper documentation and comments.
# ==============================================================================

def add_numbers(num1, num2):
    """
    Adds two numbers and returns their sum.

    Parameters:
        num1 (float): The first number to be added.
        num2 (float): The second number to be added.

    Returns:
        float: The sum of num1 and num2.

    Example:
        >>> add_numbers(5, 10)
        15
    """
    # Calculate the sum of num1 and num2
    return num1 + num2

# Example usage of the add_numbers function
if __name__ == "__main__":
    # Input: Two numbers to add
    number1 = 5
    number2 = 10

    # Call the function and print the result
    result = add_numbers(number1, number2)
    print(f"The sum of {number1} and {number2} is {result}")
