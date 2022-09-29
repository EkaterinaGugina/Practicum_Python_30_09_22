# Ex4_system_mod_2 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def fib(k):
    if k > 1:
        return fib(k - 1) + fib(k - 2)
    else:
        if k == 1:
            return 1
        if k == 0:
            return 0
n = int(input('Введите натуральное число n = '))
array_fib = [0] *(2*n + 1)
for i in range(2*n + 1):
    if i < n:
        array_fib[i] = ((-1)**(i+1)) * fib(n - i)
    elif i > n: array_fib[i] = fib(i - n)
print(array_fib)