# Define a function to add two numbers
def add(x, y):
    """Adds two numbers together and returns the sum.

    Args:
        x: The first number to add.
        y: The second number to add.

    Returns:
        The sum of x and y.
    """
    return x + y

# Print the sum of 5 and 7
print(add(5, 7))

# Define a lambda function to add two numbers
add_lambda = lambda x, y: x + y

# Print the sum of 5 and 7 using the lambda function
print(add_lambda(5, 7))

# Create a sequence of numbers
sequence = [1, 3, 5, 9]

# Double the elements of the sequence using a lambda function with the `map()` function
doubled = map(lambda x: x * 2, sequence)

# Print the doubled list
print(list(doubled))

# **Important to remember:**

# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# They are almost always single-line, so don't do anything complicated in them.
# It is very often better to just define a function and give it a proper name.
