import math as m
import random
from random import randint, getrandbits

bit_length = 1024

def gen_prime(bit_length=1024):
    while True:
        num = getrandbits(bit_length)
        if is_prime(num):
            return num

#проверка на простое число
def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def inverse(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def gcd(a: int, b: int) -> int:
    return a if b == 0 else m.gcd(a, a % b)

#шаг 1
def generate_keypair(p, q, bit_length):

    p = gen_prime(bit_length)
    q = gen_prime(bit_length)

    n = p * q
    eyler = (p-1) * (q-1)

    # Выбираем открытый ключ e, такой что 1 < e < eyler и e взаимно прост с eyler
    e = random.randrange(2, eyler)
    while m.gcd(e, eyler) != 1:
        e = random.randrange(2, eyler)

    # Вычисляем закрытый ключ d, такой что d * e ≡ 1 (mod eyler)
    d = inverse(e, eyler)

    return ((e, n), (d, n))

#шаг 2
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext] #шифруем юникод код
    
    return ciphertext

#шаг 3
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext] #юникод код в символ
    return ''.join(plaintext)


def extract_data(file_path):
    with open(file_path, 'r') as file:
        content1 = file.readline()

    content1 = content1.replace('(', '').replace(')', '')
    data1 = content1.split('[')[1].split(']')[0].split(", ")
    res1 = [int(item) for item in data1]

    return res1


def gen_key_data():
    p = gen_prime(1024)
    q = gen_prime(1024)

    public, private = generate_keypair(p, q, 1024)
    with open("lab6\\public_key_for_RSA.txt", mode = "w+") as f_key:
        f_key.write(f'Public: [{public}]')
    
    with open("lab6\\private_key_for_RSA.txt", mode = "w+") as f_key:
        f_key.write(f'Private: [{private}]')