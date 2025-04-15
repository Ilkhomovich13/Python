# ##2. Integer Squares Exercise. Task. The provided code stub reads an integer, 
### , from STDIN. For all non-negative integers where , print .ni0 <= i < ni^2

n = int(input())

for i in range(n):
    print(i ** 2)


### 3. Loop-Based Exercises

### Exercise 1: Print first 10 natural numbers using a while loop

i = 1

while i <= 10:
    print(i)
    i += 1

###  Exercise 2: Print the following pattern

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()  
    i += 1

### Exercise 3: Calculate sum of all numbers from 1 to a given number

num = int(input("Enter number: "))

i = 1
total = 0

while i <= num:
    total += i
    i += 1

print("Sum is:", total)

### Exercise 4: Print multiplication table of a given number

num = int(input("Enter number: "))

i = 1
while i <= 10:
    print(num * i)
    i += 1

### Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num>50 and num<180:
        print(num)

### Exercise 6: Count the total number of digits in a number

number = input("Enter a number: ")
print("Total number of digits:", len(number))


### Exercise 7: Print reverse number pattern

rows = 5

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()  

### Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for item in reversed(list1):
    print(item)

### Exercise 9: Display numbers from -10 to -1 using a for loop

for num in range(-10, 0):
    print(num)

### Exercise 10: Display message “Done” after successful loop execution

for num in range(5):  
    print(num)

print("Done")

