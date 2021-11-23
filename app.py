import db
import msg

def main():
    INITIAL_MENU = 0
    NEW_TODO = 1
    COMPLETE_TODO = 2
    REMOVE_TODO = 3

    while True:
        msg.show_header()
        msg.show_todos()

        try:
            print("Escolha uma das opções:")
            print("1 - Adicionar tarefa\n2 - Concluir tarefa\n3 - Excluir tarefa")
            option = int(input("Opção: "))

            if option == NEW_TODO:
                msg.show_option_new_todo()
            elif option == COMPLETE_TODO:
                msg.show_option_complete_todo()
            elif option == REMOVE_TODO:
                msg.show_option_remove_todo()
            elif option == INITIAL_MENU:
                msg.show_header()
            else:
                print("Opção inválida, por favor, digite o número 1 ou o 2.")
        except ValueError as error:
            print("Opção inválida, por favor, digite o número 1 ou o 2.")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.create_todo_table()
    main()
