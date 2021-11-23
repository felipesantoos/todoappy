import db

INITIAL_MENU = 99

def show_header():
    COL_NUM = 60
    print("-" * COL_NUM)
    print("{:^60}".format("TASKS"))
    print("-" * COL_NUM)
    print("{:^60}".format("Digite 0 para voltar ao menu inicial ou Ctrl + C para sair."))
    # print("-" * COL_NUM)

def show_todos():
    for todo in db.get_todos():
        check = u'\u2713' if todo[2] == 1 else " "
        id = "[#" + str(todo[0]) + "]"
        print("- {:<5} {:<46} [{:^1}]".format(id, todo[1], check))
    print("-" * 60)

def show_option_new_todo():
    task = input("Digite a descrição da tarefa: ")
    if (task != INITIAL_MENU):
        db.add(task)

def show_option_complete_todo():
    id = int(input("Digite o código da tarefa que quer concluir: "))
    if (id != INITIAL_MENU):
        db.complete(id)

def show_option_remove_todo():
    id = int(input("Digite o código da tarefa que deseja excluir: "))
    if (id != INITIAL_MENU):
        db.remove(id)


