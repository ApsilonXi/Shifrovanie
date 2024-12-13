# RC6

import struct
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import base64

W = 32  # размер слова в битах
R = 20  # количество раундов
P32 = 0xB7E15163
Q32 = 0x9E3779B9

def left(x, y):
    return ((x << y) | (x >> (32 - y))) & 0xFFFFFFFF

def right(x, y):
    return ((x >> y) | (x << (32 - y))) & 0xFFFFFFFF

def key_sh(key):
    L = [0] * ((len(key) + 3) // 4)
    for i in range(len(key)):
        L[i // 4] = (L[i // 4] << 8) + key[i]

    # S
    S = [(P32 + i * Q32) & 0xFFFFFFFF for i in range(2 * R + 4)]
    i, j, A, B = 0, 0, 0, 0
    v = 3 * max(len(L), len(S))

    # ключи
    for _ in range(v):
        A = S[i] = left((S[i] + A + B) & 0xFFFFFFFF, 3)
        B = L[j] = left((L[j] + A + B) & 0xFFFFFFFF, (A + B) & 0x1F)
        i = (i + 1) % len(S)
        j = (j + 1) % len(L)

    return S

def encrypt(block, S):
    A, B, C, D = struct.unpack('<4I', block)
    B = (B + S[0]) & 0xFFFFFFFF
    D = (D + S[1]) & 0xFFFFFFFF

    for i in range(1, R + 1):
        t = left((B * (2 * B + 1)) & 0xFFFFFFFF, 5)
        u = left((D * (2 * D + 1)) & 0xFFFFFFFF, 5)
        A = (left(A ^ t, u & 0x1F) + S[2 * i]) & 0xFFFFFFFF
        C = (left(C ^ u, t & 0x1F) + S[2 * i + 1]) & 0xFFFFFFFF
        A, B, C, D = B, C, D, A

    A = (A + S[2 * R + 2]) & 0xFFFFFFFF
    C = (C + S[2 * R + 3]) & 0xFFFFFFFF
    return struct.pack('<4I', A, B, C, D)

def decrypt(block, S):
    A, B, C, D = struct.unpack('<4I', block)
    C = (C - S[2 * R + 3]) & 0xFFFFFFFF
    A = (A - S[2 * R + 2]) & 0xFFFFFFFF

    for i in range(R, 0, -1):
        A, B, C, D = D, A, B, C
        u = left((D * (2 * D + 1)) & 0xFFFFFFFF, 5)
        t = left((B * (2 * B + 1)) & 0xFFFFFFFF, 5)
        C = right((C - S[2 * i + 1]) & 0xFFFFFFFF, t & 0x1F) ^ u
        A = right((A - S[2 * i]) & 0xFFFFFFFF, u & 0x1F) ^ t

    D = (D - S[1]) & 0xFFFFFFFF
    B = (B - S[0]) & 0xFFFFFFFF
    return struct.pack('<4I', A, B, C, D)

def encrypt_ecb_no_padding(plaintext, key):

    key = key.encode('utf-8')
    S = key_sh(key)
    ciphertext = b''

    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        if len(block) < 16:
            block = block.ljust(16, b'\x00')  
        encrypted_block = encrypt(block, S)
        ciphertext += encrypted_block

    return ciphertext


def decrypt_ecb_no_padding(ciphertext, key):

    key = key.encode('utf-8')
    S = key_sh(key)
    plaintext = b''

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decrypted_block = decrypt(block, S)
        plaintext += decrypted_block.rstrip(b'\x00')  

    return plaintext.decode('utf-8', errors='ignore') 


def main():
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        o = int(input("^: "))
        match o:
            case 1:
                key = input("key: ")
                input_file = 'lab4\mumu.txt'
                with open(input_file, "r", encoding='utf-8') as f_in:
                    file_data = f_in.read().encode('utf-8')

                encrypted = encrypt_ecb_no_padding(file_data, key)

                blocks = [encrypted[i:i+16] for i in range(0, len(encrypted), 16)]

                output_file = 'lab4\encrypted.txt'
                if output_file:
                    with open(output_file, 'w', encoding='utf-8') as file:
                        file.write(encrypted.hex())
                break

            case 2:
                key = input("Введите ключ: ")
                input_file = 'lab4\encrypted.txt'

                with open(input_file, "r", encoding="utf-8") as f_in:
                    file_data = f_in.read().strip()
                try:
                    file_data = bytes.fromhex(file_data)
                except ValueError:
                    print("Error: File contains non-hexadecimal characters.")
                    return

                blocks = [file_data[i:i+16] for i in range(0, len(file_data), 16)]
               
                ciphertext_permuted = b''.join(blocks)
                decrypted = decrypt_ecb_no_padding(ciphertext_permuted, key)

                output_file = 'lab4\decrypted.txt'
                if output_file:
                    with open(output_file, 'w', encoding='utf-8') as file:
                        file.write(decrypted)
                break


main()