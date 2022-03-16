num1 = input('Digite um número inteiro: ')

if num1.isdigit():
    if int(num1) % 2 == 0:
        print('Seu número é par')
    else:
        print('Seu número é ímpar')
else:
    print('Favor insira um número inteiro!!!!')

hora1 = input('Favor insira a hora atual: ')

if hora1.isdigit():
    hora1 = int(hora1)
    if hora1 < 12:
        print('Bom dia!')
    elif hora1 < 18:
        print('Boa tarde!')
    elif hora1 <= 24:
        print('Boa noite!')
    else:
        Print('Favor insira um numero entre 0 e 24')
else:
    print('Favor insira um número INTEIRO!')



