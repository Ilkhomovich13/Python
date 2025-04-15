### 1. Write a Python program to handle a ZeroDivisionError 
# exception when dividing a number by zero.

try:
    num = 10
    print("Natija: ", num / 0)
except ZeroDivisionError:
    print("Xato: Nolga bo'lish mumkin emas.")

### 2. Write a Python program that prompts the user to input an integer and raises a ValueError 
# exception if the input is not a valid integer.

try:
    number = int(input("Iltimos, butun son kiriting: "))
except ValueError:
    print("Xato! Bu kiritilgan qiymat butun son emas. Iltimos, faqat son kiriting.")

### 3. Write a Python program that opens a file and handles a FileNotFoundError 
# exception if the file does not exist.

try:
    with open('non_existent_file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Xato: Fayl topilmadi. Iltimos, faylni tekshirib ko'ring.")

### 4. Write a Python program that prompts the user to input two numbers and raises a TypeError 
# exception if the inputs are not numerical.

try:
    a = input("Birinchi sonni kiriting: ")
    b = input("Ikkinchi sonni kiriting: ")
    print("Yig'indi: ", float(a) + float(b))
except ValueError:  # float() bo'lgani uchun ValueError kutiladi
    raise TypeError("Xato! Iltimos, faqat raqam kiriting.")

### 5. Write a Python program that opens a file and handles a PermissionError 
# exception if there is a permission issue.

try:
    with open('/root/secret.txt', 'r') as f:
        print(f.read())
except PermissionError:
    print("Ruxsat etilmagan. Faylni ochish uchun ruxsat yo'q.")

### 6. Write a Python program that executes an operation on a list and handles an IndexError 
# exception if the index is out of range.

try:
    lst = [1, 2, 3]
    print("Ro'yxatdagi element:", lst[10])  # IndexError chiqadi
except IndexError:
    print("Xato! Kiritilgan indeks ro'yxatda mavjud emas.")

### 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt 
# exception if the user cancels the input.

try:
    num = input("Son kiriting: ")
except KeyboardInterrupt:
    print("\nXato: Foydalanuvchi inputni bekor qildi.")

### 8. Write a Python program that executes division and handles an ArithmeticError 
# exception if there is an arithmetic error.

try:
    result = 1 / 0
except ArithmeticError:
    print("Aritmetik xato yuz berdi! Nolga bo'lish mumkin emas.")

########################################################################################################


### 1. Write a Python program to read an entire text file.

try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Fayl topilmadi.")

### 2. Write a Python program to read first n lines of a file.

n = int(input("Nechta satr o'qimoqchisiz? "))
try:
    with open('example.txt', 'r') as file:
        for _ in range(n):
            print(file.readline(), end='')
except FileNotFoundError:
    print("Fayl topilmadi.")

### 3. Write a Python program to append text to a file and display the text.



### 4. Write a Python program to read last n lines of a file.



### 5. Write a Python program to read a file line by line and store it into a list.

try:
    with open('example.txt', 'r') as file:
        lines = file.readlines()
    print("Fayldagi barcha satrlar:", lines)
except FileNotFoundError:
    print("Fayl topilmadi.")

### 6. Write a Python program to read a file line by line and store it into a variable.

try:
    with open('example.txt', 'r') as file:
        content = ""
        for line in file:
            content += line
    print("Fayldagi barcha matn:", content)
except FileNotFoundError:
    print("Fayl topilmadi.")

### 7. Write a Python program to read a file line by line and store it into an array.

try:
    with open('example.txt', 'r') as file:
        lines = [line.strip() for line in file]
    print("Fayldagi barcha satrlar:", lines)
except FileNotFoundError:
    print("Fayl topilmadi.")


### 8. Write a Python program to find the longest words.

try:
    with open('example.txt', 'r') as file:
        words = file.read().split()
    longest_word = max(words, key=len)
    print("Eng uzun so'z:", longest_word)
except FileNotFoundError:
    print("Fayl topilmadi.")

### 9. Write a Python program to count the number of lines in a text file.

try:
    with open('example.txt', 'r') as file:
        lines = file.readlines()
    print("Fayldagi satrlar soni:", len(lines))
except FileNotFoundError:
    print("Fayl topilmadi.")

### 10. Write a Python program to count the frequency of words in a file.

try:
    with open('example.txt', 'r') as file:
        words = file.read().split()
    word_count = {word: words.count(word) for word in set(words)}
    print("So'zlarning chastotasi:", word_count)
except FileNotFoundError:
    print("Fayl topilmadi.")

### 11. Write a Python program to get the file size of a plain file.

import os

try:
    file_size = os.path.getsize('example.txt')
    print("Faylning hajmi:", file_size, "bayt")
except FileNotFoundError:
    print("Fayl topilmadi.")

### 12. Write a Python program to write a list to a file.

data = ["Birinchi satr", "Ikkinchi satr", "Uchinchi satr"]
try:
    with open('output.txt', 'w') as file:
        for line in data:
            file.write(line + '\n')
    print("Ro'yxat faylga yozildi.")
except FileNotFoundError:
    print("Fayl topilmadi.")

### 13. Write a Python program to copy the contents of a file to another file.

try:
    with open('example.txt', 'r') as file:
        content = file.read()
    with open('copy_example.txt', 'w') as file:
        file.write(content)
    print("Fayl muvaffaqiyatli nusxalandi.")
except FileNotFoundError:
    print("Fayl topilmadi.")

### 14. Write a Python program to combine each line from the first file with the corresponding 
# line in the second file.



### 15. Write a Python program to read a random line from a file.



### 16. Write a Python program to assess if a file is closed or not.

try:
    file = open('example.txt', 'r')
    print("Fayl ochildi:", file.closed)
    file.close()
    print("Fayl yopildi:", file.closed)
except FileNotFoundError:
    print("Fayl topilmadi.")

### 17. Write a Python program to remove newline characters from a file.

