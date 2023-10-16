# -- Finding Local Friends --

# We have a set of friends and a set of friends abroad.
# To find friends who are local, we can use `.difference`.

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local = friends.difference(abroad)
print(local)

# This returns an empty set because there are no friends abroad that are not in our main set.

print(abroad.difference(friends))

# -- Combining Friend Lists --

# We have a set of local friends and a set of friends abroad.
# To create a complete list of friends, we can use `.union`.

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)

# -- Finding Common Students --

# We have two sets of students, one for art and one for science.
# To find students who are in both classes, we can use `.intersection`.

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)
