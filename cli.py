import os
from utils import obtemTrimestres, obtemUltimosTrimestres, expressaoValida
from graficos import criaGraficos
from calcula_info import parseExpressao,calculaExpressao,traduzExpressao

def obtemInput(promptText,inputValido: list[str]=[]) -> str:
    '''
    Obtem input do utilizador e verifica que o input é
    uma opcao valida
    '''
    userInput = input(promptText)

    if len(inputValido) == 0: return userInput
    if not userInput in inputValido: return obtemInput(promptText,inputValido)

    return userInput


def obtemInputNumero(promptText, minimo, maximo) -> int:
    '''
    Obtem input do utilizador como numero e verifica que esta
    entre o intervalo dado
    '''
    userInput = input(promptText)
    if not userInput.isdigit(): return obtemInputNumero(promptText,minimo,maximo)

    n = int(userInput)
    if n < minimo or n > maximo: return obtemInputNumero(promptText,minimo,maximo)

    return n


def obtemInputExpressao(promptText) -> str:
    '''
    Obtem input do utilizador como expressao e verifica que eh
    uma expressao valida
    '''
    userInput = input(promptText)
    
    if not expressaoValida(userInput): return obtemInputExpressao(promptText)
    return userInput


def criaGraficosPrompt():
    print()
    listaTrimestres = obtemTrimestres()

    print("Insira expressões para gráficos (q para parar):")

    expressoes = []

    while True:
        userInput = obtemInput("> ",[])
        if userInput == 'q': break

        if not expressaoValida(userInput):
            print("Expressão Inválida")
            continue

        expressoes.append(userInput) 

    if len(expressoes) == 0: return
    criaGraficos(expressoes,listaTrimestres)
    

def mostraValoresPrompt(): 
    '''
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
    '''

def calculaValoresPrompt():
    print()
    ultimoTrimestre = obtemUltimosTrimestres(1)[0]

    print("Insira expressão para calcular (q para sair):")
    while True:
        userInput = obtemInput("> ",[])
        if userInput == 'q': 
            prompt()
            return

        if not expressaoValida(userInput):
            print("Expressão Inválida")
            continue

        expressao = parseExpressao(userInput)
        traduzExpressao(expressao)
        print(calculaExpressao(expressao, ultimoTrimestre))
        print()

opcoes = {
    "1": {"nome": "Cria gráficos", "funcao": criaGraficosPrompt},
    "2": {"nome": "Calcula valores", "funcao": calculaValoresPrompt},
    "3": {"nome": "Mostra valores", "funcao": mostraValoresPrompt},
    "q": {"nome": "Sair", "funcao": 0},
}


def prompt():
    os.system("clear")
    print("\n------ AgileGraphs ------\n")
    print("Escolha uma opção:")

    for key,opcao in opcoes.items():
        print(f"[{key}] - {opcao["nome"]}")

    print()

    userInput = obtemInput("",opcoes)
    if userInput == "q": return
    else: opcoes[userInput]["funcao"]()

