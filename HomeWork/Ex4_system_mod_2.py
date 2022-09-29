# Ex4_system_mod_2 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите натуральное число n = '))
string_binary = ''
res = n
while res > 0:
    string_binary += str(res % 2)
    res //= 2
print(f'число {n} в двоичной системе --> {string_binary[: : -1]}')