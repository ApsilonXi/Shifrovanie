import time
import random
import mouse  # Для работы с мышкой
import os

class LinearCongruentialGenerator:
    def __init__(self, n):
        self.m = 2 ** n
        self.a = self.generate_a()
        self.b = self.generate_b()
        self.c = self.generate_c()
        self.current = self.c

    def generate_a(self):
        while True:
            a = int(time.time()) % (self.m - 1) + 1  # Генерация a
            if a % 4 == 1:
                return a

    def generate_b(self):
        while True:
            b = random.randint(1, self.m - 1)
            if b % 2 == 1 and os.gcd(b, self.m) == 1:
                return b

    def generate_c(self):
        x, y = mouse.get_position()  # Получаем текущую позицию мыши
        seed = (x + y + int(time.time())) % self.m
        return seed

    def next(self):
        self.current = (self.a * self.current + self.b) % self.m
        return self.current

    def generate_sequence(self, length):
        return [self.next() for _ in range(length)]

def save_to_file(sequence, filename):
    with open(filename, 'w') as f:
        for number in sequence:
            f.write(f"{number}\n")

# Пример использования
if __name__ == "__main__":
    n = 24
    lcg = LinearCongruentialGenerator(n)

    # Генерация одного числа
    print("Сгенерированное псевдослучайное число:", lcg.next())

    # Генерация последовательности длиной 10
    sequence_length = 10
    sequence = lcg.generate_sequence(sequence_length)
    print("Сгенерированная последовательность:", sequence)

    # Сохранение в файл
    save_to_file(sequence, 'random_numbers.txt')
    print("Последовательность сохранена в файл random_numbers.txt")