import random


def password_generator():
    """ This Function will generate a Password according to given length.
    User will enter the number of characters and numbers he want in password.You can Choose
    symbols between this '!', '@', '#', '$', '%', '^', ' &', '*', '<', '>', '?' and Number from 0 to 9 along with all
    the alphabets of ABC."""
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols_list = ['!', '@', '#', '$', '%', '^', ' &', '*', '<', '>', '?']
    pwrd_length = int(input('Enter How Much Long Password You want: '))
    number_length = int(input('Enter How Many Numbers You Want: '))
    char_length = int(input('Enter How Many Characters You Want: '))
    symbol_length = int(input('Enter How Many Symbols You want: '))
    password_dic = {'characters': '', 'numbers': '', 'symbols': ''}
    while True:
        for j in range(char_length):
            random_letter = random.randint(0, 25)
            password_dic['characters'] = password_dic['characters'] + letters_list[random_letter]
        for k in range(number_length):
            random_number = random.randint(0, 9)
            password_dic['numbers'] = password_dic['numbers'] + str(number_list[random_number])
        for l in range(symbol_length):
            random_symbol = random.randint(0, 10)
            password_dic['symbols'] = password_dic['symbols'] + symbols_list[random_symbol]
        counter = sum([char_length, number_length, symbol_length])
        if counter == pwrd_length:
            break

    password = password_dic['characters'] + password_dic['numbers'] + password_dic['symbols']
    print(password)


password_generator()
