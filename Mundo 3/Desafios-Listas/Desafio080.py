lista = list()

for c in range(5):
    n = int(input('Digite um numero:'))

    inseriu = True
    for cc in range(len(lista)):
        if n < lista[cc]:
            lista.insert(cc, n)
            inseriu = False
            break
    if inseriu:
        lista.append(n)
print(f'Os valores digitados em ordem foram {lista}')

# SOLUÇÃO DE GUANABARA
# lista = []
#
# for c in range(0, 5):
#    n = int(input('Digite um valor:'))
#    if c == 0 or n > lista[-1]:
#        lista.append(n)
#        print('Adicionado ao final da lista..')
#    else:
#        pos = 0
#        while pos < len(lista):
#            if n <= lista[pos]:
#                lista.insert(pos, n)
#                print(f'Adicionado na posição {pos} da lista')
#                break
#            pos += 1
# print('-=' * 30)
# print(f'Os valores digitados em ordem foram {lista}')

