"""
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes.
Elas querem um programa que mostre:
Quais itens apareceram nas duas listas
Quais foram exclusivos de Laura
Quais foram exclusivos da Ana
Escreva um programa que solicite as listas e mostre os resultados dessas comparações.
"""

lista1 = set((input("Lista de Laura: ")).split(", "))
lista2 = set((input("Lista de Ana: ")).split(", "))

itens_iguais = (lista1).intersection(lista2)

exclusive_laura = (lista1).difference(lista2)

exclusive_ana = (lista2).difference(lista1)

print(f"Itens em ambas as listas: {", ".join(itens_iguais)}")

print(f"Itens exclusivos de Laura: {", ".join(exclusive_laura)}")

print(f"Itens exclusivos de Ana: {", ".join(exclusive_ana)}")


# leite, pão, café, açúcar
# pão, café, biscoito, chocolate
