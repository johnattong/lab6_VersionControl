def encode(password):
    encoded_password = ''
    for i in password:
        i = int(i) + 3
        encoded_password += str(i)
    return encoded_password


def main():
    choice = 0
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        choice = int(input('\nPlease enter an option: '))
        if choice == 1:
            password = (input('Please enter your password to encode: '))
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')
        elif choice == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {password}.\n')
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
