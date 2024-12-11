from utils import obtemValores


operadores = ["+", "-", "*", "/", "(", ")"]


def calculaInfoTrimestre(expressao: list[str], trimestre: str) -> int | float:
    expressao_substituida = ""
    for i in range(len(expressao)):
        argumento = expressao[i]
        if argumento not in operadores and not argumento.isnumeric():
            expressao_substituida += str(obtemValores(argumento, trimestre))
        else:
            expressao_substituida += argumento

    return eval(expressao_substituida)


def calculaInfo(expressao_raw: str, trimestres: list[str]) -> list[int | float]:
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

    return [calculaInfoTrimestre(expressao, trimestre) for trimestre in trimestres]
