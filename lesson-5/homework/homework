
# 1. Sort a Dictionary by Value
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary by value:", sorted_dict)

# 2. Add a Key to a Dictionary
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Dictionary after adding a key:", my_dict)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)
print("Concatenated dictionary:", dic1)

# Alternative method:
# new_dic = {**dic1, **dic2, **dic3}
# print("Concatenated dictionary (alternative):", new_dic)

# 4. Generate a Dictionary with Squares
n = 5
squares = {x: x * x for x in range(1, n + 1)}
print("Squares up to 5:", squares)

# 5. Dictionary of Squares (1 to 15)
squares_dict = {}
for x in range(1, 16):
    squares_dict[x] = x * x
print("Squares from 1 to 15:", squares_dict)


###################### SET EXERCISES ######################

# 1. Create a Set
my_set = {1, 2, 3, 4, 5}
print("Created set:", my_set)

# 2. Iterate Over a Set
my_set = {10, 20, 30, 40, 50}
print("Iterating set:")
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
# Add single item
my_set = {1, 2, 3}
my_set.add(4)
print("After adding one item:", my_set)

# Add multiple items
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print("After adding multiple items:", my_set)

# 4. Remove Item(s) from a Set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)      # Will raise error if 3 not found
my_set.discard(5)     # Will not raise error if 5 not found
print("After removing items:", my_set)

# 5. Remove an Item if Present in the Set
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    my_set.remove(3)
print("After conditionally removing 3:", my_set)

