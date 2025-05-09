# 1.  Print the third fruit

fruits = ["olma", "banan", "gilos", "anor", "shaftoli"]
print(fruits[2])

# 2. Concatenate Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

concatenated = list1 + list2
print(concatenated)

# 3. Extract Elements from a List

numbers = [10, 20, 30, 40, 50, 60, 70]

first_element = numbers[0]
middle_element = numbers[len(numbers) // 2]  
last_element = numbers[-1]

extracted_elements = [first_element, middle_element, last_element]
print(extracted_elements)

# 4. Convert List to Tuple

favorite_movies = ["Inception", "Interstellar", "The Matrix", "The Dark Knight", "Gladiator"]


movies_tup = tuple(favorite_movies)
print(movies_tup)

# 5. Check Element in a List

cities = ["London", "New York", "Tokyo", "Paris", "Dubai"]

citydaparisbormi = "Paris" in cities
print(citydaparisbormi)

if "Paris" in cities:
    print("Bor")
else:
    print("Yo'q")

# 6. Duplicate a List Without Using Loop

numbers = [1, 2, 3, 4, 5]

duplicated = numbers * 2
print(duplicated)

# 7. Swap First and Last Elements of a List

numbers = [10, 20, 30, 40, 50]

numbers = numbers[::-1]

print(numbers)

# 8. Slice a Tuple

num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

sliced_tup = num_tuple [2:7]
print(sliced_tup)

# 9. Count Occurrences in a List

colors = ["red", "blue", "green", "blue", "yellow", "blue", "black"]

print(colors.count("blue"))

# 10. Find the Index of an Element in a Tuple

animals = ("cat", "dog", "elephant", "lion", "tiger", "bear")

print(animals.index("lion"))

# 11. Merge Two Tuples

tup1 = (1, 2, 3, 4, 5)
tup2 = (6, 7, 8, 9, 10)

print(tup1+tup2)

# 12. Find the Length of a List and Tuple

num_list = [10, 20, 30, 40, 50]
num_tuple = (1, 2, 3, 4, 5, 6, 7)

print(len(num_list), len(num_tuple))

# 13. Convert Tuple to List

num_tup = (1, 2, 3, 4, 5)
print(list(num_tup))

# 14. Find Maximum and Minimum in a Tuple

num = (15, 8, 22, 35, 4, 19)
print(max(num), min(num))

# 15. Reverse a Tuple

words = ("apple", "banana", "cherry", "date", "elderberry")
print(words[::-1])

