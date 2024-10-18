# Программа DES

# Начальная перестановка (IP)
def initial_permutation(block):
    ip = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    return [block[i - 1] for i in ip]

# Обратная перестановка (IP^-1)
def inverse_initial_permutation(block):
    ip_inv = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    return [block[i - 1] for i in ip_inv]

# Генерация ключей
def permuted_choice_1(key):
    pc1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    return [key[i - 1] for i in pc1]

def permuted_choice_2(key):
    pc2 = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]
    return [key[i - 1] for i in pc2]

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def generate_keys(key):
    key = permuted_choice_1(key)  # Применяем PC-1
    c, d = key[:28], key[28:]  # Делим на C0 и D0
    keys = []
    shifts = [1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1]  # Сдвиги на раунд
    for shift in shifts:
        c = left_shift(c, shift)
        d = left_shift(d, shift)
        round_key = permuted_choice_2(c + d)  # Применяем PC-2
        keys.append(round_key)
    return keys

# Функция Фейстеля
def feistel_function(right, key):
    # Расширение
    expansion = [
        32, 1, 2, 3, 4, 5, 4, 5,
        6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 16, 17,
        18, 19, 20, 21, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29, 30, 31
    ]

    # S-блоки
    s_boxes = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8],
            [3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1],
            [2, 1, 14, 13, 3, 10, 6, 12]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4],
            [9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 5, 2, 8, 14],
            [12, 10, 15, 9, 0, 3, 14, 6]
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5],
            [1, 13, 2, 8, 12, 7, 4, 11],
            [7, 11, 4, 1, 9, 12, 5, 0],
            [6, 13, 14, 3, 15, 8, 2, 4]
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10],
            [1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 10, 1, 3, 15, 4, 2],
            [2, 5, 6, 12, 0, 11, 9, 7]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6],
            [8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 13, 4, 7, 5, 0],
            [3, 9, 8, 10, 15, 1, 2, 12]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8],
            [0, 13, 3, 4, 14, 7, 5, 11],
            [10, 4, 5, 3, 2, 12, 0, 1],
            [15, 9, 14, 8, 13, 6, 11, 7]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13],
            [3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10],
            [2, 13, 14, 8, 12, 5, 6, 15]
        ],
        [
            [1, 4, 11, 13, 12, 7, 10, 15],
            [6, 8, 5, 14, 9, 3, 2, 0],
            [7, 4, 1, 10, 13, 8, 14, 12],
            [0, 5, 9, 11, 3, 2, 15, 6]
        ]
    ]

    # Расширяем правую половину
    right_expanded = [right[i - 1] for i in expansion]
    xor_result = [right_expanded[i] ^ key[i] for i in range(48)]

    # Проходим по S-блокам
    s_output = []
    for i in range(8):
        row = (xor_result[i * 6] << 1) | xor_result[i * 6 + 5]  # 1st and 6th bits
        col = (xor_result[i * 6 + 1] << 3) | (xor_result[i * 6 + 2] << 2) | (xor_result[i * 6 + 3] << 1) | xor_result[i * 6 + 4]  # 2nd to 5th bits
        s_value = s_boxes[i][row][col]
        s_output += [int(bit) for bit in format(s_value, '04b')]  # 4-битное значение

    # Перестановка после S-блоков
    p_box = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]

    return [s_output[i - 1] for i in p_box]

# Основная функция шифрования DES
def des_encrypt(block, keys):
    block = initial_permutation(block)  # Начальная перестановка
    left, right = block[:32], block[32:]  # Разделяем на L и R

    for key in keys:
        temp = right
        right = [left[i] ^ feistel_function(right, key)[i] for i in range(32)]
        left = temp

    # Объединяем L и R и применяем обратную перестановку
    combined = left + right
    return inverse_initial_permutation(combined)

# Функция для преобразования файла в двоичный массив
def file_to_bits(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    bits = []
    for char in data:
        bits.extend([int(bit) for bit in format(ord(char), '08b')])  # Преобразуем каждый символ в 8 бит
    return bits

# Функция для преобразования двоичного массива в строку
def bits_to_file(bits, filename):
    with open(filename, 'wb') as f:
        byte_array = bytearray()
        for i in range(0, len(bits), 8):
            byte_array.append(int(''.join(str(b) for b in bits[i:i + 8]), 2))
        f.write(byte_array)

# Основной блок программы
def main():
    input_file = 'c:\EmilyVolkova\VUZ\Shifrovanie\lab3\mumu.txt'
    encrypted_file = 'c:\EmilyVolkova\VUZ\Shifrovanie\lab3\encrypted_mumu.txt'
    decrypted_file = 'c:\EmilyVolkova\VUZ\Shifrovanie\lab3\decrypted_mumu.txt'

    key = '12345678'  # Ваш ключ
    bits = file_to_bits(input_file)  # Преобразуем файл в двоичный массив
    key_bits = [int(bit) for bit in ''.join(format(ord(c), '08b') for c in key)]  # Преобразуем ключ в двоичный массив
    keys = generate_keys(key_bits)  # Генерируем ключи

    # Шифруем
    encrypted_bits = []
    for i in range(0, len(bits), 64):
        block = bits[i:i + 64]
        if len(block) < 64:
            block.extend([0] * (64 - len(block)))  # Дополняем до 64 бит
        encrypted_bits.extend(des_encrypt(block, keys))

    bits_to_file(encrypted_bits, encrypted_file)  # Записываем зашифрованные биты в файл

    # Дешифруем
    decrypted_bits = []
    for i in range(0, len(encrypted_bits), 64):
        block = encrypted_bits[i:i + 64]
        decrypted_bits.extend(des_encrypt(block, keys[::-1]))  # Используем обратный порядок ключей

    bits_to_file(decrypted_bits, decrypted_file)  # Записываем расшифрованные биты в файл

if __name__ == "__main__":
    main()
