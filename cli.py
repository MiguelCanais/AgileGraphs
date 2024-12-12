import os
from utils import obtemTrimestres, obtemUltimosTrimestres
from graficos import criaGraficos
from calcula_info import parseExpressao, calculaExpressao, traduzExpressao, ehExpressaoValida


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
        print()
        print("Insira expressões para gráficos (q para parar):")
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

        if len(expressoes) == 0:
            return
        criaGraficos(expressoes, listaTrimestres)


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


    > vendas:prod1:ue
    x
    """


def calculaValoresPrompt():
    print()
    ans = 0
    ultimoTrimestre = obtemUltimosTrimestres(1)[0]

    print("Insira expressão para calcular (q para sair):")
    while True:
        userInput = obtemInput("> ", [])
        if userInput == "q":
            return

        if not ehExpressaoValida(userInput):
            print("Expressão Inválida")
            continue

        userInput = userInput.replace("ans", str(ans))
        expressao = parseExpressao(userInput)
        traduzExpressao(expressao)
        ans = calculaExpressao(expressao, ultimoTrimestre)

        print(ans)
        print()


opcoes = {
    "1": {"nome": "Cria gráficos", "funcao": criaGraficosPrompt},
    "2": {"nome": "Calcula valores", "funcao": calculaValoresPrompt},
    "3": {"nome": "Mostra valores", "funcao": mostraValoresPrompt},
    "q": {"nome": "Sair", "funcao": exit},
}


def prompt():
    os.system("clear")
    print("\n------ AgileGraphs ------\n")
    print("Escolha uma opção:")

    for key, opcao in opcoes.items():
        print(f"[{key}] - {opcao["nome"]}")

    print()

    userInput = obtemInput("", opcoes)
    opcoes[userInput]["funcao"]()
    prompt()
