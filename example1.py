true_password = 'qwerty123'
max_tries = 3
current_try = 1

while True:
    user_password = input('Введи пОроль: ')

    if user_password == true_password:
        print('Верно')
        break
    if current_try > max_tries
        print('Время вышло')
        break
    print('Пароль неверный. Осталось попыток ' max_tries - current_try)
    current_try -=1