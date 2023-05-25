s = 0
for n in range(0, 4):  # vai de 0 a 4 (roda 5x desconsidera o 6)
    n = int(input('Digite um número:'))
    s += n
print(s)

# ===============================
# Exemplo de enumerate (for com indices)
lista = ['Thiago', 'Gabriel']
for c, p in enumerate(lista):
    print(p)