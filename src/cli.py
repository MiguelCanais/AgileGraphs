from os import system

from graficos import criaGraficos
from calcula_info import calculaInfo, ehExpressaoValida
from prompt import obtemInputExpressao


def criaGraficosPrompt():
    """
    Aceita várias expressões do utilizador.
    Quando tentar voltar para o menu original ele irá mostrar um gráfico com os valores das expressões introduzidas
    para cada relatório para o qual as expressões sejam validas.
    Caso nenhuma expressão seja introduzida irá imediatamente voltar para o menu inicial.
    """
    while True:
        print("\nInsira expressões para gráficos (q para parar):")
        expressoes = []

        while True:
            userInput = obtemInputExpressao()
            if userInput == "q" or userInput == "":
                if len(expressoes) == 0:
                    return
                break

            if not ehExpressaoValida(userInput):
                continue

            expressoes.append(userInput)

        criaGraficos(expressoes)


def calculaValoresPrompt():
    """ Escreve o valor numérico da expressão dada em relação ao último relatório para o qual a expressão é válida."""
    ans = 0

    print("\nInsira expressão para calcular (q para sair):")
    while True:
        userInput = obtemInputExpressao()
        if userInput == "q" or userInput == "":
            return

        if not ehExpressaoValida(userInput):
            continue

        userInput = userInput.replace("ANS", str(ans))
        info_graficos = calculaInfo([userInput])

        if len(info_graficos) == 1:
            print(info_graficos[0][1][-1])
        else:
            for expressao, info in info_graficos:
                print(f'{expressao} = {info[-1]}')

        print()


def mostraValoresPrompt():
    """
    Mostra os valores numa tabela.
    É equivalente a substituir cada chave omitida por um ALL.

    Alguns exemplos:

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
    print("mostra valores ainda está em desenvolvimento, atualmente não faz nada")
    print("\nInsira expressão para mostrar (q para sair):")
    while True:
        userInput = obtemInputExpressao()
        if userInput == "q" or userInput == "":
            return

        if not ehExpressaoValida(userInput):
            continue

        # ans = calculaExpressao(expressao, ultimoTrimestre)

        # print(ans)
        print()



OPCOES = {
    "1": {"nome": "Cria gráficos", "funcao": criaGraficosPrompt},
    "2": {"nome": "Calcula valores", "funcao": calculaValoresPrompt},
    "3": {"nome": "Mostra valores", "funcao": mostraValoresPrompt},
    "q": {"nome": "Sair", "funcao": exit},
}


def prompt():
    """
    A função principal do programa.
    Gera um menu interativo onde se escolhe o modo a utilizar.
    Depois chama a função correspondente ao modo selecionado.
    """
    while True:
        system("clear")
        print("\n------ AgileGraphs ------\n")
        print("Escolha uma opção:")

        for key, opcao in OPCOES.items():
            print(f"[{key}] - {opcao["nome"]}")

        print()

        userInput = ""
        while userInput not in OPCOES:
            userInput = input("> ")

        OPCOES[userInput]["funcao"]()
