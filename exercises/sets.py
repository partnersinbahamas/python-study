# Exercises
    # 1. Create an empty set and assign it to a variable.
    # 2. Add three items to your empty set using either several add calls, or a single call to update.
    # 3. Create a second set which includes at least one common element with the first set.
    # 4. Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
    # 5. Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.
    # If you want an extra challenge, also tell the user if their number was too high or too low.

new_set = set()

new_set.add(1)
new_set.update([2, 3])

other_set = set([2])

new_union = new_set.union(other_set)
new_difference = new_set.difference(other_set)
new_sym_difference = new_difference.symmetric_difference(other_set)
print(new_union, new_difference, new_sym_difference)


n_range = range (1, 11)
user_num = int(input("Enter number: "))

print(user_num in n_range)


