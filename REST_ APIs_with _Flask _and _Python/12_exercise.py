# Create a list of squares for the numbers 1, 3, and 5 using list comprehension
squares = [x * x for x in [1, 3, 5]]

# Filter the friends list to only include friends whose names start with "S" using list comprehension
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# Print the filtered list
print(starts_s)

# Demonstrate that list comprehension creates a new list
friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# Print the original and filtered lists and their object IDs to show that they are different objects
print(friends)
print(starts_s)
print(friends is starts_s)
print(f"friends: {id(friends)} starts_s: {id(starts_s)}")
