# 1. Circle Class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(5)
print("Yuzasi:", circle.area())  
print("Perimetri:", circle.perimeter()) 

# 2. Person Class

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date

    def age(self, current_year):
        return current_year - self.birth_date

person = Person("Alisher", "O'zbekiston", 1995)
print("Yoshi:", person.age(2025))

# 3. Calculator Class

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Xato: Nolga bo'lish mumkin emas"


calc = Calculator()
print("Qo'shish:", calc.add(5, 3))  
print("Bo'lish:", calc.divide(10, 2))  


# 8. Shopping Cart Class

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def remove_item(self, item):
        self.items = [i for i in self.items if i[0] != item]

    def total_price(self):
        return sum(price for item, price in self.items)


cart = ShoppingCart()
cart.add_item("Non", 1000)
cart.add_item("Sut", 1500)
print("Jami narx:", cart.total_price())  
