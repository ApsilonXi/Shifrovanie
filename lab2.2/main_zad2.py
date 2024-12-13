import time
import pyautogui
import os
import math

def vzaimno_simple(a, b):
    while True:
        if math.gcd(a, b) != 1:
            a -= 1
        else:
            return a


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

def generate_new_parameters():
    """Генерирует новые параметры ГПСЧ."""
    c0 = abs(a - b) * m
    c0 = Check_num(c0, m)
    print(f"Новые параметры сгенерированы: c0 = {c0}")
    return c0


time_now = time.time()
a, b = pyautogui.position()
a *= time_now; b *= time_now

n = 24
m = 2**n


# a = 5  # a mod 4 = 1
c0 = None

a = Check_num(a, m)
b = Check_num(b, m) # Нечетное число, взаимно простое с m
b = vzaimno_simple(b, m)

print(f"b do: {b}")
b = check_b(b)
print(f"b posle: {b}")



print(f"a do: {a}")
a = check_a(a)
print(f"a posle: {a}")

c0 = generate_new_parameters()






def generate_key(filename):
    """Генерирует файл-ключ с параметрами LCG."""
    if os.path.exists(filename):
        choice = input(f"Файл '{filename}' уже существует. Заменить его? (да/нет): ")
        if choice.lower() != 'да':
            return

    with open(filename, "w") as f:
        f.write(f"{a}\n{b}\n{c0}")

    print(f"Файл-ключ '{filename}' успешно создан.")

def lcg_generator(a, b, c0, length):
    """Генерирует последовательность случайных чисел LCG."""
    x = c0
    for _ in range(length):
        x = (a * x + b) % 2**32
        yield x

def encrypt(input_filename, key_filename, output_filename):
    # [+] Шифрует файл гаммированием
    with open(key_filename, "r") as f:
        a, b, c0 = map(int, f.readlines())

    with open(input_filename, "rb") as f_in:
        data = f_in.read()
        # print(data)

    length = len(data)

    if os.path.exists(output_filename):
        choice = input(f"Файл '{output_filename}' уже существует. Заменить его? (да/нет): ")
        if choice.lower() != 'да':
            return

    with open(output_filename, "wb") as f_out:
        for i, byte in enumerate(data):
            # print("leee", i, byte)
            random_number = next(lcg_generator(a, b, c0, length))
            f_out.write(bytes([byte ^ (random_number & 0xFF)]))

    print(f"Файл '{input_filename}' успешно зашифрован в файл '{output_filename}'.")

import coder_to_utf_8

def decrypt(input_filename, key_filename, output_filename):
    # [+] Дешифрует файл гаммированием
    with open(key_filename, "r") as f:
        a, b, c0 = map(int, f.readlines())

    with open(input_filename, "rb") as f_in:
        data = f_in.read()

    length = len(data)

    if os.path.exists(output_filename):
        choice = input(f"Файл '{output_filename}' уже существует. Заменить его? (да/нет): ")
        if choice.lower() != 'да':
            return

    with open(output_filename, "wb") as f_out:
        for i, byte in enumerate(data):
            random_number = next(lcg_generator(a, b, c0, length))
            f_out.write(bytes([byte ^ (random_number & 0xFF)]))

    print(f"Файл '{input_filename}' успешно расшифрован в файл '{output_filename}'.")
    coder_to_utf_8.convert_to_utf8(output_filename)

    

if __name__ == "__main__":
    while True:
        print("\n" + "Выберите действие:")
        print("1. Сгенерировать файл-ключ")
        print("2. Зашифровать файл")
        print("3. Расшифровать файл")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            filename = input("Введите имя файла-ключа (с расширением .key): ")
            generate_key(filename)
        elif choice == "2":
            input_filename = input("Введите имя файла для шифрования: ")
            key_filename = input("Введите имя файла-ключа: ")
            output_filename = input("Введите имя выходного файла: ")

            start_time = time.time()
            encrypt(input_filename, key_filename, output_filename)
            end_time = time.time()

            print(f"Время выполнения: {end_time - start_time:.2f} секунд")
        elif choice == "3":
            input_filename = input("Введите имя файла для дешифрования: ")
            key_filename = input("Введите имя файла-ключа: ")
            output_filename = input("Введите имя выходного файла: ")

            start_time = time.time()
            decrypt(input_filename, key_filename, output_filename)
            end_time = time.time()

            print(f"Время выполнения: {end_time - start_time:.2f} секунд")

        elif choice == "4":
            break
        else:
            print("Неверный выбор.")