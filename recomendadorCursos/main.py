from db_operations import (
    cadastrar_aluno,
    cadastrar_curso,
    registrar_realizacao,
    recomendar_cursos,
    listar_cursos,
    listar_alunos
)

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar aluno")
        print("2. Cadastrar curso")
        print("3. Registrar realização")
        print("4. Recomendar cursos")
        print("5. Listar cursos")
        print("6. Listar alunos")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")
            interesses = input("Interesses (separados por vírgula): ").split(",")
            interesses = [i.strip() for i in interesses]
            cadastrar_aluno(nome, idade, curso, interesses)

        elif opcao == "2":
            titulo = input("Título do curso: ")
            area = input("Área do curso: ")
            nivel = input("Nível (Fácil/Médio/Avançado): ")
            cadastrar_curso(titulo, area, nivel)

        elif opcao == "3":
            nome = input("Nome do aluno: ")
            curso = input("Título do curso: ")
            registrar_realizacao(nome, curso)

        elif opcao == "4":
            nome = input("Nome do aluno para recomendação: ")
            print("Recomendando cursos...")
            recomendar_cursos(nome)

        elif opcao == "5":
            listar_cursos()

        elif opcao == "6":
            listar_alunos()

        elif opcao == "7":
            print("Encerrando.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
