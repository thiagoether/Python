dicio1 = {}  # declaração de dicionário 1
dicio2 = dict()  # declaração de dicionário 2

dados3 = {'nome': 'Thiago', 'idade': 30}  # items de dentro de dados
dados3['sexo'] = 'M'  # adicionar elemento em dados
del dados3['idade']  # deletar idade de dados
dados3['nome'] = 'Alguém'  # substitui o item

# FUNCIONALIDADES
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }
print(filme.values())  # retorna todos os valores do dicionário (Star Wars, 1977 e George Lucas)
print(filme.keys())  # retorna todos os indices (titulo, ano e diretor)
print(filme.items())  # retorna tudo, valores e indices

for k, v in filme.items():
    print(f'O {k} é {v}')

# UMA LISTA COM VÁRIOS DICIONÁRIOS
locadora = [
    {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
    {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
    {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowsky'}
]
print(locadora[0]['ano']) # retorna 1977
print(locadora[2]['titulo']) #retorna matrix

estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Estado:'))
    estado['sigla'] = str(input('Sigla:'))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')

# COLOCANDO DICIONARIO EM ORDEM
numeros = {'Pessoa 1':3, 'pessoa 2':5, 'pessoa 3':7, 'pessoa 4':2}
for n in sorted(numeros, key = numeros.get):
    print(n, numeros[n])
# ORDEM REVERSA
for n in sorted(numeros, key = numeros.get, reverse=True):
    print(n, numeros[n])