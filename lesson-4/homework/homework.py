# 1. Sort a Dictionary by Value  ######## ???????????????

# 2. Add a Key to a Dictionary

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

# 3. Concatenate Multiple Dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# new_dic = {**dic1, **dic2, **dic3}
# print(new_dic)

# 4. Generate a Dictionary with Squares

n = 5
print({x: x * x for x in range(1, n + 1)})

# 5. Dictionary of Squares (1 to 15)

squares_dict = {}
for x in range(1, 16):
    squares_dict[x] = x * x

print(squares_dict)

###################### SET EXERCISES ######################

# 1. Create a Set

my_set = {1,2,3,4,5}
print(my_set)

# 2. Iterate Over a Set 

my_set = {10, 20, 30, 40, 50}

for item in my_set:
    print(item)

# 3. Add Member(s) to a Set

my_set = {1, 2, 3}
my_set.add(4)     ###############3 faqat 1ta son qo'shadi
print(my_set)


my_set = {1, 2, 3}
my_set.update([4, 5, 6])     ##################### ko'p son qo'shadi
print(my_set)

# 3. Remove Item(s) from a Set

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
# my_set.remove(10)  ############### bu holatda agar xatolik bo'lsa ko'rsatadi
my_set.discard(5)
# my_set.discard(10)   ###### bu holatda agar xatolik bo'lsa ko'rsatmaydi va bor natijani chiqarib beradi
print(my_set)

# 5. Remove an Item if Present in the Set

my_set = {1, 2, 3, 4, 5}

if 3 in my_set:
    my_set.remove(3)  

print(my_set)





