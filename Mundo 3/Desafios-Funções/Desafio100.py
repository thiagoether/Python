from time import sleep
numeros = list()

def sorteia():
    from random import randint
    from time import sleep
    lst = []
    for c in range(5):
        lst.append(randint(10, 99))
    return lst


def somaPAr(fn):
    par = 0
    for n in fn:
        if n % 2 == 0:
            par += n
    return par


numeros = sorteia() # ccolocando 5 numeros sorteados dentro da lista
print('Sorteando 5 valores da lista: ', end='')
for n in numeros:
    sleep(0.2)
    print(n, end=' ')
print('PRONTO!')
print(f'Somando os valores pares de {numeros} : temos {somaPAr(numeros)}', end=' ')