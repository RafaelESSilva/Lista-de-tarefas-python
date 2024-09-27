'''Lista de Trefas em Python'''

lista_tarefas = ['fazer commpras']

# Função para exibir as tarefas
def exibir_tarefas():
    if lista_tarefas:
        print('\Sua lista de tarefas: ')
        for idx, tarefa in enumerate(lista_tarefas, start=1):
            print(f'{idx}.{tarefa}')
    else:
        print('\nNão a tarefas em sua lista')

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    tarefa = input('\n Descreva sua tarefa:')
    lista_tarefas.append(tarefa)
    print(f"Tarefa {tarefa} adicionada com sucesso: ")

# Função para remover uma tarefa
def remover_tarefa():
    exibir_tarefas()
    try:
        tarefa_idx = int(input('Informe o numero da tarefa que deseja remover: '))
        tarefa_removida = lista_tarefas.pop(tarefa_idx - 1)
        print(f'Tarefa {tarefa_removida} removida com sucesso! ')
    except (IndexError, ValueError):
        print("Número inválido. Tente novamente.")

def menu ():
    while True:
        print('\n menu')
        print('1.Exibir lista de tarefas')
        print('2.adicionar itens a lista de tarefas')
        print('3.remover item da lista')
        print('4.Sair')

        opcao = int(input('escolha umas das opçoes: '))

        if opcao == 1:
            exibir_tarefas()
        elif opcao == 2 :
            adicionar_tarefa()
        elif opcao == 3:
            remover_tarefa()
        elif opcao == 4:
            print("Saindo do gerenciador de tarefas...")
            break
        else:
            print('opcao invalida tente novamente.')
#inicia o programa.
menu()