%python
# ==============================================================================
# File Name: add_numbers.py
# Author: Surendra
# Date: 22 March 2025
# Description: This script provides functions to add and multiply two numbers 
#              and demonstrates their usage. The script is designed with proper 
#              documentation and comments.
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

def multiply_numbers(num1, num2):
    """
    Multiplies two numbers and returns their product.

    Parameters:
        num1 (float): The first number to be multiplied.
        num2 (float): The second number to be multiplied.

    Returns:
        float: The product of num1 and num2.

    Example:
        >>> multiply_numbers(5, 10)
        50
    """
    # Calculate the product of num1 and num2
    return num1 * num2

# Example usage of the add_numbers and multiply_numbers functions
if __name__ == "__main__":
    # Input: Two numbers to add and multiply
    number1 = 5
    number2 = 10

    # Call the add_numbers function and print the result
    sum_result = add_numbers(number1, number2)
    print(f"The sum of {number1} and {number2} is {sum_result}")

    # Call the multiply_numbers function and print the result
    product_result = multiply_numbers(number1, number2)
    print(f"The product of {number1} and {number2} is {product_result}")