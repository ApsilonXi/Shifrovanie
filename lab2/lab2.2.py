import os
import time
import struct

def confirm_replacement(file_path):
    if os.path.exists(file_path):
        return input(f"Файл {file_path} уже существует. Заменить? (y/n): ").strip().lower() == 'y'
    return True

def fixed_key_parameters():
    a = 1664525  # Стандартный коэффициент для ЛКГ
    b = 1013904223
    c0 = 42  # Начальное значение
    return a, b, c0

def save_key(file_path, a, b, c0):
    if confirm_replacement(file_path):
        with open(file_path, 'w') as f:
            f.write(f"{a}\n{b}\n{c0}\n")
        print(f"Ключи сохранены в файл {file_path}")

def load_key(file_path):
    with open(file_path, 'r') as f:
        a = int(f.readline().strip())
        b = int(f.readline().strip())
        c0 = int(f.readline().strip())
    return a, b, c0

def linear_congruential_generator(a, b, c0, length):
    numbers = []
    c = c0
    for _ in range(length):
        c = (a * c + b) % (2**32)  # Используем 32-битный диапазон
        numbers.append(c)
    return numbers

def encrypt_file(source_file, key_file, output_file):
    a, b, c0 = load_key(key_file)
    
    with open(source_file, 'rb') as infile:
        data = infile.read()

    length = len(data)
    random_numbers = linear_congruential_generator(a, b, c0, length)

    encrypted_data = bytearray()
    for i in range(length):
        encrypted_byte = data[i] ^ (random_numbers[i] % 256)  # Возвращаемимые значения в пределах 0-255
        encrypted_data.append(encrypted_byte)

    if confirm_replacement(output_file):
        with open(output_file, 'wb') as outfile:
            outfile.write(encrypted_data)
        print(f"Файл зашифрован и сохранён как {output_file}")

if __name__ == '__main__':
    # Определяем параметры ключа
    a, b, c0 = fixed_key_parameters()

    # Сохраняем ключ
    key_file_path = 'C:\EmilyVolkova\VUZ\Shifrovanie\lab2/key.txt'
    save_key(key_file_path, a, b, c0)

    # Шифруем файл
    source_file_path = 'C:\EmilyVolkova\VUZ\Shifrovanie\lab2/mumu.txt'  # Исходный файл
    output_file_path = 'C:\EmilyVolkova\VUZ\Shifrovanie\lab2/encrypted.bin'  # Файл с зашифрованными данными
    encrypt_file(source_file_path, key_file_path, output_file_path)