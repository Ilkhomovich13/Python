### 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). 
# Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

print(is_prime(4))  
print(is_prime(7))  


### 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, 
# u k sonining raqamlari yig'indisini hisoblaydi.

def digit_sum(k):
    return sum(int(digit) for digit in str(k))  

print(digit_sum(24))  
print(digit_sum(502)) 

### 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini 
# (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def powers_of_two(N):
    power = 2
    while power <= N:
        print(power, end=" ")
        power *= 2


powers_of_two(10)  
