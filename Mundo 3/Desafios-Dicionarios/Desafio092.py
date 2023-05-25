from datetime import date
dados = dict()
anoat = date.today().year

while True:
    dados['nome'] = str(input('Nome:')).capitalize().strip()
    anasc = int(input('Ano de nascimento:'))
    dados['idade'] = (anoat - anasc)-1
    dados['ctps'] = int(input('Carteira de Trabalho(0 não tem):'))
    if dados['ctps'] == 0:
        break
    dados['contratação'] = int(input('Ano de contratação:'))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratação'] - anasc) + 35
    break

print('-='*40)
print(f'nome tem o valor {dados["nome"]}')
print(f'idade tem o valor {dados["idade"]}')
print(f'ctps tem o valor {dados["ctps"]}')
print(f'contratação tem o valor {dados["contratação"]}' if dados['ctps'] > 0 else '')
print(f'salário tem o valor {dados["salario"]}' if dados['ctps'] > 0 else '')
print(f'aposentadoria tem o valor {dados["aposentadoria"]}' if dados['ctps'] > 0 else '')


