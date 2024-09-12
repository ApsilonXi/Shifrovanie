def encrypt(text, key):
    match key:
        case '0':
            with open(text, 'r', encoding='utf-8') as f:
                new_text = ''
                for i in f.readlines():
                    for j in i:
                        for row in range(6):
                            for colmn in range(6):
                                if polibius_alph[row][colmn] == j.upper():
                                    new_text += f'{row}{colmn}'
                                    continue
                                

            with open('c:\EmilyVolkova\VUZ\Shifrovanie\encrypted_mumu.txt', 'w', encoding='utf-8') as f2:
                f2.write(new_text)
        case any:
            pass

def decrypt(text, key):
    match key:
        case '0':
            with open(text, 'r', encoding='utf-8') as f:
                enc_text = f.readlines()
                print(enc_text)
                new_text = ''
                for i in range(0, len(enc_text), 2):
                    print(i, enc_text[i], enc_text[i+1])
                    try:
                        new_text += polibius_alph[int(enc_text[i])][int(enc_text[i+1])]
                    except IndexError:
                        break

            with open('c:\EmilyVolkova\VUZ\Shifrovanie\decrypted_mumu.txt', 'w', encoding='utf-8') as f2:
                f2.write(new_text)

                    
        case any:
            pass

polibius_alph = [
    ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
    ['Ё', 'Ж', 'З', 'И', 'Й', 'К'], 
    ['Л', 'М', 'Н', 'О', 'П', 'Р'],
    ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
    ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
    ['Э', 'Ю', 'Я', '.', ',', '?']
]

path_en = 'c:/EmilyVolkova/VUZ/Shifrovanie/mumu.txt'
path_dec = 'c:\EmilyVolkova\VUZ\Shifrovanie\encrypted_mumu.txt'

while True:
    choice = input('Меню:\n1. Зашифровать\n2. Расшифровать\n^: ')
    match choice:
        case '1':
            key = input('Ключ: ')
            encrypt(path_en, key)
            break
        case '2':
            key = input('Ключ: ')
            decrypt(path_dec, key)
            break
        case any:
            print("\nВведите верный вариант\n")