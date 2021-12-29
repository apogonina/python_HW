def div(*args):

    try:
        arg1 = int(input('Введите число'))
        arg2 = int(input('Введите число'))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'Ошибка! Делить на 0 нельзя'

    return res

print(f'result  {div()}')
