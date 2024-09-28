from time import sleep

cadastNome = input('Digite o nome para cadastro: ')
cadastIdade = input('Digite a idade para cadastro: ')
cadastEmail = input('Digite o email para cadastro: ')

print('Dados Salvos!')
sleep(5)

print('Vamos Realizar o Login: ')
sleep(3)

loginNome = input('Digite o nome de login: ')
loginIdade = input('Digite a sua idade: ')
loginEmail = input('Digite seu email de login: ')

if loginNome == cadastNome and loginIdade == cadastIdade and loginEmail == cadastEmail:
    print('Login Realizado Com Sucesso!')
else:
    print('Alguma das informações está errada!')
