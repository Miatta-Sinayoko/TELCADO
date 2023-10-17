# Function to add two numbers, with a default value of 3 for y
def add(x, y=3):
    """Adds two numbers together and returns the sum.

    Args:
        x: The first number to add.
        y: The second number to add (optional, default value of 3).

    Returns:
        The sum of x and y.
    """

    result = x + y
    print(result)


# Calling the function with different arguments

# Case 1: x=5, y uses the default value of 3
add(5)  # Output: 8

# Case 2: x=5, y is explicitly set to 8
add(5, 8)  # Output: 13

# Case 3: Trying to call the function with only y, which is an error
# add(y=3)  # Error, missing x

# **Important to remember:**
# Default parameters must be assigned after non-default parameters.
# It is usually not a good practice to use variables as default values. This is because the default value can be accidentally modified, which can lead to unexpected behavior.

# **Refactored code to avoid using a variable as the default value:**

def add(x, y=3):
    """Adds two numbers together and returns the sum.

    Args:
        x: The first number to add.
        y: The second number to add (optional, default value of 3).

    Returns:
        The sum of x and y.
    """

    result = x + y
    print(result)


# Output:

add(5)  # Output: 8
add(5, 8)  # Output: 13

# **Additional notes:**

# The default value of `y` is assigned directly to the `y` parameter. This avoids the need to use a variable as the default value.
# It is important to note that the default value of `y` is only used if the `y` parameter is not explicitly passed to the function. For example, the call `add(5, 8)` will not use the default value of `y`, even though it is not explicitly passed to the function. This is because the `y` parameter is explicitly set to 8.
