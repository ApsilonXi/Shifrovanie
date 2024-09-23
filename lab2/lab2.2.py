import os
import time

def confirm_replacement(file_path):
    if os.path.exists(file_path):
        return input(f"Файл {file_path} уже существует. Заменить? (y/n): ").strip().lower() == 'y'
    return True

def load_key(file_path):
    with open(file_path, 'r') as f:
        a = int(f.readline().strip())
        b = int(f.readline().strip())
        c0 = int(f.readline().strip())
    return a, b, c0

def linear_congruential_generator(a, b, c0, length): 
    numbers = []
    c = c0
    for _ in range(length):
        c = (a * c + b) % (2**32)  
        numbers.append(c)
    return numbers

def encrypt_file(input_file, key_file, output_file):
    a, b, c0 = load_key(key_file)
    
    with open(input_file, 'rb') as infile:
        original_data = infile.read()

    length = len(original_data)
    random_numbers = linear_congruential_generator(a, b, c0, length)

    encrypted_data = bytearray()
    for i in range(length):
        encrypted_byte = original_data[i] ^ (random_numbers[i] % 256)  
        encrypted_data.append(encrypted_byte)

    if confirm_replacement(output_file):
        with open(output_file, 'wb') as outfile:
            outfile.write(encrypted_data)
        print(f"Файл зашифрован и сохранён как {output_file}")

def decrypt_file(encrypted_file, key_file, output_file):
    a, b, c0 = load_key(key_file)
    
    with open(encrypted_file, 'rb') as infile:
        encrypted_data = infile.read()

    length = len(encrypted_data)
    random_numbers = linear_congruential_generator(a, b, c0, length)

    decrypted_data = bytearray()
    for i in range(length):
        decrypted_byte = encrypted_data[i] ^ (random_numbers[i] % 256) 
        decrypted_data.append(decrypted_byte)

    if confirm_replacement(output_file):
        with open(output_file, 'wb') as outfile:
            outfile.write(decrypted_data)
        print(f"Файл расшифрован и сохранён как {output_file}")

if __name__ == "__main__":
    key_file = "lab2/key.txt"

    input_file_to_encrypt = "lab2/mumu.txt"
    encrypted_file = "lab2/encrypted_file.bin"
    t1 = time.time()
    encrypt_file(input_file_to_encrypt, key_file, encrypted_file)
    print('Время шифрования: ', time.time() - t1)

    encrypted_file_to_decrypt = "lab2/encrypted_file.bin"
    decrypted_file = "lab2/decrypted_file.txt"
    #t1 = time.time()
    #decrypt_file(encrypted_file_to_decrypt, key_file, decrypted_file)
    #print('Время дешифрования: ', time.time() - t1)
