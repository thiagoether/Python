#FUNÇÕES SEMPRE COM 2 LINHAS DE DISTÂNCIA
#FUNÇÃO DE MOSTRAR A LINHA
def ml():
    print('='*30)


ml()


#FUNÇÃO RETORNA MENSAGEM
def mensagem(msg):
    print('-'*(len(msg)))
    print(msg)
    print('-'*(len(msg)))


mensagem(f'{"THIAGO":^30}')


#FUNÇÃO DE SOMA
def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(a=5, b=2)


#CONTADOR DE NUMEROS
def contador(*num): # ao usar * você esta dizendo que num vai receber vários numeros (tipo lista)
    for v in num:
        print(v)

# Interactive Help:
# Console -> help()
# print(comando.__doc__)

# docstrings //documentação da sua função
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     """

# Argumentos Opcionais // declarar valor a variavel para assim se necessario usar menos entradas quando chamar a função
# def somar(a, b, c=0):
#    s = a + b + c
#    print(f'A soma vale {s}')
# somar(8, 4)

# Escopo de variáveis
#def teste(b):
#    global a
#    a = 8
#    b += 4
#    c = 2
#    print(f'A dentro vale {a}')
#    print(f'B dentro vale {b}')
#    print(f'C dentro vale {c}')
#
#
#a = 5
#teste(a)
#print(f'A fora vale {a}')

# Retorno de Resultados
