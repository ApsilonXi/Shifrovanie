# DES - Data Encryption Standard

# Битовые таблицы для DES
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8
]

IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 9, 5, 3, 11, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 2, 8, 14, 6, 11, 1, 3, 4, 9, 12, 7, 13, 0, 5, 10]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 2, 8, 14, 12, 4, 7],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 1, 15, 14, 12, 5, 11],
        [3, 12, 5, 10, 15, 4, 8, 9, 0, 2, 14, 1, 7, 6, 11, 13],
        [5, 4, 11, 3, 2, 14, 0, 15, 8, 1, 9, 7, 6, 12, 13, 10]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 10, 13, 7, 9, 3, 4, 6, 0, 5, 11, 12, 14, 15, 8, 2],
        [3, 5, 2, 12, 7, 1, 15, 4, 10, 14, 9, 11, 6, 8, 0, 13]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 9, 5, 0, 15, 14, 3, 8, 13],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [2, 12, 4, 1, 7, 10, 11, 6, 9, 5, 0, 15, 14, 3, 8, 13],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [6, 11, 13, 2, 12, 4, 1, 10, 14, 9, 0, 7, 3, 5, 15, 8],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 10, 13, 7, 9, 3, 4, 6, 0, 5, 11, 12, 14, 15, 8, 2],
        [3, 5, 2, 12, 7, 1, 15, 4, 10, 14, 9, 11, 6, 8, 0, 13]
    ]
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Функция для преобразования ключа
def permute(key, table):
    return [key[i - 1] for i in table]

# Функция для расширения данных
def expand_half_block(block):
    if len(block) != 32:
        raise ValueError(f"Длина блока должна быть 32 бита, но длина блока {len(block)}.")
    return [block[i - 1] for i in E]

# Функция для применения S-боксов
def s_box_substitution(expanded_block):
    result = []
    for i in range(8):
        row = (expanded_block[i * 6] << 1) | expanded_block[i * 6 + 5]
        col = (expanded_block[i * 6 + 1] << 3) | (expanded_block[i * 6 + 2] << 2) | (expanded_block[i * 6 + 3] << 1) | expanded_block[i * 6 + 4]
        result.extend(list(map(int, bin(S_BOXES[i][row][col])[2:].zfill(4))))  # 4 бита результата
    return result

# Функция для выполнения одного раунда DES
def des_round(left, right, key):
    expanded_right = expand_half_block(right)
    xor_result = [a ^ b for a, b in zip(expanded_right, key)]
    s_box_output = s_box_substitution(xor_result)
    p_output = permute(s_box_output, P)
    return right, [a ^ b for a, b in zip(left, p_output)]

# Функция для генерации ключей
def generate_keys(key):
    key = permute(key, IP)
    keys = []
    for i in range(16):
        keys.append(key)  # Здесь будет логика для реальной генерации ключа
    return keys

# Основная функция DES
def des_encrypt(plaintext, key):
    key = [int(bit) for bit in key]
    keys = generate_keys(key)

    plaintext = permute(plaintext, IP)

    left, right = plaintext[:32], plaintext[32:]

    for i in range(16):
        left, right = des_round(left, right, keys[i])

    return permute(right + left, IP_INV)

# Функция для расшифровки
def des_decrypt(ciphertext, key):
    key = [int(bit) for bit in key]
    keys = generate_keys(key)[::-1]

    ciphertext = permute(ciphertext, IP)

    left, right = ciphertext[:32], ciphertext[32:]

    for i in range(16):
        left, right = des_round(left, right, keys[i])

    return permute(right + left, IP_INV)

# Функции для работы с файлами
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r', encoding="utf-8") as f:
        plaintext = f.read().strip()
    
    if not plaintext:
        print("Ошибка: файл с текстом пуст.")
        return

    # Конвертация текста в биты
    plaintext_bits = []
    for char in plaintext:
        plaintext_bits.extend([int(bit) for bit in bin(ord(char))[2:].zfill(8)])
    
    # Дополнение до кратности 64
    while len(plaintext_bits) % 64 != 0:
        plaintext_bits.append(0)

    ciphertext_bits = []
    for i in range(0, len(plaintext_bits), 64):
        block = plaintext_bits[i:i + 64]
        if len(block) != 64:
            print(f"Ошибка: блок должен быть 64 бита, но длина блока {len(block)}.")
            continue  # Пропустите блок, если его длина не 64
        ciphertext_block = des_encrypt(block, key)
        ciphertext_bits.extend(ciphertext_block)

    # Конвертация битов в строку
    ciphertext = ''.join(str(bit) for bit in ciphertext_bits)

    with open(output_file, 'w') as f:
        f.write(ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as f:
        ciphertext = f.read().strip()

    ciphertext_bits = [int(bit) for bit in ciphertext]

    plaintext_bits = []
    for i in range(0, len(ciphertext_bits), 64):
        block = ciphertext_bits[i:i + 64]
        if len(block) != 64:
            print(f"Ошибка: блок должен быть 64 бита, но длина блока {len(block)}.")
            continue  # Пропустите блок, если его длина не 64
        plaintext_block = des_decrypt(block, key)
        plaintext_bits.extend(plaintext_block)

    # Конвертация битов в символы
    plaintext = ''
    for i in range(0, len(plaintext_bits), 8):
        byte = plaintext_bits[i:i + 8]
        if len(byte) == 8:
            plaintext += chr(int(''.join(str(bit) for bit in byte), 2))

    with open(output_file, 'w') as f:
        f.write(plaintext)

def main():
    input_file = 'lab3/mumu.txt'  # Файл с текстом для шифрования
    encrypted_file = 'lab3/encrypted.txt'  # Файл для зашифрованного текста
    decrypted_file = 'lab3/decrypted.txt'  # Файл для расшифрованного текста

    key = '0001001100110100010100110111100010011010101111001101111111111110'  # Пример 64-битного ключа

    # Шифрование
    encrypt_file(input_file, encrypted_file, key)
    print('Файл зашифрован.')

    # Дешифрование
    decrypt_file(encrypted_file, decrypted_file, key)
    print('Файл расшифрован.')

if __name__ == "__main__":
    main()
