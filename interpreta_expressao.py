from utils import obtemValor


operadores = ["+", "-", "*", "/", "(", ")"]


def calculaExpressao(expressao: list[str], trimestre: str) -> int | float:
    expressao_substituida = ""
    for i in range(len(expressao)):
        argumento = expressao[i]
        if argumento not in operadores and not argumento.isnumeric():
            expressao_substituida += str(obtemValor(argumento, trimestre))
        else:
            expressao_substituida += argumento

    return eval(expressao_substituida)


def interpretaExpressao(expressao_raw: str, trimestres: list[str]) -> list[int | float]:
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

    return [calculaExpressao(expressao, trimestre) for trimestre in trimestres]
