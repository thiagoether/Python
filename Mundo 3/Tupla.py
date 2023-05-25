from random import randint
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#TUPLAS SÃO IMUTÁVEIS

#METODO 1
for c in lanche:
    print(c)
#METODO 2
for c in range(len(lanche)):
    print(lanche[c])

#METODO 3
for pos, c in enumerate(lanche):
    print(f'Vou comer {c} na posição {pos}')

# VALORES ALEATORIOS EM TUPLAS
tupla = (randint(1,10), randint(1,10), randint(1,10))
print(tupla)
print(f'maior valor {max(tupla)}')
print(f'menor valor {min(tupla)}')

# sorted(tupla) A FUNÇÃO SORTED MOSTRA A TUPLA EM ORDEM ALFABETICA
# tupla.index('nome') MOSTRA  A POSIÇÃO DO NOME NA TUPLA