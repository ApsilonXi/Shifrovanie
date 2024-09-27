import numpy as np
import matplotlib.pyplot as plt

def generate_random_sequence(c0, length, modulus=2**32, a=1664525, b=1013904223):
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

def main():
    c0 = int(input("Введите порождающее число (c0): "))
    length = int(input("Введите длину последовательности: "))
    filename = input("Введите имя файла для сохранения: ")

    # Генерация последовательности
    random_numbers = generate_random_sequence(c0, length)

    # Сохранение в файл
    save_to_file(random_numbers, filename)
    print(f"Последовательность сохранена в {filename}")

    # Построение гистограммы
    plot_histogram(random_numbers)

if __name__ == "__main__":
    main()