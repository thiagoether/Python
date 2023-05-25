lanche = ['hamburguer', 'suco', 'pizza', 'pudim'] # lista usa colchete
lanche2 = lanche #ele iguala as listas de modo que se uma for alterada a outra também será
lanche2 = lanche[:] # dessa forma ele copia o que esta em lanche para dentro de lanche2


lanche.append('cookie') # adiciona elemento a lista
lanche.insert(1, 'cachorro-quente') #adicionar item na lista em uma posição especifica
lanche.remove('suco') # ele procura do inicio da lista e remove o primeiro elemento encontrado.
del lanche[0] # deleta item da lista
lanche.pop(2) #normalmente é para eliminar o ultimo se nao usar indice, mas pode passar o parametro para deletar um especifico
valores = list(range(4, 11)) # cria lista com range de 4 a 10
valores.sort() # ordena os valores da lista de forma crescente
valores.sort(reverse=True) # ordena os valores de forma decrescente
len(valores) # tamanho da lista

for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores): # pega o valor e o indice na estrutura de repetição
    print(f'na posição {c} en contrei o valor {v}!')
print('Cheguei ao final da lista.')

for c in range(0, 5): #adicionar valores a lista individualmente
    valores.append(int(input('Digite um valor:')))