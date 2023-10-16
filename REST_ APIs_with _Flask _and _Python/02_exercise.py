# Using f-strings to create a greeting with the name "Bob"
name = "Bob"
greeting = f"Hello, {name}"
print(greeting)

# Changing the name to "Rolf" and updating the greeting
name = "Rolf"
greeting = f"Hello, {name}"
print(greeting)

# --

# Setting a new name "Anne" and printing a greeting with it
name = "Anne"
print(f"Hello, {name}")

# -- Using .format() to create greetings --

# Creating a greeting template and replacing '{}' with "Rolf"
greeting = "Hello, {}"
with_name = greeting.format("Rolf")
print(with_name)

# Creating a longer phrase template and replacing '{}' with "Rolf" and "Monday"
longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
