import re


first_string = str(543298765432)
second_string = str(6543298765432)

def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


cnpj_Input = input('Insira o CNPJ: ')
cnpj_Input = remover_caracteres(cnpj_Input)
cnpj_sem_dv = cnpj_Input[0:12]

def calcula_primeiro_digito(cnpj):
    soma_digitos = 0
    for i, j in enumerate(cnpj):
        soma_digitos += int(j) * int(first_string[i])
    primeiro_digito = 11 - (soma_digitos % 11)
    if primeiro_digito > 9:
        primeiro_digito = 0
    return primeiro_digito

def calcula_segundo_digito(cnpj):
    soma_digitos = 0
    for i, j in enumerate(cnpj):
        soma_digitos += int(j) * int(second_string[i])
    segundo_digito = 11 - (soma_digitos % 11)
    if segundo_digito > 9:
        segundo_digito = 0
    return segundo_digito


def valida(cnpj):
    primeiro_digito = calcula_primeiro_digito(cnpj)
    cnpj2 = cnpj + str(primeiro_digito)
    segundo_digito = calcula_segundo_digito(cnpj2)
    cnpj_calculado = cnpj2 + str(segundo_digito)
    if cnpj_calculado == cnpj_Input:
        print('CNPJ Correto')
    else:
        print('CNPJ Errado')

valida(cnpj_sem_dv)