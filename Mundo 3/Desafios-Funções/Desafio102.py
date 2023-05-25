def fatorial(n=0, show=False):
    """
    ->CALCULO DE FATORIAL
    :param n: É o numero a ser calculado
    :param show: (opcional) mostra o processo de calculo
    :return: O valor do fatorial do numero n
    """
    f = 1
    if show == True:
        for n in range(n, 0, -1):
            f *= n
            print(f'{n} x' if n > 1 else '=', end=' ')
    else:
        for n in range(n, 0, -1):
            f *= n
    return f


print(fatorial(5, show=False))
help(fatorial)
