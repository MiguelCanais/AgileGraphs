from obtem_valor import obtemValor

operadores = ["+", "-", "*", "/", "(", ")"]

aliases = {
    "dr": "demonstracaoResultados",
    "hr": "recursosHumanos",
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


def calculaInfo(expressao_raw: str, trimestres: list[str]) -> list[int | float]:
    expressao = parseExpressao(expressao_raw)
    expressao = traduzExpressao(expressao)
    return [calculaExpressao(expressao, trimestre) for trimestre in trimestres]
