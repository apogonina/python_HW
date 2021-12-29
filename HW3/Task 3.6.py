def int_fun(word):
    char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(char) else False


words = input('Введите строку из слов с пробелами').split()
for w in words:
    result = int_fun(w)
    if result:
        print(int_fun(w), '')

