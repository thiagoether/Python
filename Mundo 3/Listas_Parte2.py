galera = list()
dados = list()

for c in range(3):
    dados.append(str(input('Nome:')))
    dados.append(int(input('Idade:')))
    galera.append(dados[:])
    dados.clear()
    
print(galera)