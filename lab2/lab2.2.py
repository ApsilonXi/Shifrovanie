import matplotlib.pyplot as plt
import numpy as np
from math import gcd

class LinearCongruentialGenerator:
    def __init__(self, seed, a, b, m):
        self.seed = seed
        self.a = a
        self.b = b
        self.m = m
        self.current = seed

    def next(self):
        self.current = (self.a * self.current + self.b) % self.m
        return self.current

    def generate_sequence(self, n):
        return [self.next() for _ in range(n)]

    def plot_sequence(self, n):
        sequence = self.generate_sequence(n)
        plt.plot(sequence, marker='o')
        plt.title('Линейный Конгруэнтный Генератор')
        plt.xlabel('Итерация')
        plt.ylabel('Случайное число')
        plt.grid()
        plt.show()

    def check_periodicity(self):
        initial_value = self.seed
        seen = set()
        while self.current not in seen:
            seen.add(self.current)
            self.next()
        return len(seen)

    def is_coprime(self, x, y):
        return gcd(x, y) == 1

# Параметры генератора
seed = 42      # Начальное значение
a = 1664525    # Множитель
b = 1013904223 # Прибавка
m = 2**32      # Модуль (обычный выбор)

lcg = LinearCongruentialGenerator(seed, a, b, m)

# Генерируем и отображаем последовательность
n = 1000
lcg.plot_sequence(n)

# Проверяем периодичность
period_length = lcg.check_periodicity()
print(f"Длина периода: {period_length}")

# Проверка взаимной простоты
print(f"a и m взаимно простые: {lcg.is_coprime(a, m)}")