import random

matriz = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

print('Matriz: ')
for linha in matriz:
    print(linha)

somaTotal = sum(sum(linha) for linha in matriz)

print(f'\nSoma de todos os valores da matriz: {somaTotal}')

matriz2 = [[valor * 3 for valor in linha] for linha in matriz]

print(f'\nMatriz 2 (Mat1 * 3): ')

for linha in matriz2:
    print(linha)
