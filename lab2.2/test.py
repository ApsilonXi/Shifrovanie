# import random
# import math
# import time


# def GPSCH(a, b, c0, m):
#     c1 = a * c0 + b
#     c1 %= m
#     return c1


# def Start(a, b, m):
#     c0 = random.randint(1, m - 1)
    
#     pass



# if __name__ == "__main__":
#     n = 24
#     a = int(input(""))
#     Start()
#     pass




# sys.path = [
#     'C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\4 курс 7 сем\\кодировка\\лаба 2',
#     'C:\\Python312\\python312.zip',
#     'C:\\Python312\\DLLs',
#     'C:\\Python312\\Lib',
#     'C:\\Python312',
#     'C:\\Python312\\Lib\\site-packages',
# ]
# USER_BASE: 'C:\\Users\\79045\\AppData\\Roaming\\Python' (doesn't exist)
# USER_SITE: 'C:\\Users\\79045\\AppData\\Roaming\\Python\\Python312\\site-packages' (doesn't exist)
# ENABLE_USER_SITE: True

# print(f'a: {a}')
# print(f"m: {m}")



import matplotlib.pyplot as plt
import time
import pyautogui
import math


def Check_num(x, m):
    while x > m:
        x *= 0.1

    x = round(x)
    return x


def check_a(a):
    while a % 4 != 1:
        a -= 1
    return a


def check_b(b):
    if b % 2 == 0:
        b -= 1
    return b


time_now = time.time()
a, b = pyautogui.position()
a *= time_now; b *= time_now

n = 24
m = 2**n


# a = 5  # a mod 4 = 1
c0 = None

a = Check_num(a, m)
b = Check_num(b, m)  # Нечетное число, взаимно простое с m

print(f"b do: {b}")
b = check_b(b)
print(f"b posle: {b}")

print(f"a do: {a}")
a = check_a(a)
print(f"a posle: {a}")

# Добавляем глобальную переменную для хранения c0
global_c0 = None


def generate_new_parameters():
    """Генерирует новые параметры ГПСЧ."""
    global c0, global_c0
    c0 = abs(a - b) * m
    c0 = Check_num(c0, m)
    global_c0 = c0  # Сохраняем c0 после генерации новых параметров
    print(f"Новые параметры сгенерированы: c0 = {c0}")


def generate_next_number():
    """Генерирует следующее псевдослучайное число."""
    global c0, global_c0
    print(f"Значение c0 изначально: {c0}")
    c0 = (a * c0 + b) % m
    c0 = Check_num(c0, m)
    return c0


def generate_sequence(length):
    """Генерирует последовательность псевдослучайных чисел заданной длины."""
    global c0, global_c0
    c0 = global_c0  # Используем глобальное c0 для последовательности
    sequence = [c0]
    for _ in range(length - 1):
        sequence.append(generate_next_number())
    return sequence


def plot_histogram(sequence):
    # Деление диапазона на 100 интервалов
    interval_length = math.ceil(m / 100)
    intervals = [i * interval_length for i in range(101)]

    # Подсчет относительных частот
    frequencies = [0] * 100
    for number in sequence:
        for i in range(100):
            if intervals[i] <= number < intervals[i + 1]:
                frequencies[i] += 1
    frequencies = [freq / len(sequence) for freq in frequencies]

    # Вывод гистограммы
    plt.bar(range(100), frequencies)
    plt.xlabel("Интервалы")
    plt.ylabel("Относительная частота")
    plt.title("Гистограмма относительных частот")
    plt.show()


def main():
    """Основная функция программы."""
    generate_new_parameters()

    while True:
        action = input(
            "Введите действие (g - генерировать, c - изменить a и b, s - последовательность, q - выход): "
        )
        if action == "g":
            next_number = generate_next_number()
            print(f"Следующее число: {next_number}")
        elif action == "c":
            a = int(input("Введите значение a: "))
            b = int(input("Введите значение b: "))
            a = check_a(a)
            b = check_b(b)
            generate_new_parameters()  # Обновляем c0 после изменения a и b
        elif action == "s":
            try:
                length = int(input("Введите длину последовательности: "))
                sequence = generate_sequence(length)
                with open("sequence.txt", "w") as file:
                    for number in sequence:
                        file.write(str(number) + "\n")
                plot_histogram(sequence)
            except ValueError:
                print("Некорректный ввод длины последовательности.")
        elif action == "q":
            break
        else:
            print("Некорректное действие.")


if __name__ == "__main__":
    main()