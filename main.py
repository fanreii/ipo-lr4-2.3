number = int(input("Введите число: ")) # ввод числа с клавиатуры
factorial = 1 # присвоение значения переменной 
while 1 < number: #  цикл while  с условием
    factorial *= number # рассчет факториала
    number -= 1 # рассчет факториала
print (factorial) # вывод результата
