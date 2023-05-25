seq = int(input('Digite um numero:'))
t = []

for c in range(5, seq + 5):
    t.append((c-1)+(c-2))

for c in range(seq):
    print(t[c], end=' ')

# 0 1 1 2 3 5 8 13 21
