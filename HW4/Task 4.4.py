from random import randint
from time import perf_counter

my_list = [randint(-1000,1000) for _ in range(2000)]

uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(uniq_list)
