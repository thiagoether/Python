aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado!'
elif aluno['média'] < 7 and aluno['média'] >=5:
    aluno['situação'] = 'Recuperação!'
else:
    aluno['situação'] = 'Reprovado!'
print('-='*20)
for k, v in aluno.items():
    print(f'{"-":>3} {k} é igual a {v}')