lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_c = []
for i, j in zip(lista_b,lista_b):
    lista_c.append(float(i) + float(j))

print(lista_c)