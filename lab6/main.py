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
                RSA.create_keys()
                public_key = RSA.read_keys("lab6/public_key.txt")
                ciphered_key = RSA.encrypt(public_key, key)

                enc_key = ""
                for i in ciphered_key:
                    enc_key += str(i) + ", "

                with open("lab6/ciphered_key.txt", 'w+', encoding='utf-8') as file:
                    file.write(enc_key)

            case "2":
                key = read_numbers("lab6/ciphered_key.txt")
                private_key = RSA.read_keys("lab6/private_key.txt")
                decrypted_key = RSA.decrypt(private_key, key)
                key_hex = DES.string_to_hex(decrypted_key)

                des_encryptor = DES.DES(pt_file='lab6/mumu.txt', enc_file='lab6/encrypted.txt', key=key_hex, mode='encrypt')

            case "3":
                key = read_numbers("lab6/ciphered_key.txt")
                private_key = RSA.read_keys("lab6/private_key.txt")
                decrypted_key = RSA.decrypt(private_key, key)
                key_hex = DES.string_to_hex(decrypted_key)
            
                des_decryptor = DES.DES(enc_file='lab6/encrypted.txt', dec_file='lab6/decrypted.txt', key=key_hex, mode='decrypt')

if __name__ == "__main__":
    menu()