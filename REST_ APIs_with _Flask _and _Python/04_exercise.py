# Prompt the user for their age input.
user_age = input("Enter your age: ")

# Convert the user's age input to an integer.
age_number = int(user_age)

# Calculate the equivalent number of months for the given age.
months = age_number * 12

# Display the age in months.
print(f"{age_number} years is equal to {months} months.")
