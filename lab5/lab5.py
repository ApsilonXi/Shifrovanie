import random
import time
from sympy import primerange, primitive_root
from sympy.ntheory.generate import randprime

# Проверка Рабина-Миллера
def rabin_miller_test(p, t):
    if p < 2: #число составное 
        return False
    if p in (2, 3): #число простое
        return True
    if p % 2 == 0: #число четное и составное
        return False

    # Представление p-1 в виде 2^b * m
    m = p - 1 
    b = 0
    while m % 2 == 0: 
        m //= 2
        b += 1

    for _ in range(t):
        a = random.randint(2, p - 2) #выбор случайного числа в диапазоне
        z = pow(a, m, p) # a**m mod p
        if z == 1 or z == p - 1: #проходим текущий раунд и генерируем новое а
            continue

        for _ in range(b - 1): # если z не удовлетворило условиям
            z = pow(z, 2, p)
            if z == p - 1:
                break
        else: 
            return False

    return True

# алгоритм генерации большого простого числа с алгоритмом Рабина-Миллера
def generate_large_prime(n_bits, t):
    start_time = time.time()
    iterations = 0
    small_primes = list(primerange(2, 2000))

    while True:
        iterations += 1
        candidate = random.getrandbits(n_bits)
        candidate |= (1 << n_bits - 1) | 1  # 2. устанавливаем старший и младший биты в 1 (старший для длины, младший для нечетности)

        #проверка не делимости
        if any(candidate % p == 0 for p in small_primes):
            continue

        #Рабина-Миллера
        if rabin_miller_test(candidate, t):
            elapsed_time = time.time() - start_time
            return candidate, iterations, elapsed_time

def find_primes_in_range(start, end):
    start_time = time.time()
    primes = list(primerange(start, end + 1))
    elapsed_time = time.time() - start_time
    return primes, elapsed_time
    
# поиск первых 100 первообразных корней для заданного числа p
def find_primitive_roots(p):
    start_time = time.time()
    roots = [] 

    for candidate in range(2, p):
        if len(roots) >= 100:
            break
        if pow(candidate, (p - 1) // 2, p) != 1:  # проверка условия для корня
            roots.append(candidate)

    elapsed_time = time.time() - start_time
    return roots, elapsed_time

def diffie_hellman_exchange(n_bits, t):
    n, _, _ = generate_large_prime(n_bits, t)  # Случайное большое простое число
    g = primitive_root(n)  # первообразный корень 

    # Генерация секретных чисел
    x_a = random.randint(2, n - 1)
    x_b = random.randint(2, n - 1)

    # Вычисление открытых ключей
    y_a = pow(g, x_a, n)
    y_b = pow(g, x_b, n)

    # Обмен ключами
    k_a = pow(y_b, x_a, n)
    k_b = pow(y_a, x_b, n)

    return n, g, x_a, x_b, y_a, y_b, k_a, k_b

if __name__ == "__main__":
    while True:
        print("Выберите опцию:")
        print("1. Создать большое простое число и найти 100 первообразных")
        print("2. Найти 100 первообразных для числа")
        print("3. Найти все простые числа в диапазоне.")
        print("4. Смоделировать обмен ключами между абонентами")
        o = int(input("^: "))
        match o:
            case 1:
                # Генерация большого простого числа
                n_bits = int(input("Введите n: "))
                if n_bits < 128:
                    print("Должно быть от 128")
                    break
                t = int(input("Введите число проверок t: "))
                prime, iterations, elapsed_time = generate_large_prime(n_bits, t)
                print(f"Создано простое число: {prime}")
                print(f"Итераций: {iterations}, Время: {elapsed_time:.2f} сек\n")

                # Первые 100 первообразных корней
                roots, elapsed_time = find_primitive_roots(prime)
                print(f"Первые 100 первообразных {prime}: {roots}")
                print(f"Время: {elapsed_time:.2f} сек")

            case 2:
                prime = int(input("Введите число для нахождения его первообразных: "))
                roots, elapsed_time = find_primitive_roots(prime)
                print(f"Первые 100 первообразных {prime}: {roots}")
                print(f"Время: {elapsed_time:.2f} сек")


            case 3:
                # Простые числа в диапазоне
                start, end = int(input("Начало: ")), int(input("Конец: "))
                primes, elapsed_time = find_primes_in_range(start, end)
                print(f"Простые числа в диапазоне [{start}, {end}]: {primes}")
                print(f"Время: {elapsed_time:.2f} сек")

            case 4:
                # Обмен ключами Диффи-Хеллмана
                n_bits = int(input("Введите n: "))
                t = int(input("Введите число проверок t: "))
                n, g, x_a, x_b, y_a, y_b, k_a, k_b = diffie_hellman_exchange(n_bits, t)
                print(f"n = {n}, g = {g}")
                print(f"Секретные числа: X_A = {x_a}, X_B = {x_b}")
                print(f"Открытые ключи: Y_A = {y_a}, Y_B = {y_b}")
                print(f"Секретные ключи: K_A = {k_a}, K_B = {k_b}")

            case _:
                break
