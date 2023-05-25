def aumentar(p, porc):
    a = p + ((p*porc)/100)
    return a


def diminuir(p, porc):
    m = p - (p*(porc/100)) # m recebe preço - preço * porcentagem / 100
    return m


def dobro(p):
    d = p * 2
    return d


def metade(p):
    m = p / 2
    return m