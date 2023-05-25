from time import sleep

def contador(i, f, r):
    if r < 0:
        for c in range(i, f+r, r):
            sleep(0.5)
            print(c, end=' ')
    elif r == 0:
        p = 1
        for c in range(i, f+p, p):
            sleep(0.5)
            print(c, end=' ')
    else:
        if i <= f:
            for c in range(i, f, r):
                sleep(0.5)
                print(c, end=' ')
        else:
            for c in range( i, f-r, r*-1):
                sleep(0.5)
                print(c, end=' ')


    print('FIM!')


print('-='*20)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)

print('-='*20)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)



# 10 até 100 de 8 em 8
# 90 até 40 voltando de 10 em 10
# se o valor do passo for negativo
# se o valor do passo for 0 considerar 1
