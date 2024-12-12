from obtem_valor import obtemValor
from dados_celulas import dados_relatorio

operadores = ["+", "-", "*", "/", "(", ")"]

aliases = {
    "dr": "demonstracaoResultados",
    "hr": "recursosHumanos",

    "emp1": "empresa1",
    "emp2": "empresa2",
    "emp3": "empresa3",
    "emp4": "empresa4",
    "emp5": "empresa5",
    "emp6": "empresa6",
    "emp7": "empresa7",
}


def ehVarivel(argumento: str) -> bool:
    return argumento not in operadores and not all(s.isnumeric() for s in argumento.split('.'))


def calculaExpressao(expressao: list[str], trimestre: str) -> int | float:
    expressao_substituida = ""
    for argumento in expressao:
        if ehVarivel(argumento):
            expressao_substituida += str(obtemValor(argumento, trimestre))
        else:
            expressao_substituida += argumento

    return eval(expressao_substituida)


def parseExpressao(expressao_raw: str) -> list[str]:
    expressao = [expressao_raw.replace(" ", "")]
    for operador in operadores:
        new_expressao = []
        for argumento in expressao:
            argumento_splited = argumento.split(operador)

            argumento_processado = []
            for j in argumento_splited:
                argumento_processado += [j, operador]
            argumento_processado = argumento_processado[:-1]

            new_expressao += argumento_processado

        expressao = new_expressao

    expressao = list(filter(lambda s: s != '', expressao))
    return expressao


def ehExpressaoValida(expressao_raw: str) -> bool:
    '''
    Verifica que uma string eh uma expressao valida
    '''
    expressao = parseExpressao(expressao_raw)
    expressao = traduzExpressao(expressao)

    try:
        if "ALL" in expressao_raw:
            expansao = expandeExpressao(expressao_raw)

            for expr_raw in expansao:
                expressao = parseExpressao(expr_raw)
                expressao = traduzExpressao(expressao)
                calculaExpressao(expressao,"Relatorio1")
        else:
            calculaExpressao(expressao, "Relatorio1")
    except Exception:
        return False
    else:
        return True


def traduzExpressao(expressao: list[str]) -> list[str]:  # aliases
    for i in range(len(expressao)):
        novo_argumento = ""
        for campo in expressao[i].split(':'):
            novo_argumento += aliases.get(campo, campo) + ':'

        novo_argumento = novo_argumento[:-1]
        expressao[i] = novo_argumento

    return expressao



def expandeExpressao(expressao_raw: str) -> list[str]:
    '''
    Expande uma expressao para uma lista de todas as possiveis expressoes
    a partir da keyword "ALL"

    por exemplo:
        quotasMercado:ALL:prod1

    expande para:
        quotasMercado:empresa1:prod1
        quotasMercado:empresa2:prod1
        quotasMercado:empresa3:prod1
        quotasMercado:empresa4:prod1
        etc..
    '''
    expansao = []
    componentesExpressao = processaExpressao(expressao_raw)
    
    if expressao_raw.count("ALL") != 1: return [expressao_raw]
    var = [x for x in componentesExpressao if "ALL" in x][0]

    componentesVar = var.split(':')
    i = componentesVar.index("ALL")

    tabela_valores = dados_relatorio

    for j in range(i):
        tabela_valores = tabela_valores[componentesVar[j]]
        
    for k in tabela_valores.keys():
        novaExpressao = expressao_raw.replace("ALL",k)
        expansao.append(novaExpressao)

    return expansao


def processaExpressao(expressao_raw: str):
    expressao = parseExpressao(expressao_raw)
    return traduzExpressao(expressao)


def calculaInfo(expressao_raw: str, trimestres: list[str]) -> list[int | float]:
    expressao = parseExpressao(expressao_raw)
    expressao = traduzExpressao(expressao)
    return [calculaExpressao(expressao, trimestre) for trimestre in trimestres]
