#  int generalNumber = 98657;

 # int tensOfThousands = generalNumber / 10000; // Десятки тысяч
# int thousand = (generalNumber - tensOfThousands * 10000) / 1000; // Тысячи
# int hundred = (generalNumber - tensOfThousands * 10000 - thousand * 1000) / 100; // Сотни
# int ten = (generalNumber - tensOfThousands * 10000 - thousand * 1000 - hundred * 100) / 10; // Десятки
# int unit = generalNumber - tensOfThousands * 10000 - thousand * 1000 - hundred * 100 - ten * 10; // Единицы

# Console.WriteLine(tensOfThousands + " " + thousand + " " + hundred + " " + ten + " " + unit);

# // Возведение десятков в степень равную кол-ву единиц
 # int exponentiationOfNumber = (int)Math.Pow(ten, unit);

 # // Умножение получившегося числа на кол-во сотен
 #int multiplication = exponentiationOfNumber * hundred;

 # // Деление получившегося числа на разность кол-ва десятков тысяч и кол-ва тысяч
 # double division = multiplication / (tensOfThousands - thousand);

 # Console.WriteLine("1. Возведение десятков в степень равную кол-ву единиц, число А: " + exponentiationOfNumber +
 #    "\n2. Умножение получившегося числа A на кол-во сотен, число В: " + multiplication +
#   "\n3. Деление получившегося числа В на разность кол-ва десятков тысяч и кол-ва тысяч: " + division);

      #  Задание первое

sideA = float(input("Введите сторону сторону треугольника А: "))
sideB = float(input("Введите сторону треугольника B: "))
sideC = float(input("Введите сторону треугольника С: "))

#   Считаем периметр треугольника

print("Периметр реугольника равен", sep="="), print(sideA + sideB + sideC)

# Считаем площадь треугольника

s = (sideA + sideB + sideC) / 2  # Полупериметр
area = (s*(s - sideA)*(s - sideB)*(s - sideC)) ** 0.5

print('The area of the triangle is %0.2f' %area)


                                            # Площадь и периметр прямоугольника

side_A = float(input("Введите сторону прямоугольника A: "))
side_B = float(input("Введите сторону прямоугольника B: "))

# Считаем периметр прямоугольника

print("Периметр прямоугольника равен", sep="="), print((side_A * 2) + (side_B * 2))



