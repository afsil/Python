def saudacao(saudacao = 'olá', nome = 'anonimo'):
    print(saudacao, nome)

saudacao()

def soma(x, y, z):
    print(x + y + z)

soma(1, 2, 4)

def fizzbuzz(x):
    if x%5 == 0 and x%3 == 0:
        return 'fizzbuzz'
    elif x%3 == 0:
        return 'fizz'
    elif x%5 == 0:
        return 'buzz'
    else:
        return x

print(fizzbuzz(15))