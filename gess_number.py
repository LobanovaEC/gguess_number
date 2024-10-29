import random
n = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(st):
    if st.isdigit() and 1 <= int(st) <= 100:
        return True
    else:
        return False
counter = 0
while True:
    num = input('Введите целое число от 1 до 100 :', )
    counter += 1
    if is_valid(num):
        num = int(num)
        if num > n:
            print('Ваше число больше загаданного, попробуйте еще разок')

        elif num < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')

        else:
            print('Вы угадали, поздравляем!')
            print('Число попыток:', counter)
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

