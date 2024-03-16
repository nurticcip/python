import random

print('Игра начался!!!')

a = int(input('Первый диапазон: '))
b = int(input('Второй диапазон: '))

random_num = random.randint(a, b)

s = 0

while True:
    ans = int(input(f'Найдите числу в диапазоне от {a} до {b} ваш ответ: '))

    if ans < random_num:
        s += 1
        print('Это число меньше: ')
    elif ans > random_num:
        s += 1
        print('Это число больше: ')
    else:
        print('Поздравляю!!! Вы угадали  число за ' +str(s)+ ' попытки)')
        break