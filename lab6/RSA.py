import math as m
import random
from random import randint, getrandbits

def gen_prime(bits=1024):
    while True:
        num = getrandbits(bits)
        if rabin_miller_test(num):
            return num

def rabin_miller_test(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(5):
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

def d_key(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

#шаг 1
def keys(p, q, bits):

    p = gen_prime(bits)
    q = gen_prime(bits)

    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(2, phi)
    while m.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = d_key(e, phi)

    return ((e, n), (d, n))

#шаг 2
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    
    return ciphertext

#шаг 3
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)


def read_keys(file_path):
    with open(file_path, 'r') as file:
        content1 = file.readline()
    content1 = content1.replace('(', '').replace(')', '')
    data1 = content1.split('[')[1].split(']')[0].split(", ")
    res1 = [int(item) for item in data1]

    return res1


def create_keys():
    p = gen_prime(1024)
    q = gen_prime(1024)

    public, private = keys(p, q, 1024)
    with open("lab6\\public_key.txt", mode = "w+") as f_key:
        f_key.write(f'Public: [{public}]')
    
    with open("lab6\\private_key.txt", mode = "w+") as f_key:
        f_key.write(f'Private: [{private}]')
