# Define a function to add two numbers and return the sum.
def add(x, y):
    """Adds two numbers together and returns the sum.

    Args:
        x: The first number to add.
        y: The second number to add.

    Returns:
        The sum of x and y.
    """
    return x + y

# Example usage:
print(add(5, 8))  # Prints 13
result = add(5, 8)  # Returns 13
print(result)

# Note that functions always return something, even if it's None.

# If we want to do something with the result of the function, we need to assign it to a variable or print it.

# For example, we can assign the result of the `add()` function to a variable and then print it:

result = add(2, 3)
print(result)  # Prints 5

# Or, we can simply print the result of the `add()` function directly:

print(add(5, 8))  # Prints 13

# We can also use the `add()` function in expressions:

print(10 + add(2, 3))  # Prints 15

# Returning terminates the function

# If we return from a function, the function will stop executing.

# For example, the following function will always return 10, even though it has a `print()` statement after the `return` statement:

def always_return_10():
    return 10
    print("This will never be printed")

print(always_return_10())  # Prints 10

# Returning with conditionals

# We can also use `return` statements with conditionals to control the flow of execution.

# For example, the following function will return the quotient of two numbers if the divisor is not zero, otherwise it will return the string "You fool!"

def divide(dividend, divisor):
    """Divides two numbers and returns the quotient.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        The quotient of dividend and divisor, or the string "You fool!" if the divisor is zero.
    """
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

print(divide(15, 3))  # Prints 5
print(divide(15, 0))  # Prints "You fool!"
