import numpy as np
import matplotlib.pyplot as plt
import time
import mouse
import math

def generate_random_sequence(c0, length, a, b, modulus=2**32):
    random_numbers = []
    current_value = c0
    for _ in range(length):
        current_value = (a * current_value + b) % modulus
        random_numbers.append(current_value / modulus)  
    return random_numbers

def save_to_file(numbers, filename):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")

def plot_histogram(numbers):
    plt.hist(numbers, bins=100, density=True, alpha=0.5, color='b')
    plt.title('Гистограмма относительных частот')
    plt.xlabel('Значения')
    plt.ylabel('Относительная частота')
    plt.grid(True)
    plt.show()

def main(a, b, c):
    length = int(input("Введите длину последовательности: "))
    filename = 'lab2/rand_num.txt'

    # Генерация последовательности
    random_numbers = generate_random_sequence(c, length, a, b)

    # Сохранение в файл
    save_to_file(random_numbers, filename)
    print(f"Последовательность сохранена в {filename}")

    # Построение гистограммы
    plot_histogram(random_numbers)

def generate_abc():
    current_time = int(time.time() * 1000)  # текущее время в миллисекундах
    cursor_x, cursor_y = mouse.get_position()  # координаты курсора

    # Определяем параметры a, b и c0
    a = (current_time + cursor_x + 1) % (2**48 - 1)  # избегаем 0
    b = (current_time + cursor_y + 1) % (2**48 - 1) | 1  # делаем нечетным
    c = (cursor_x + cursor_y) % (2**48 - 1)  # начальное значение
    
    return a, b, c

if __name__ == "__main__":
    m = 2**48
    while True:
        a, b, c = generate_abc()
        if (a % 4 == 1) and (math.gcd (m, b) == 1):
            print(a, b, c)
            break
    main(a, b, c)