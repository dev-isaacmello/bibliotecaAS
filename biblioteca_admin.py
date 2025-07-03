class BibliotecaAdmin:
    def __init__(self, database):
        self.database = database

    def cadastrar_livro(self, titulo, autor, ano):
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "disponivel": True
        }
        self.database["livros"].append(livro)
        print(f"O livro '{titulo}' foi adicionado a biblioteca.")

    def cadastrar_usuario(self, nome, cpf):
        if len(cpf) !=  11 or not cpf.isdigit():
            print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
            return

        usuario = {
            "nome": nome,
            "cpf": cpf,
            "livro_emprestado": None
        }
        self.database["usuarios"].append(usuario)
        print(f"O usuário '{nome}' foi cadastrado com sucesso!")

    def mostrar_livros(self):
        print("Livros Disponíveis para emprestimo:")
        for livro in self.database["livros"]:
            if livro["disponivel"]:
                print(f" - {livro["titulo"]} por {livro["autor"]} ({livro["ano"]})")
        print("\nLivros Emprestados:")
        for livro in self.database["livros"]:
            if not livro["disponivel"]:
                print(f" - {livro["titulo"]} por {livro["autor"]} ({livro["ano"]})")
    def emprestar_livro(self, cpf, titulo):
        usuario = next((u for u in self.database["usuarios"] if u["cpf"] == cpf), None)
        livro = next((l for l in self.database["livros"] if l["titulo"] == titulo), None)

        if not usuario:
            print("Usuário não encontrado.")
            return
        if not livro:
            print("Esse livro não foi encontrado na biblioteca.")
            return
        if not livro["disponivel"]:
            print("Infelizmente este livro já foi emprestado para alguém...")
            return
        if usuario["livro_emprestado"]:
            print("O usuário já possui um livro em mãos, termine de ler ele primeiro antes de pegar outro!")
            return

        livro["disponivel"] = False
        usuario["livro_emprestado"] = titulo
        print(f"O livro '{titulo} foi emprestado para o usuário '{usuario["nome"]}'.")