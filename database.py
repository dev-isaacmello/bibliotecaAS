import json
from time import sleep

class Database:
    def __init__(self, filename="database.json"):
        self.filename = filename
        self.data = {
            'livros': [],
            'usuarios': []
        }
        self.carregar()

    def carregar(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Arquivo {self.filename} não encontrado. Criando um novo arquivo...")
            sleep(2)
            self.salvar()
    def salvar(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

