# **While loop to play a number guessing game:**
def play_number_guessing_game():
    """Plays a number guessing game with the user.

    The user is given a chance to guess a secret number. If they guess correctly,
    they win. Otherwise, they are given a clue and asked to guess again.

    Returns:
        None
    """

    # Generate a secret number
    number = 7

    # Ask the user if they want to play
    play = input("Would you like to play? (Y/n) ")

    # Keep playing while the user wants to play
    while play.lower() != "n":

        # Get the user's guess
        user_number = int(input("Guess our number: "))

        # Check if the user guessed correctly
        if user_number == number:
            print("You guessed correctly!")
            break

        # Give the user a clue
        elif abs(number - user_number) == 1:
            print("You were off by 1.")
        else:
            print("Sorry, it's wrong!")

        # Ask the user if they want to play again
        play = input("Would you like to play again? (Y/n) ")

# **The break keyword to exit a loop:**
def play_number_guessing_game_with_break():
    """Plays a number guessing game with the user.

    The user is given a chance to guess a secret number. If they guess correctly,
    they win. Otherwise, they are given a clue and asked to guess again.

    Returns:
        None
    """

    # Generate a secret number
    number = 7

    # Keep playing while the user wants to play
    while True:

        # Ask the user if they want to play
        play = input("Would you like to play? (Y/n) ")

        # Exit the loop if the user doesn't want to play
        if play.lower() == "n":
            break

        # Get the user's guess
        user_number = int(input("Guess our number: "))

        # Check if the user guessed correctly
        if user_number == number:
            print("You guessed correctly!")
            break

        # Give the user a clue
        elif abs(number - user_number) == 1:
            print("You were off by 1.")
        else:
            print("Sorry, it's wrong!")

# **For loop to iterate through a list of friends:**
def print_friends(friends):
    """Prints a list of friends to the console.

    Args:
        friends: A list of friends.

    Returns:
        None
    """

    for friend in friends:
        print(f"{friend} is my friend.")

# **For loop to calculate the average of a list of grades:**
def calculate_average_grade(grades):
    """Calculates the average of a list of grades.

    Args:
        grades: A list of grades.

    Returns:
        The average of the grades.
    """

    total = sum(grades)
    amount = len(grades)

    return total / amount

# **Note:** Searching for Python functions and concepts is a valuable skill.


# **Example usage:**

# Play the number guessing game
play_number_guessing_game()

# Play the number guessing game with the break keyword
play_number_guessing_game_with_break()

# Print a list of friends
friends = ["Rolf", "Jen", "Bob", "Anne"]
print_friends(friends)

# Calculate the average of a list of grades
grades = [35, 67, 98, 100, 100]
average_grade = calculate_average_grade(grades)

# Print the average grade
print(average_grade)
