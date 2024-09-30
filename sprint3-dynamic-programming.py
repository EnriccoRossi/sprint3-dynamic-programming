professores = {
    "Jose Ferreira": "jf1234",
    "Pedro Augusto": "pa1234"
}

salas = {
    "Jose Ferreira": {
        "sala1": {
            "alunos": ["Maria", "João", "Ana", "Carlos", "Fernanda"],
            "atividades": ["Trabalho de História", "Projeto de Ciências"]
        },
        "sala2": {
            "alunos": ["Lucas", "Camila", "Pedro", "Juliana", "Roberto"],
            "atividades": ["Prova de Matemática", "Redação de Português"]
        },
        "sala3": {
            "alunos": ["Laura", "Gabriel", "Isabela", "Rafael", "Tatiane"],
            "atividades": ["Experimento de Física", "Apresentação de Geografia"]
        }
    },
    "Pedro Augusto": {
        "sala1": {
            "alunos": ["Ana", "Felipe", "Sofia", "André", "Luiza"],
            "atividades": ["Exercício de Artes", "Relatório de Biologia"]
        },
        "sala2": {
            "alunos": ["Marcos", "Beatriz", "Renato", "Gisele", "Eduardo"],
            "atividades": ["Debate de História", "Leitura de Literatura"]
        },
        "sala3": {
            "alunos": ["Clara", "Vinícius", "Bianca", "Samuel", "Patrícia"],
            "atividades": ["Projeto de Tecnologia", "Pesquisa de Química"]
        }
    }
}


def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in professores and professores[usuario] == senha:
        return usuario
    else:
        print("Usuário ou senha incorretos.")
        return None


def mostrar_salas(usuario):
    print("\nSalas de aula:")
    for sala in salas[usuario]:
        print(f"Sala: {sala}")
        print("Alunos:")
        for aluno in salas[usuario][sala]["alunos"]:
            print(f"- {aluno}")
        print("Atividades:")
        for atividade in salas[usuario][sala]["atividades"]:
            print(f"- {atividade}")
        if not salas[usuario][sala]["atividades"]:
            print("- Nenhuma")


def criar_sala(usuario):
    nova_sala = input("Nome da nova sala: ")
    salas[usuario][nova_sala] = {"alunos": [], "atividades": []}
    print(f"Sala '{nova_sala}' criada.")


def adicionar_aluno(sala, usuario):
    aluno = input("Nome do aluno a adicionar: ")
    salas[usuario][sala]["alunos"].append(aluno)
    print(f"Aluno '{aluno}' adicionado à sala '{sala}'.")


def criar_atividade(sala, usuario):
    atividade = input("Nome da nova atividade: ")
    salas[usuario][sala]["atividades"].append(atividade)
    print(f"Atividade '{atividade}' criada na sala '{sala}'.")


def menu_principal(usuario):
    while True:
        print("\nMenu:")
        print("1. Mostrar salas de aula")
        print("2. Criar nova sala")
        print("3. Adicionar aluno a uma sala")
        print("4. Criar nova atividade em uma sala")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrar_salas(usuario)
        elif opcao == '2':
            criar_sala(usuario)
        elif opcao == '3':
            sala = input("Digite o nome da sala: ")
            if sala in salas[usuario]:
                adicionar_aluno(sala, usuario)
            else:
                print("Sala não encontrada.")
        elif opcao == '4':
            sala = input("Digite o nome da sala: ")
            if sala in salas[usuario]:
                criar_atividade(sala, usuario)
            else:
                print("Sala não encontrada.")
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


def mostrar_todas_as_informacoes(usuario):
    print("\nInformações finais:")
    mostrar_salas(usuario)


def main():
    usuario = login()
    if usuario:
        menu_principal(usuario)
        mostrar_todas_as_informacoes(usuario)


if __name__ == "__main__":
    main()
