def x_pow (x, y):
    try:
        x, y = float(x), int(y)
        if x<=0 or y>=0:
            return 'Значения должны быть больше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
            return f'Результат: {round(result, 6)}'
    except ValueError:
        return 'Введите числа'

print(x_pow(2,-3))

