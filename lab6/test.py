import RSA

import DES

def If_needed():
    RSA.gen_key_data()
    return {"status": "ok"}

def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    
def write_text_file(text, filename):
    with open(filename, 'w+', encoding='utf-8') as file:
        return file.write(text)

def Start():
    while True:
        print("\nВыберите действие:")
        print("0. Для шифрования ключа и дешифрования ключа с помощью RSA")
        print("1. Шифрование файла")
        print("2. Дешифрование файла")
        print("3. Выход")
        choice = input("Ваш выбор: ")

        match choice:
            case "0":
                key = read_text_file("laba 6/keys/key.txt")
                public_key_RSA = RSA.extract_data("laba 6/keys/public_key_for_RSA.txt")
                
                ciphered_key = RSA.encrypt(public_key_RSA, key)

                res_str = ""
                for i in ciphered_key:
                    res_str += str(i) + ", "

                write_text_file(res_str, "laba 6/keys/ciphered key.txt")
                # decrypted_key = RSA.decrypt(private_key_RSA, ciphered_key)
                # write_text_file(decrypted_key, "laba 6/keys/decrypted key.txt")

            case "1":
                input_file = input("Введите путь к файлу: ")
                # key = read_text_file("laba 6/keys/key.txt")
                key = RSA.read_numbers_from_file("laba 6/keys/ciphered key.txt")
                private_key_RSA = RSA.extract_data("laba 6/keys/private_key_for_RSA.txt")
                decrypted_key = RSA.decrypt(private_key_RSA, key)
                print(decrypted_key)


                with open(input_file, 'r', encoding='utf-8') as file:
                    data = file.read().encode('utf-8')

                encrypted_data = rc6.encrypt_ecb(data, decrypted_key)
                output_path = "laba 6/res/encoded.txt"
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(encrypted_data.hex())
                print(f"Зашифрованный файл сохранён: {output_path}")

            case "2":
                input_file = input("Введите путь к зашифрованному файлу: ")

                key = RSA.read_numbers_from_file("laba 6/keys/ciphered key.txt")
                private_key_RSA = RSA.extract_data("laba 6/keys/private_key_for_RSA.txt")
                decrypted_key = RSA.decrypt(private_key_RSA, key)
                
                print(decrypted_key)
                
                with open(input_file, 'r', encoding='utf-8') as file:
                    data = bytes.fromhex(file.read().strip())

                decrypted_data = rc6.decrypt_ecb(data, decrypted_key)
                output_path = "laba 6/res/decoded.txt"
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(decrypted_data)
                print(f"Расшифрованный файл сохранён: {output_path}")



            case "3":
                break

            case _:
                print("Вы ввели непонятную фигню!")
            
            


    pass







# Основное меню
def main():

    while True:
        print("\nВыберите действие:")
        print("1. Шифрование файла RC6")
        print("2. Дешифрование файла RC6")
        print("3. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            input_file = input("Введите путь к файлу: ")
            key = read_text_file("laba 6/res/key.txt")
            with open(input_file, 'r', encoding='utf-8') as file:
                data = file.read().encode('utf-8')

            encrypted_data = rc6.encrypt_ecb(data, key)
            output_path = "laba 6/res/encoded.txt"
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(encrypted_data.hex())
            print(f"Зашифрованный файл сохранён: {output_path}")

        elif choice == "2":
            input_file = input("Введите путь к зашифрованному файлу: ")
            key = read_text_file("laba 6/key.txt")
            with open(input_file, 'r', encoding='utf-8') as file:
                data = bytes.fromhex(file.read().strip())

            decrypted_data = rc6.decrypt_ecb(data, key)
            output_path = "laba 6/res/decoded.txt"
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(decrypted_data)
            print(f"Расшифрованный файл сохранён: {output_path}")

        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    Start()
    pass
    # main()