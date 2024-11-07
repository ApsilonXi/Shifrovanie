import random
import time
from sympy import isprime, primerange, primitive_root
from sympy.ntheory.generate import randprime

# тест Рабина-Миллера
def miller_rabin_test(n, k):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # n-1 в виде (2^r) * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Тестирование k раз
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# генерация n-битного простого числа
def generate_large_prime(n_bits, t):
    start_time = time.time()
    iteration = 0
    while True:
        iteration += 1
        candidate = random.getrandbits(n_bits)
        if candidate % 2 == 0:
            candidate += 1  # делаем нечетным

        if miller_rabin_test(candidate, t):
            end_time = time.time()
            print(f"Простое число сгенерировано за {iteration} итераций.")
            print(f"Затраченное время: {end_time - start_time:.5f} секунд.")
            return candidate

# поиск простых чисел в заданном диапазоне
def find_primes_in_range(start, end):
    start_time = time.time()
    primes = list(primerange(start, end))
    end_time = time.time()
    print(f"Простые числа в диапазоне от {start} до {end}: {primes}")
    print(f"Время на поиск простых чисел: {end_time - start_time:.5f} секунд.")
    return primes

# нахождение первых 100 первообразных корней
def find_primitive_roots(p):
    start_time = time.time()
    roots = []
    for i in range(2, p):
        if len(roots) >= 100:
            break
        try:
            root = primitive_root(p)
            roots.append(root)
        except ValueError:
            continue
    end_time = time.time()
    print(f"Первые 100 первообразных корней: {roots[:100]}")
    print(f"Время на поиск первообразных корней: {end_time - start_time:.5f} секунд.")
    return roots[:100]

# моделирование обмена ключами по схеме Диффи-Хеллмана
def diffie_hellman_key_exchange(t, n_bits):
    # Генерация простых чисел X_A, X_B и n
    X_A = generate_large_prime(n_bits, t)
    X_B = generate_large_prime(n_bits, t)
    n = generate_large_prime(n_bits, t)

    # Вычисление ключей
    g = primitive_root(n)  # первообразный корень по модулю n
    A = pow(g, X_A, n)     # открытый ключ A
    B = pow(g, X_B, n)     # открытый ключ B

    # Вычисление общего секрета
    secret_A = pow(B, X_A, n)
    secret_B = pow(A, X_B, n)

    print(f"Общий секрет для абонента A: {secret_A}")
    print(f"Общий секрет для абонента B: {secret_B}")
    return secret_A, secret_B

if __name__ == "__main__":
    # Генерация простого числа
    n_bits = 65  # 65 бит - число больше чем 2^64
    t = 5        # Количество проверок в тесте Рабина-Миллера
    prime = generate_large_prime(n_bits, t)

    # Поиск простых чисел в диапазоне
    start_range = 2**63
    end_range = 2**64
    primes_in_range = find_primes_in_range(start_range, end_range)

    # Поиск первых 100 первообразных корней
    primitive_roots = find_primitive_roots(prime)

    # Моделирование обмена ключами по схеме Диффи-Хеллмана
    secret_A, secret_B = diffie_hellman_key_exchange(t, n_bits)
