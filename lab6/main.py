import RSA
import DES

def read_numbers(filename):
    numbers = []
    with open(filename, "r") as file:
        line = file.read()  
        parts = line.split(", ")  
        for part in parts:
            try:
                number = int(part)  
                numbers.append(number) 
            except ValueError:
                pass

    return numbers

def menu():
    
    while True:
        print("1. Шифрование ключа и дешифрование ключа\n2. Шифрование текста\n3. Дешифрование текста\n")
        choice = input("^: ")

        match choice:
            case "1":
                key = input("Input key: ")
                RSA.gen_key_data()
                public_key_RSA = RSA.extract_data("lab6/public_key_for_RSA.txt")
                ciphered_key = RSA.encrypt(public_key_RSA, key)

                res_str = ""
                for i in ciphered_key:
                    res_str += str(i) + ", "

                with open("lab6/ciphered_key.txt", 'w+', encoding='utf-8') as file:
                    file.write(res_str)

            case "2":
                key = read_numbers("lab6/ciphered_key.txt")
                private_key_RSA = RSA.extract_data("lab6/private_key_for_RSA.txt")
                decrypted_key = RSA.decrypt(private_key_RSA, key)
                key_hex = DES.string_to_hex(decrypted_key)

                des_encryptor = DES.DES(pt_file='lab6/mumu.txt', enc_file='lab6/encrypted.txt', key=key_hex, mode='encrypt')
                print(f"Зашифрованный файл сохранён\n")

            case "3":
                key = read_numbers("lab6/ciphered_key.txt")
                private_key_RSA = RSA.extract_data("lab6/private_key_for_RSA.txt")
                decrypted_key = RSA.decrypt(private_key_RSA, key)
                key_hex = DES.string_to_hex(decrypted_key)
            
                des_decryptor = DES.DES(enc_file='lab6/encrypted.txt', dec_file='lab6/decrypted.txt', key=key_hex, mode='decrypt')
                print(f"Расшифрованный файл сохранён\n")

if __name__ == "__main__":
    menu()