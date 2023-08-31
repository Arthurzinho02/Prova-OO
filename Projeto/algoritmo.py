from classe import *
import os
def main():
    objeto = ToDoList()
    print("Bem vindo ao ToDoList")
    menu = True
    while menu == True:
        try:
            deseja = input("O que deseja fazer: \n[1]Adicionar \n[2]Excluir \n[3]Listar \n[4]Sair \n-")
            os.system("cls")

            match deseja:
                case "1":
                    descri = input("Digite a tarefa: ")
                    objeto.adicionar_tarefa(descri)
                    os.system("pause")
                    os.system("cls")
                case "2":
                    index = int(input("Qual é o numero da tarfe que deseja excluir \n-"))
                    objeto.excluir_tarefa(index)
                    os.system("pause")
                    os.system("cls")
                case "3":
                    objeto.listar_tarefas()
                    os.system("pause")
                    os.system("cls")
                case  "4":
                    menu = False
                case '_':
                    print("Opção inválida")
                    os.system("pause")
                    os.system("cls")


        except Exception as erro:
            print("Valor inválido")
            print(erro.__class__.__name__)
            os.system("pause")
            os.system("cls")
