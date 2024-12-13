import os
from utils import obtemTrimestres, obtemUltimosTrimestres
from graficos import criaGraficos
from calcula_info import calculaInfo, ehExpressaoValida, expandeExpressao


def obtemInput(promptText, inputValido: list[str] = []) -> str:
    """
    Obtem input do utilizador e verifica que o input é
    uma opcao valida
    """
    while True:
        userInput = input(promptText)

        if len(inputValido) != 0 and userInput not in inputValido:
            continue

        return userInput


def criaGraficosPrompt():
    listaTrimestres = obtemTrimestres()

    while True:
        print("\nInsira expressões para gráficos (q para parar):")
        expressoes = []

        while True:
            userInput = obtemInput("> ", [])
            if userInput == "q":
                if len(expressoes) == 0:
                    return
                break

            if not ehExpressaoValida(userInput):
                print("Expressão Inválida")
                continue

            expressoes.append(userInput)

        criaGraficos(expressoes, listaTrimestres)


def calculaValoresPrompt():
    ans = 0
    ultimoTrimestre = obtemUltimosTrimestres(1)[0]

    print("\nInsira expressão para calcular (q para sair):")
    while True:
        userInput = obtemInput("> ", [])
        if userInput == "q":
            return

        if not ehExpressaoValida(userInput):
            print("Expressão Inválida")
            continue

        userInput = userInput.replace("ANS", str(ans))
        info_graphs = calculaInfo([userInput], [ultimoTrimestre])

        if len(info_graphs) == 1:
            print(info_graphs[0][1][0])
        else:
            for expressao, info in info_graphs:
                print(f'{expressao}: {info[0]}')

        print()


def mostraValoresPrompt():
    """
    Calulca expressao:
    > vendas

             Prod1 Prod2 Prod3
    UE         x     x     x
    nafta      x     x     x
    internet   x     x     x


    > vendas:prod1

    UE       x
    nafta    x
    internet x


    > vendas:ue

    Prod1   x
    Prod2   x
    Prod3   x

    """
    ultimoTrimestre = obtemUltimosTrimestres(1)[0]

    print("\nInsira expressão para mostrar (q para sair):")
    while True:
        userInput = obtemInput("> ", [])
        if userInput == "q":
            return

        if not ehExpressaoValida(userInput):
            print("Expressão Inválida")
            continue

        # ans = calculaExpressao(expressao, ultimoTrimestre)

        print(ans)
        print()



OPCOES = {
    "1": {"nome": "Cria gráficos", "funcao": criaGraficosPrompt},
    "2": {"nome": "Calcula valores", "funcao": calculaValoresPrompt},
    "3": {"nome": "Mostra valores", "funcao": mostraValoresPrompt},
    "q": {"nome": "Sair", "funcao": exit},
}


def prompt():
    while True:
        os.system("clear")
        print("\n------ AgileGraphs ------\n")
        print("Escolha uma opção:")

        for key, opcao in OPCOES.items():
            print(f"[{key}] - {opcao["nome"]}")

        print()

        userInput = obtemInput("", OPCOES)
        OPCOES[userInput]["funcao"]()
