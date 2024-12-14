from numpy import nan
from obtem_valor import obtemValor, obtemValorEspecifico, numero_relatorios

OPERADORES = ["+", "-", "*", "/", "(", ")"]

ALIASES = {
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


def ehVariavel(termo: str) -> bool:
    return termo not in OPERADORES and not all(s.isnumeric() for s in termo.split('.'))


def ehExpressaoValida(expressao_raw: str) -> bool:
    '''
    Verifica que uma string eh uma expressao valida
    '''
    try:
        calculaInfo([expressao_raw])
    except Exception:
        return False
    else:
        return True


def calculaRelatoriosValidos(expressao: list[str]) -> list[int]:
    max_frente, max_tras = 0, 0

    variaveis = filter(ehVariavel, expressao)
    for variavel in variaveis:
        if not variavel.startswith(':'):
            continue

        chaves = variavel.split(':')
        offset = chaves[1]

        if offset.startswith('~'):
            max_tras = max(max_tras, int(offset[1:]))
        else:
            max_frente = max(max_frente, int(offset))

    return list(range(max_tras, numero_relatorios - max_frente))


def calculaExpressao(expressao: list[str], relatorio: int) -> int | float:
    expressao_substituida = ""
    for termo in expressao:
        if ehVariavel(termo):
            expressao_substituida += str(obtemValor(termo, relatorio))
        else:
            expressao_substituida += termo

    return eval(expressao_substituida)


def parseExpressao(expressao_raw: str) -> list[str]:
    expressao = [expressao_raw.replace(" ", "")]
    for operador in OPERADORES:
        new_expressao = []
        for termo in expressao:
            termo_splited = termo.split(operador)

            termo_processado = []
            for j in termo_splited:
                termo_processado += [j, operador]
            termo_processado = termo_processado[:-1]

            new_expressao += termo_processado

        expressao = new_expressao

    expressao = list(filter(lambda s: s != '', expressao))
    return expressao


def traduzExpressao(expressao: list[str]) -> list[str]:  # aliases
    for i in range(len(expressao)):
        novo_termo = ""
        for campo in expressao[i].split(':'):
            novo_termo += ALIASES.get(campo, campo) + ':'

        novo_termo = novo_termo[:-1]
        expressao[i] = novo_termo

    return expressao


def expandeVariavel(variavel: str) -> list[str]:
    chaves = variavel.split(':')
    all_index = chaves.index("ALL")
    valor, failure_index = obtemValorEspecifico(chaves)


    chaves_expandidas = []
    if all_index == failure_index:
        for chave in valor:
            chaves_expandidas.append(chaves[:all_index] + [chave] + chaves[all_index+1:])

    else:
        nova_chaves = chaves[:failure_index] + [list(valor.keys())[0]] + chaves[failure_index:]
        nova_variavel = ':'.join(nova_chaves)

        for variavel in expandeVariavel(nova_variavel):
            chaves_temp = variavel.split(':')
            del chaves_temp[failure_index]
            chaves_expandidas.append(chaves_temp)

    variaveis_expandidas = list(map(':'.join, chaves_expandidas))
    return variaveis_expandidas


def expandeExpressao(expressao: list[str]) -> list[list[str]]:
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
    if all("ALL" not in termo for termo in expressao):
        return [expressao]

    for i in range(len(expressao)):
        termo = expressao[i]
        chaves = termo.split(':')
        if ehVariavel(termo) and "ALL" in chaves:
            expressoes_expandidas = []
            for variavel in expandeVariavel(termo):
                nova_expressao = expressao[:i] + [variavel] + expressao[i+1:]
                expressoes_expandidas += expandeExpressao(nova_expressao)

            return expressoes_expandidas


def calculaInfoExpressao(expressao: list[str]) -> list[int | float]:
    relatorios = calculaRelatoriosValidos(expressao)
    if len(relatorios) == 0:
        raise ValueError("Não existem relatórios suficientes para satisfazer a expressão")

    info = [nan] * numero_relatorios
    for relatorio in relatorios:
        info[relatorio] = calculaExpressao(expressao, relatorio)

    return info


def calculaInfo(expressoes_raw: list[str]) -> list[tuple[str, list[int | float]]]:  # what a pretty return type ;)
    expressoes = list(map(parseExpressao, expressoes_raw))
    expressoes = list(map(traduzExpressao, expressoes))

    expressoes_expandidas = []
    for expressao in expressoes:
        expressoes_expandidas += expandeExpressao(expressao)

    return [(''.join(expressao), calculaInfoExpressao(expressao)) for expressao in expressoes_expandidas]
