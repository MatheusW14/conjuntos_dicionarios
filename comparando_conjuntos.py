"""
Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas.
Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário.
Sua tarefa é criar um programa que realize essa operação.
"""

equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

tarefa_final = (equipe_a).union(equipe_b)

tarefa_remover = input("Tarefa a ser removida: ").lower()

if tarefa_remover in tarefa_final:

    tarefa_final.remove(tarefa_remover)

print(f"Tarefas finais: {tarefa_final}")
