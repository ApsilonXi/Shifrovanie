import time
import mouse  # Нужно установить библиотеку python-mouse для отслеживания курсора

def generate_a_b_c():
    current_time = int(time.time() * 1000)  # текущее время в миллисекундах
    cursor_x, cursor_y = mouse.get_position()  # координаты курсора

    # Определяем параметры a, b и c0
    a = (current_time + cursor_x + 1) % (2**24 - 1)  # избегаем 0
    b = (current_time + cursor_y + 1) % (2**24 - 1) | 1  # делаем нечетным
    c0 = (cursor_x + cursor_y) % (2**24 - 1)  # начальное значение

    return a, b, c0

def linear_congruential_generator(a, b, c0, m=(2**24)):
    c = c0
    while True:
        c = (a * c + b) % m
        yield c

def generate_numbers(num_count=1):
    a, b, c0 = generate_a_b_c()
    generator = linear_congruential_generator(a, b, c0)
    
    # Генерация числа и вывод на экран
    if num_count == 1:
        return next(generator)
    
    # Генерация последовательности чисел
    numbers = [next(generator) for _ in range(num_count)]
    return numbers

def save_numbers_to_file(numbers, filename='C:\EmilyVolkova\VUZ\Shifrovanie\lab2/random_numbers.txt'):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")

# Пример использования
if __name__ == "__main__":
    single_number = generate_numbers()
    print(f"Случайное число: {single_number}")

    sequence_length = 10
    numbers = generate_numbers(num_count=sequence_length)
    print(f"Последовательность случайных чисел: {numbers}")
    
    # Сохранение в файл
    save_numbers_to_file(numbers)
    print(f"Числа сохранены в файл random_numbers.txt")