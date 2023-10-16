# Get user's name and print it
name = input("Enter your name: ")
print(name)

# -- Perform math on user's input --

# Get the size of the house in square feet from the user
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)  # Convert user input to an integer
square_metres = square_feet / 10.8  # Calculate square meters (approximate conversion)
print(f"{square_feet} square feet is approximately {square_metres:.2f} square meters.")
