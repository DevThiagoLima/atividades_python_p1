c = 0
acumuladora = 0
somaNotas = 0

while c != -1:

    c = float(input('Digite a nota do aluno : '))
    if c != -1:
        somaNotas = somaNotas + c
        acumuladora = acumuladora + 1

media = somaNotas / acumuladora

print(f'{media:.2f}')
