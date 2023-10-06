#
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

print("Периметр прямоугольника равен", sep="=")
print((side_A * 2) + (side_B * 2))

                                       # Площадь прямоугольника
print("Площадь прямоугольника равна: ", sep="=")
print(side_A * side_B)


number = int(input("Enter number:"))

units = number % 10
dozens = number % 100 // 10
hundreads = number % 1000 // 100
thousands = number % 10000 // 1000
doz_of_thous = number // 10000

print((dozens ** units) * hundreads / (doz_of_thous - thousands))


