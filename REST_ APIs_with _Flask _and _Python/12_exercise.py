# Creating a list of squares for numbers 1, 3, and 5
numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# Dealing with strings - Filtering friends whose names start with "S"
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# Using a for loop to filter names that start with "S"
starts_s = []
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)
print(starts_s)

# Using list comprehension to achieve the same result
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

# Demonstrating that list comprehension creates a new list
friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# Printing the original list, the filtered list, and checking if they are the same object
print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))
