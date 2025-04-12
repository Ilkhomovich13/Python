
# 1. Modify String with Underscores
def insert_underscores(txt):
    result = []
    i = 0
    count = 0
    vowels = "aeiouAEIOU"

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            if i+1 < len(txt) and (txt[i+1] in vowels or txt[i+1] == '_'):
                result.append(txt[i+1])
                i += 1
            result.append('_')
            count = 0
        i += 1

    if result and result[-1] == '_':
        result.pop()

    return ''.join(result)

print("1.1", insert_underscores("hello"))              # hel_lo
print("1.2", insert_underscores("assalom"))            # ass_alom
print("1.3", insert_underscores("abcabcabcdeabcdefabcdefg"))  # qisqaroq natija



# 2. Integer Squares
print("2.")
n = 5
for i in range(n):
    print(i ** 2)



# 3.1 Print first 10 natural numbers using a while loop
print("3.1")
i = 1
while i <= 10:
    print(i)
    i += 1

# 3.2 Triangle pattern
print("3.2")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# 3.3 Sum of numbers from 1 to n
print("3.3")
n = 10
total = 0
for i in range(1, n+1):
    total += i
print("Sum is:", total)

# 3.4 Multiplication table of a number
print("3.4")
num = 2
for i in range(1, 11):
    print(num * i)

# 3.5 Display numbers from list using loop
print("3.5")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 70 < num < 500:
        print(num)

# 3.6 Count digits in a number
print("3.6")
number = 75869
print("Digits:", len(str(number)))

# 3.7 Reverse number pattern
print("3.7")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# 3.8 Print list in reverse order
print("3.8")
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# 3.9 Display numbers from -10 to -1
print("3.9")
for i in range(-10, 0):
    print(i)

# 3.10 Display “Done” after loop
print("3.10")
for i in range(5):
    print(i)
else:
    print("Done!")

# 3.11 Print all prime numbers in range
print("3.11")
for num in range(25, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# 3.12 Fibonacci series up to 10 terms
print("3.12")
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# 3.13 Factorial of a number
print("3.13")
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")


# 4. Uncommon elements of lists
def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for key in c1:
        if key not in c2:
            result.extend([key] * c1[key])
    for key in c2:
        if key not in c1:
            result.extend([key] * c2[key])

    return result

print("4.1", uncommon_elements([1, 1, 2], [2, 3, 4]))             # [1, 1, 3, 4]
print("4.2", uncommon_elements([1, 2, 3], [4, 5, 6]))             # [1, 2, 3, 4, 5, 6]
print("4.3", uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) # [2, 2, 5]


