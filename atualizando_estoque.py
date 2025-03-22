"""
Ana percebeu que, após o cadastro inicial dos produtos,
precisa atualizar a quantidade de um item específico no estoque.
Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade,
atualizando essa informação no dicionário de estoque.
"""

estoque = {"Caderno universitário": 50, "Caneta azul": 120, "Borracha branca": 30}

item = input("Nome do produto a ser atualizado: ")

if item in estoque:
    quantidade = input("Nova quantidade: ")
    estoque[item] = int(quantidade)
    print(estoque)
else:
    print("Produto não encontrado no estoque.")
