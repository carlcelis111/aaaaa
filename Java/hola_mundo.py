pares = 0
impares = 0

for numero in range(1, 21):
    if numero % 2 == 0:
        print('par')
        pares += 1
    else:
        print('impares')
        impares += 1
print('Pares:', pares, 'Impares:', impares)
