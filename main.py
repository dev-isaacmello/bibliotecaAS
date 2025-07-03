from biblioteca_admin import BibliotecaAdmin
from database import  Database

def main():
    db = Database()
    biblioteca_admin = BibliotecaAdmin(db.data)

    while True:
        print("\nBem vindo ao Dashboard da Biblioteca da Ulbra!")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Listar Livros")
        print("4. Realizar Empréstimo")
        print("5. Sair")

        opcao = input("Escolha uma opção para continuar: ")

        if opcao == "1":
            titulo = input("Digite o titulo do livro: ")
            autor = input("Nome do autor do livro: ")
            ano = input("Ano de publicação: ")
            biblioteca_admin.cadastrar_livro(titulo, autor, ano)
        elif opcao == "2":
            nome = input("Digite o nome de usuário: ")
            cpf = input("Digite o CPF do usuário (11 dígitos): ")
            biblioteca_admin.cadastrar_usuario(nome, cpf)
        elif opcao == "3":
            biblioteca_admin.mostrar_livros()
        elif opcao == "4":
            cpf_usuario = input("Digite o CPF do usuário (11 dígitos): ")
            titulo_livro = input("Digite o título do livro que quer emprestar: ")
            biblioteca_admin.emprestar_livro(cpf_usuario, titulo_livro)
        elif opcao == "5":
            db.salvar()
            print("Serviço encerrado. Todos os dados foram salvos com sucesso!")
            break
        else:
            print("Ops! Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
