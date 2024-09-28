real = float(input('Digite Quantas Moedas de 1 Real Você Tem: '))
centavos50 = float(input('Digite Quantas Moedas de 50 Centavos Você Tem: '))
centavos25 = float(input('Digite Quantas Moedas de 25 Centavos Você Tem: '))

totalReal = real * 1
totalCentavos50 = centavos50 * 0.50
totalCentavos25 = centavos25 * 0.25

total = totalReal + totalCentavos25 + totalCentavos50

print(f'Você tem {real} moedas de 1 Real, {centavos50} Moedas de 50 Centavos e {centavos25} Moedas de 25 Centavos, no total você tem: R$ {total:.2f}')
