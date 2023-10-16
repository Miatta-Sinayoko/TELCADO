# Lists, Tuples, and Sets containing names.
names_list = ["Bob", "Rolf", "Anne"]
names_tuple = ("Bob", "Rolf", "Anne")
names_set = {"Bob", "Rolf", "Anne"}

# Accessing individual items in lists and tuples by their position.
print(names_list[0])
print(names_tuple[0])

# Sets don't support positional access as they are unordered.
# print(names_set[0])  # This would result in an error due to the lack of ordering in sets.

# Modifying individual items in lists using their index.
names_list[0] = "Smith"

# Tuples are "immutable," so trying to change an element will result in an error.
# names_tuple[0] = "Smith"

print(names_list)
print(names_tuple)

# Adding a new name to a list using `.append`.
names_list.append("Jen")
print(names_list)

# Tuples cannot be modified after creation, so appending is not possible.
# Tuples are "immutable."

# Adding a new name to a set using `.add`.
names_set.add("Jen")
print(names_set)

# Sets automatically handle unique elements, so adding "Bob" again won't change the set.
names_set.add("Bob")
print(names_set)
