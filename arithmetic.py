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
        
    
