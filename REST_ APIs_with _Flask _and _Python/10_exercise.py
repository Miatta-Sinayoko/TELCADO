# List of movies watched.
movies_watched = {"The Matrix", "Power Book IV", "Renfield"}

# Prompt the user for a movie they've watched recently.
user_movie = input("Enter something you've watched recently: ")

# Check if the user's movie is in the list and provide a response.
if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

# --

# Secret number game.
number = 7

# Prompt the user if they want to play.
user_input = input("Enter 'y' if you would like to play: ")

# Check if the user wants to play.
if user_input.lower() == "y":
    # Prompt the user to guess the number.
    user_number = int(input("Guess our number: "))

    # Check if the user's guess is correct or close.
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")
