import struct

# Константы
W = 32  # Размер слова в битах (32-битные слова)
R = 20  # Количество раундов
PW = 0xb7e15163  # Константа для генерации ключей
QW = 0x9e3779b9  # Вторая константа для генерации ключей

# Функция для циклического сдвига влево
def rotate_left(x, y):
    return ((x << y) & (2**W - 1)) | (x >> (W - y))

# Функция для циклического сдвига вправо
def rotate_right(x, y):
    return (x >> y) | ((x << (W - y)) & (2**W - 1))

# Функция для генерации расширенного ключа
def key_schedule(key):
    L = [0] * (len(key) // 4)
    for i in range(len(L)):
        L[i] = struct.unpack('<I', key[4 * i: 4 * (i + 1)])[0]
    
    # Генерация ключей
    S = [0] * (2 * R + 4)
    S[0] = PW
    for i in range(1, 2 * R + 4):
        S[i] = (S[i - 1] + QW) % (2 ** W)

    i = j = A = B = 0
    v = 3 * max(len(L), 2 * R + 4)
    
    for _ in range(v):
        A = S[i] = rotate_left((S[i] + A + B) % (2**W), 3)
        B = L[j] = rotate_left((L[j] + A + B) % (2**W), (A + B) % W)
        i = (i + 1) % (2 * R + 4)
        j = (j + 1) % len(L)

    return S

# Функция шифрования одного блока
def encrypt_block(plain_block, S):
    A, B, C, D = struct.unpack('<4I', plain_block)

    B = (B + S[0]) % (2 ** W)
    D = (D + S[1]) % (2 ** W)

    for i in range(1, R + 1):
        t = rotate_left((B * (2 * B + 1)) % (2 ** W), 5)
        u = rotate_left((D * (2 * D + 1)) % (2 ** W), 5)
        A = (rotate_left(A ^ t, u % W) + S[2 * i]) % (2 ** W)
        C = (rotate_left(C ^ u, t % W) + S[2 * i + 1]) % (2 ** W)
        A, B, C, D = B, C, D, A

    A = (A + S[2 * R + 2]) % (2 ** W)
    C = (C + S[2 * R + 3]) % (2 ** W)

    return struct.pack('<4I', A, B, C, D)

# Функция дешифрования одного блока
def decrypt_block(cipher_block, S):
    A, B, C, D = struct.unpack('<4I', cipher_block)

    C = (C - S[2 * R + 3]) % (2 ** W)
    A = (A - S[2 * R + 2]) % (2 ** W)

    for i in range(R, 0, -1):
        A, B, C, D = D, A, B, C
        u = rotate_left((D * (2 * D + 1)) % (2 ** W), 5)
        t = rotate_left((B * (2 * B + 1)) % (2 ** W), 5)
        C = (rotate_right(C - S[2 * i + 1], t % W) ^ u) % (2 ** W)
        A = (rotate_right(A - S[2 * i], u % W) ^ t) % (2 ** W)

    D = (D - S[1]) % (2 ** W)
    B = (B - S[0]) % (2 ** W)

    return struct.pack('<4I', A, B, C, D)

# Функция добавления отступов (паддинг)
def pad(plaintext):
    padding_len = (16 - len(plaintext) % 16) % 16
    return plaintext + bytes([padding_len] * padding_len)

# Функция удаления отступов (паддинга)
def unpad(plaintext):
    padding_len = plaintext[-1]
    return plaintext[:-padding_len]

# Функция шифрования файла
def encrypt_file(input_file, output_file, key):
    S = key_schedule(key)

    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        plaintext = f_in.read()
        plaintext = pad(plaintext)

        for i in range(0, len(plaintext), 16):
            block = plaintext[i:i + 16]
            cipher_block = encrypt_block(block, S)
            f_out.write(cipher_block)

    print(f'Файл зашифрован и сохранён как {output_file}')

# Функция дешифрования файла
def decrypt_file(input_file, output_file, key):
    S = key_schedule(key)

    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        ciphertext = f_in.read()

        for i in range(0, len(ciphertext), 16):
            block = ciphertext[i:i + 16]
            
            # Проверка на длину блока, чтобы избежать ошибок с неполным блоком
            if len(block) == 16:
                plain_block = decrypt_block(block, S)
                f_out.write(plain_block)  # Сразу записываем расшифрованный блок в файл
            else:
                print(f"Ошибка: неполный блок размером {len(block)} байт обнаружен при расшифровании.")
                

        # Читаем весь файл для удаления паддинга после последнего блока
        f_out.seek(0)  # Перемещаем указатель в начало файла
        decrypted_data = f_out.read()

        try:
            decrypted_data = unpad(decrypted_data)
        except ValueError:
            print("Ошибка: неверный паддинг.")
            return

        # Перезаписываем файл без паддинга
        with open(output_file, 'w') as f_out:
            f_out.write(decrypted_data)

    print(f'Файл расшифрован и сохранён как {output_file}')


def main():
    input_file = 'lab4/mumu.txt'
    output_file_enc = 'lab4/encrypted.txt'
    output_file_dec = 'lab4/decrypted.txt'
    mode = input("Вы хотите зашифровать (e) или расшифровать (d) файл? (e/d): ")

    if mode == 'e':
        key = input("Введите ключ: ").encode()
        key = (key[:16]).ljust(16, b'\0')
        encrypt_file(input_file, output_file_enc, key)
    elif mode == 'd':
        key = input("Введите ключ: ").encode()
        key = (key[:16]).ljust(16, b'\0')
        decrypt_file(input_file, output_file_dec, key)
    else:
        print("Неверный выбор режима!")
        exit()

if __name__ == "__main__":
    main()
