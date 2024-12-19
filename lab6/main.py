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
        print("1. Шифрование ключа и дешифрование ключа\n2. Шифрование текста\n3. Дешифрование текста\n")
        choice = input("^: ")

        match choice:
            case "1":
                key = input("Input key: ")
                public_key_RSA = RSA.extract_data("lab6/keys/public_key_for_RSA.txt")
                
                ciphered_key = RSA.encrypt(public_key_RSA, key)

                res_str = ""
                for i in ciphered_key:
                    res_str += str(i) + ", "

                write_text_file(res_str, "lab6/keys/ciphered_key.txt")
                # decrypted_key = RSA.decrypt(private_key_RSA, ciphered_key)
                # write_text_file(decrypted_key, "laba 6/keys/decrypted key.txt")

            case "2":
                # key = read_text_file("lab6/keys/key.txt")
                key = RSA.read_numbers_from_file("lab6/keys/ciphered_key.txt")
                private_key_RSA = RSA.extract_data("lab6/keys/private_key_for_RSA.txt")
                decrypted_key = RSA.decrypt(private_key_RSA, key)
                key_hex = DES.string_to_hex(decrypted_key)

                des_encryptor = DES.DES(pt_file='lab6/mumu.txt', enc_file='lab6/encrypted.txt', key=key_hex, mode='encrypt')
                print(f"Зашифрованный файл сохранён\n")

            case "3":
                key = RSA.read_numbers_from_file("lab6/keys/ciphered_key.txt")
                private_key_RSA = RSA.extract_data("lab6/keys/private_key_for_RSA.txt")
                decrypted_key = RSA.decrypt(private_key_RSA, key)
                key_hex = DES.string_to_hex(decrypted_key)
            
                des_decryptor = DES.DES(enc_file='lab6/encrypted.txt', dec_file='lab6/decrypted.txt', key=key_hex, mode='decrypt')
                print(f"Расшифрованный файл сохранён\n")

if __name__ == "__main__":
    Start()