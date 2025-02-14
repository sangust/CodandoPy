n1 = int(input('escolha um numero para somar'))
n2 = int(input('escolha outro numero para somar'))
s = n1 + n2
print('a soma entre {} e {} é igual a {}!' .format(n1, n2, s))
if s >= 0:
    print('seu numero é maior que zero')