# While loop to play a number guessing game.
number = 7
play = input("Would you like to play? (Y/n) ")

while play.lower() != "n":  # Convert the input to lowercase for case-insensitive comparison.
    user_number = int(input("Guess our number: "))

    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")

    play = input("Would you like to play again? (Y/n) ")

# The break keyword to exit a loop.
while True:
    play = input("Would you like to play? (Y/n) ")

    if play.lower() == "n":  # Convert the input to lowercase for case-insensitive comparison.
        break  # Exit the loop

    user_number = int(input("Guess our number: "))

    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")

# For loop to iterate through a list of friends.
friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")

# For loop to calculate the average of a list of grades.
grades = [35, 67, 98, 100, 100]
total = sum(grades)  # Use the sum() function to calculate the total.
amount = len(grades)  # Calculate the number of grades.

print(total / amount)  # Calculate and print the average.

# Note: Searching for Python functions and concepts is a valuable skill.
