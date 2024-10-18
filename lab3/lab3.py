def permute(k, arr):
    return ''.join(k[i] for i in arr)

def left_shift(key):
    return key[1:] + key[0]

def key_schedule(key):
    # Порядки перестановки ключа
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    # Перестановка ключа с применением pc1
    key = permute(key, pc1)

    # Делим ключ на две половины
    left = key[:28]
    right = key[28:]

    round_keys = []
    for i in range(16):
        left = left_shift(left)
        right = left_shift(right)
        round_key = left + right
        round_keys.append(permute(round_key, [i for i in range(16)]))  # Здесь просто для примера.

    return round_keys

def f_function(right, round_key):
    # Определение F-функции (упрощённое)
    return ''.join(['1' if right[i] != round_key[i] else '0' for i in range(len(right))])

def encrypt(plaintext, key):
    round_keys = key_schedule(key)
    for round_key in round_keys:
        left = plaintext[:32]
        right = plaintext[32:]
        temp = right
        right = f_function(right, round_key)
        plaintext = left + ''.join(['1' if temp[i] != right[i] else '0' for i in range(len(temp))])
    return plaintext

def decrypt(ciphertext, key):
    round_keys = key_schedule(key)[::-1]  # Обратный порядок ключей
    for round_key in round_keys:
        left = ciphertext[:32]
        right = ciphertext[32:]
        temp = right
        right = f_function(right, round_key)
        ciphertext = left + ''.join(['1' if temp[i] != right[i] else '0' for i in range(len(temp))])
    return ciphertext

def main():
    action = input("Выберите действие (1 - зашифровать, 2 - расшифровать): ")
    
    input_file = "lab3/mumu.txt"
    output_file = "lab3/output.txt"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read().strip()

    # Для простоты использования, ключ будет фиксированным
    key = '10101010101111001011110011010111001100110011101100000000'  # 64 бита, просто пример

    if action == '1':
        ciphertext = encrypt(text, key)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(ciphertext)
        print("Текст зашифрован и сохранён в", output_file)

    elif action == '2':
        decrypted_text = decrypt(text, key)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted_text)
        print("Текст расшифрован и сохранён в", output_file)

    else:
        print("Некорректный ввод!")

if __name__ == "__main__":
    main()