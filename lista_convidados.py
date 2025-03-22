"""
Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições ,
pois algumas pessoas foram convidadas mais de uma vez por engano.
Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.
"""

convidados = set()

while True:
    nome = input("Digite o nome do convidado: ").lower()
    if nome == "sair":
        break
    convidados.add(nome)

print(f"Convidados confirmados: {','.join(convidados)}")
