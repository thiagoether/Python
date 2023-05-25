def notas(*notas, sit=False):
    """
     notas(*n, sit=False)
     -> função para analisar notas e situações de vários alunos.
     :param notas: uma ou mais notas dos alunos (aceita várias).
     :param sit: valor opcional, indicando se deve ou não adicionar situação
     :return: dicionário comváris informações sobre a situação do aluno
     """
    menor = maior = c = tot = 0
    aluno = dict()
    for n in notas:
        tot += n
        if c == 0:
            menor = n # adicionando valor a menor de inicio
        if n > maior:
            maior = n # pegando a maior nota
        if n < menor:
            menor = n # pegando a menor nota
        c += 1

    med = tot / c

    aluno['total'] = c
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['média'] = med
    if med < 5:
        aluno['situação'] = 'RUIM'
    elif med >= 5 and med < 7:
        aluno['situação'] = 'MEDIOCRE'
    else:
        aluno['situação'] = 'BOA'
    if sit == True:
        return aluno
    else:
        del aluno['situação']
        return aluno




print(notas(2, 6.5, 7))