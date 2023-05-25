cidade = input('Digite o nome da sua cidade:').strip().title()
c = 'Santo' in cidade.split()[0]
if c == True:
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com santo')
