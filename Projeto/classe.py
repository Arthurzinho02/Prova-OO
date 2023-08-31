class ToDoList:
    def __init__(self):
        self.lista = []

    def adicionar_tarefa(self, descricao: str):
        self.lista.append(descricao)
        print("Tarefa adicionada")
        

    def excluir_tarefa(self, indice: int):
        self.lista.pop(indice - 1)
        print("Tarefa excluida")

    def listar_tarefas(self):
        n = 0
        for i in self.lista:
            n += 1
            print(f"{n}. {i}")
