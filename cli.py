from utils import *
from graficos import criaGraficos

def obtemInput(promptText,inputValido: list[str]=[]) -> str:
    '''
    Obtem input do utilizador e verifica que o input é
    uma opcao valida
    '''
    userInput = input(promptText)

    if len(inputValido) == 0: return userInput
    if not userInput in inputValido: return obtemInput()

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


def criaGraficoPrompt():
    print()
    listaTrimestres = obtemTrimestres()

    print("Insira expressoes para graficos (q para parar):")

    expressoes = []

    while True:
        userInput = obtemInput("",[])
        if userInput == 'q': break
        expressoes.append(userInput) 

    criaGraficos(expressoes,listaTrimestres)
    

def calculaValorPrompt():
    print("valor here")

opcoes = {
    "q": 0,
    "1": criaGraficoPrompt,
    "2": calculaValorPrompt,
}


def prompt():
    print("\n------ AgileGraphs ------\n")
    print("Escolha uma opção:\n [1] - Cria gráfico\n [2] - Calcula valor\n [q] - Sair")

    userInput = obtemInput("",opcoes)
    if userInput == "q": return
    else: opcoes[userInput]()

