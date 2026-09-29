# Лабораторна робота №2
# Варіант 13
# Задачі: 114, 139, 164, 169, 183, 192

from datetime import date, timedelta


def task_114():
    number = float(input("Введіть число: "))

    if number > 0:
        print("It is positive number")
    elif number < 0:
        print("It is a negative number")
    else:
        print("It is Zero")


def task_139():
    number = float(input("Введіть число: "))

    if -5 < number < 3:
        print("True")
    else:
        print("False")


def task_164():
    height = float(input("Введіть зріст у метрах: "))
    weight = float(input("Введіть масу у кілограмах: "))

    bmi = weight / (height * height)

    if bmi < 18.5:
        status = "underweight"
    elif bmi <= 24.9:
        status = "normal weight"
    else:
        status = "overweight"

    print(f"Your body mass index is: {bmi:.2f} , that is {status}.")


def task_169():
    number = int(input("Введіть трицифрове число: "))
    digit = int(input("Введіть цифру: "))

    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    if digit == hundreds or digit == tens or digit == ones:
        print("True")
    else:
        print("False")


def task_183():
    day = int(input("Введіть день: "))
    month = int(input("Введіть місяць: "))
    year = int(input("Введіть рік: "))

    current_date = date(year, month, day)
    yesterday = current_date - timedelta(days=1)

    print(f"{yesterday.day}.{yesterday.month}.{yesterday.year}")


def task_192():
    x1 = int(input("Введіть номер стовпця першої клітинки: "))
    y1 = int(input("Введіть номер рядка першої клітинки: "))
    x2 = int(input("Введіть номер стовпця другої клітинки: "))
    y2 = int(input("Введіть номер рядка другої клітинки: "))

    if abs(x1 - x2) == abs(y1 - y2):
        print("Yes")
    else:
        print("No")


print("Лабораторна робота №2 — Варіант 13")
print("114 — додатне, від'ємне або нуль")
print("139 — перевірка належності інтервалу (-5, 3)")
print("164 — індекс маси тіла")
print("169 — перевірка наявності цифри у трицифровому числі")
print("183 — вчорашня дата")
print("192 — хід шахового слона")
print()

task_number = int(input("Оберіть номер задачі: "))

if task_number == 114:
    task_114()
elif task_number == 139:
    task_139()
elif task_number == 164:
    task_164()
elif task_number == 169:
    task_169()
elif task_number == 183:
    task_183()
elif task_number == 192:
    task_192()
else:
    print("Такої задачі у варіанті 13 немає.")
