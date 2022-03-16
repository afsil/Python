"""
Ativar "F-strings" com o um "f"
"""
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
#imc com duas casa decimais
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))