def area(a, b):
    area = a * b
    return area
    #print(f'A área de um terreno {a}x{b} é de {area}m².')


largura = float(input('Digite a largura do terreno:'))
comprimento = float(input('Digite o comprimento do terreno:'))
print(f'A área de um terreno {largura}x{comprimento} é de {area(largura, comprimento)}m².')