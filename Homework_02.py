#1. Квадрат числа.
num = int(input("Введіть число: "))
print("Квадрат числа", num**2, sep=' - ')

#2. Середнє трьох чисел
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
num3 = int(input("Введіть третє число: "))
print(f"Середнє: {(num1 + num2 + num3) / 3}")

#3. “Перетворення хвилин у години”
minutes = int(input("Введіть кількість хвилин: "))
hours = minutes // 60
minutes_left = minutes - (hours * 60)
print(f"{hours} години {minutes_left} хвилин")

#4. “Розрахунок знижки”
price = float(input("Введіть ціну товару: "))
discount = float(input("Введіть відсоток знижки: "))
print(f"Ціна зі знижкою: {price - (price * discount / 100)}")

#5. “Остання цифра числа”
num4 = int(input("Введіть число: "))
print("Остання цифра: ", num4 % 10)

#6. “Периметр прямокутника”
length = int(input("Введіть довжину: "))
width = int(input("Введіть ширину: "))
print("Периметр:", length + length + width + width)

#7. Виведення числа в стовпчик
num5 = int(input("Введіть 4-х значне число: "))
print(num5 // 1000, num5 // 100 % 10, num5 // 10 % 10, num5 % 10, sep='\n')

