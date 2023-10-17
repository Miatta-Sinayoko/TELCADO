# Function to greet the user
def print_greeting():
    """Prints a greeting to the user."""
    print("Hello, world!")

# Function to calculate user's age in seconds
def calculate_user_age_in_seconds():
    """Calculates the user's age in seconds.

    Returns:
        The user's age in seconds.
    """
    # Prompt the user for their age
    user_age = int(input("Enter your age: "))
    # Calculate age in seconds
    age_seconds = user_age * 365 * 24 * 60 * 60
    # Return the result
    return age_seconds

# List to store friends' names
friends = []

# Function to add a friend to the list
def add_friend(friend_name):
    """Adds a friend to the list.

    Args:
        friend_name: The name of the friend to add.
    """
    friends.append(friend_name)

# Greet the user and call the age calculation function
print("Welcome to the age in seconds program!")
user_age_in_seconds = calculate_user_age_in_seconds()
print(f"Your age in seconds is {user_age_in_seconds}.")
print("Goodbye!")

# Add a friend to the list and print the updated list
add_friend("Rolf")
print(friends)  # Prints the updated list of friends

# Call the say_hello function
print_greeting()
