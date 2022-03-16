cpf = input('Favor insira seu cpf (somente números): ')

first9 = cpf[0:9]


calc1 = 0

for i, j in enumerate(first9):
    calc1 += int(j) * (10-i)


if (11 - calc1 % 11) > 9:
    firstdigit = 0
else:
    firstdigit = 11 - (calc1 % 11)

first10 = first9 + str(firstdigit)

calc2 = 0

for i, j in enumerate(first10):
    calc2 += int(j) * (11-i)

if (11 - calc2 % 11) > 9:
    seconddigit = 0
else:
    seconddigit = 11 - (calc2 % 11)

cpfcalculado = first10 + str(seconddigit)

print(f'first digit = {firstdigit} and second digit = {seconddigit}')

if cpf == cpfcalculado:
    print("CPF válido!")
else:
    print('CPF inválido!')