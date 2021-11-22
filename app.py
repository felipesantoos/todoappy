import db
import msg

def main():
    NEW_TODO = 1
    COMPLETE_TODO = 2

    while True:
        msg.show_header()
        msg.show_todos()

        try:
            option = int(input("Escolha uma das opções:\n1 - Nova tarefa\n2 - Concluir tarefa\nOpção: "))

            if option == NEW_TODO:
                msg.show_option_new_todo()
            elif option == COMPLETE_TODO:
                msg.show_option_complete_todo()
            else:
                print("Opção inválida, por favor, digite o número 1 ou o 2.")
        except ValueError as error:
            print("Opção inválida, por favor, digite o número 1 ou o 2.")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.create_todo_table()
    main()
