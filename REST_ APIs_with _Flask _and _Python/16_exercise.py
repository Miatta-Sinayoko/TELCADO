# Define a function to add two numbers
def add(x, y):
    """Adds two numbers together and returns the sum.

    Args:
        x: The first number to add.
        y: The second number to add.

    Returns:
        The sum of x and y.
    """
    result = x + y
    print(result)


# Call the add() function with two positional arguments
add(2, 3)  # 5


# Define a function to greet someone
def say_hello(name=None):
    """Prints a greeting to the console.

    Args:
        name: The name of the person to greet. If None, prints a generic greeting.

    Returns:
        None.
    """
    if name is None:
        print("Hello!")
    else:
        print(f"Hello, {name}!")


# Call the say_hello() function with a named argument
say_hello(name="Bob")  # Hello, Bob!


# Call the say_hello() function without any arguments
say_hello()  # Hello!


# Define a function to divide two numbers
def divide(dividend, divisor):
    """Divides two numbers and prints the result to the console.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        None.
    """
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


# Call the divide() function with two positional arguments
divide(dividend=15, divisor=3)  # 5.0


# Call the divide() function with two positional arguments and one named argument
divide(15, 0, divisor=0)  # You fool!


# **Note:** Named arguments must go after positional arguments.
