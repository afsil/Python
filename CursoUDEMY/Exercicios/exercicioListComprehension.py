string1 = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
lista1 = [string1[v:v + n] for v in range(0, len(string1), n)]
print(lista1)