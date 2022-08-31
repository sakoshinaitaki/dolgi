def binary_search():
    span = int(input('Введи число от 1 до '))

    l1st = [i for i in range(1, span + 1)]
    a = 1
    b = l1st[-1]
    ResultOk = False

    while True:
        c = (a + b)//2
        if a < b:
            number = input('Ваше число:{}?( да, > или <)\n'.format(c))
            if number.lower() == 'да':
                a = c
                b = a
                ResultOk = True
            elif number == '>':
                a = c + 1
            elif number == '<':
                b = c - 1
            else:
                print('Вводите только да, > или <')
                continue

        else:
            if ResultOk == True:
                print(f'Вы загадали {c} ')
                break
            else:
                print('Элемент не найден')
                break

binary_search()