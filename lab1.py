def help_def_no_key(symbol):
    new = ''
    for row in range(6):
        for colmn in range(6):
            if polibius_alph[row][colmn] == symbol.upper():
                new = f'{row}{colmn}'
                return new

def help_def_with_key(symbol, key):
    new = ''
    for row in range(6):
        for colmn in range(6):
            if polibius_alph[row][colmn] == symbol.upper():
                new = f'{key[row]}{key[colmn]}'
                return new

def encrypt(text, key):
    match key:
        case '0':
            with open(text, 'r', encoding='utf-8') as f:
                new_text = ''
                for i in f.readlines():
                    for j in i:
                        new_text += help_def_no_key(j)
            with open('c:\EmilyVolkova\VUZ\Shifrovanie\encrypted_mumu.txt', 'w', encoding='utf-8') as f2:
                f2.write(new_text)
        case any:
            with open(text, 'r', encoding='utf-8') as f:
                new_text = ''
                for i in f.readlines():
                    for j in i:
                        new_text += help_def_with_key(j, key)
            with open('c:\EmilyVolkova\VUZ\Shifrovanie\encrypted_mumu.txt', 'w', encoding='utf-8') as f2:
                f2.write(new_text)

def decrypt(text, key):
    match key:
        case '0':
            with open(text, 'r', encoding='utf-8') as f:
                enc_text = f.readlines()[0]
                new_text = ''
                for i in range(0, len(enc_text), 2):
                    try:
                        new_text += polibius_alph[int(enc_text[i])][int(enc_text[i+1])]
                    except IndexError:
                        break
            with open('c:\EmilyVolkova\VUZ\Shifrovanie\decrypted_mumu.txt', 'w', encoding='utf-8') as f2:
                f2.write(new_text)
        case any:
            with open(text, 'r', encoding='utf-8') as f:
                enc_text = f.readlines()[0]
                new_text = ''
                for i in range(0, len(enc_text), 2):
                    try:
                        new_text += polibius_alph[key.index(enc_text[i])][key.index(enc_text[i+1])]
                    except IndexError:
                        break
            with open('c:\EmilyVolkova\VUZ\Shifrovanie\decrypted_mumu.txt', 'w', encoding='utf-8') as f2:
                f2.write(new_text)

polibius_alph = [
    ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
    ['Ё', 'Ж', 'З', 'И', 'Й', 'К'], 
    ['Л', 'М', 'Н', 'О', 'П', 'Р'],
    ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
    ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
    ['Э', 'Ю', 'Я', ' ', '.', ',']
]

path_en = 'c:/EmilyVolkova/VUZ/Shifrovanie/mumu.txt'
path_dec = 'c:\EmilyVolkova\VUZ\Shifrovanie\encrypted_mumu.txt'

while True:
    choice = input('Меню:\n1. Зашифровать\n2. Расшифровать\n^: ')
    match choice:
        case '1':
            key = input('Ключ: ')
            if (key != 0) or (len(key) == 6):
                encrypt(path_en, key)
            else:
                print('Неверный ключ')
            break
        case '2':
            key = input('Ключ: ')
            if (key != 0) or (len(key) == 6):
                decrypt(path_dec, key)
            else:
                print('Неверный ключ')
            break
        case any:
            print("\nВведите верный вариант\n")