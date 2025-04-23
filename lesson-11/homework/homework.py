def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nolga bo'lish mumkin emas"
    return a / b


print("Qo'shish:", add(2, 3))
print("Ayirish:", subtract(5, 2))
print("Ko'paytirish:", multiply(4, 3))
print("Bo'lish:", divide(10, 2))
print("Bo'lish:", divide(10, 0))

def reverse_string(text):
    return text[::-1]

print("So'zning teskarisi:", reverse_string("hello"))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print("Unlilar soni:", count_vowels("education"))



def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


write_file("example.txt", "Salom, bu faylga yozilgan matn!")
print("File yozildi!")
