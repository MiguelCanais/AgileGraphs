from utils import obtemValor

operadores = ["+", "-", "*", "/", "(", ")"]

aliases = {
    "dr": "demonstracaoResultados",
}


def calculaExpressao(expressao: list[str], trimestre: str) -> int | float:
    expressao_substituida = ""
    for i in range(len(expressao)):
        argumento = expressao[i]
        if argumento not in operadores and not argumento.isnumeric():
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
                if j == '':
                    continue
                argumento_processado += [j, operador]
            argumento_processado = argumento_processado[:-1]

            new_expressao += argumento_processado

        expressao = new_expressao

    return expressao


def traduzExpressao(expressao: list[str]):  # aliases
    for i in range(len(expressao)):
        novo_argumento = ""
        for campo in expressao[i].split(':'):
            novo_argumento += aliases.get(campo, campo) + ':'

        novo_argumento = novo_argumento[:-1]
        expressao[i] = novo_argumento


def calculaInfo(expressao_raw: str, trimestres: list[str]) -> list[int | float]:
    expressao = parseExpressao(expressao_raw)
    traduzExpressao(expressao)
    return [calculaExpressao(expressao, trimestre) for trimestre in trimestres]
