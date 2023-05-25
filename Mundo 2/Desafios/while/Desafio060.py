from math import factorial

n = int(input('Digite um numero:'))
f = factorial(n)
seq = ''
print(n, end='!= ')
while n > 1:
    print(n, end='x')
    n -= 1
print('1=', f)

# METODO 2
# n = int(input('Digite um numero para calcular o seu fatorial:'))
# c = n
# f = 1

# for c in range(c, 0, -1):
#    print('{}'.format(c), end='')
#    print('x' if c > 1 else '=', end='')
#    f *= c

# print('{}'.format(f))
