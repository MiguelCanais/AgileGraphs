from numpy import nan

from obtem_valor import obtemValor, obtemDados, NUMERO_RELATORIOS

OPERADORES = ["+", "-", "*", "/", "(", ")"]

ALIASES = {
    "dr": "demonstracaoResultados",
    "da": "despesasAdminstrativas",
    "rh": "recursosHumanos",
    "qm": "quotasMercado",

    "emp1": "empresa1",
    "emp2": "empresa2",
    "emp3": "empresa3",
    "emp4": "empresa4",
    "emp5": "empresa5",
    "emp6": "empresa6",
    "emp7": "empresa7",

    "prod1": "produto1",
    "prod2": "produto2",
    "prod3": "produto3",
}


def ehVariavel(termo: str) -> bool:
    """ Determina se um termo é uma variavel."""
    return termo not in OPERADORES and not all(s.isnumeric() for s in termo.split('.'))


def ehExpressaoValida(expressao_raw: str) -> bool:
    '''
    Verifica que uma string eh uma expressao valida,
    ou seja, se não vai dar erro quando se tentar calcular o seus valores.
    '''
    try:
        calculaInfo([expressao_raw])
    except Exception as e:
        print("Expressao inválida -", str(e))
        return False
    else:
        return True


def calculaRelatoriosValidos(expressao: list[str]) -> list[int]:
    """
    Dado uma expressao determina quais os relatorios para o qual se pode calcular a expressao.
    Isto por causa do prefixo de relatorio, se tivermos 8 relatorios e tentarmos calcular:
        :~5:vendas - vendas
    Só vai ser valida para os relatórios 5, 6 e 7.
    """
    max_frente, max_tras = 0, 0

    variaveis = filter(ehVariavel, expressao)
    for variavel in variaveis:
        if not variavel.startswith(':'):
            continue

        chaves = variavel.split(':')
        offset = chaves[1]

        if offset.startswith('~'):
            max_tras = max(max_tras, int(offset[1:]))
        elif offset.startswith('#'):
            if not (1 <= int(offset[1:]) <= NUMERO_RELATORIOS):
                raise ValueError(f"O relatório {int(offset[1:])} não existe.")
        else:
            max_frente = max(max_frente, int(offset))

    return list(range(max_tras, NUMERO_RELATORIOS - max_frente))


def calculaExpressao(expressao: list[str], relatorio: int) -> int | float:
    """ Calcula o valor de uma expressao considerando um dado relatorio."""
    expressao_substituida = ""
    for termo in expressao:
        if ehVariavel(termo):
            expressao_substituida += str(obtemValor(termo, relatorio))
        else:
            expressao_substituida += termo

    return eval(expressao_substituida)


def calculaInfoExpressao(expressao: list[str]) -> list[int | float]:
    """
    Calcula os valor de uma expressao para todos os relatorios validos.
    Devolve sempre uma lista de tamanho `NUMERO_RELATORIOS`, que pussui o valor nan
    para os relatorios invalidos.
    """
    relatorios = calculaRelatoriosValidos(expressao)

    if len(relatorios) == 0:
        raise ValueError("Não existem relatórios suficientes para satisfazer a expressão.")

    info = [nan] * NUMERO_RELATORIOS
    for relatorio in relatorios:
        info[relatorio] = calculaExpressao(expressao, relatorio)

    return info


def parseExpressao(expressao_raw: str) -> list[str]:
    """ Separa uma expressao_raw nos seus termo para facilitar o seu processamento."""
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
    """ Realiza a substituição de todos os aliases."""
    for i in range(len(expressao)):
        novo_termo = ""
        for campo in expressao[i].split(':'):
            novo_termo += ALIASES.get(campo, campo) + ':'

        novo_termo = novo_termo[:-1]
        expressao[i] = novo_termo

    return expressao


def expandeALL(chaves: list[str]) -> list[str]:
    """
    Devolve todas as possiveis expanssões do primeiro ALL (se houver mais, os outros ficam inalterados).
    Qualquer ALLn foi trocado por um simples ALL.
    As chaves não incluiem o prefixo de relatório
    """
    all_index = chaves.index("ALL")
    valor, failure_index = obtemDados(chaves)

    if all_index == failure_index:
        return list(valor.keys())
    else:
        nova_chaves = chaves[:failure_index] + [list(valor.keys())[0]] + chaves[failure_index:]
        return expandeALL(nova_chaves)


def substituiALLn(expressao_original: list[str], ALLn: str, substituicao: str) -> list[str]:
    """ Utilizada para trocar todas as ocorrencias de um ALLn especifico numa expressao pelo valor de `substituicao`."""
    expressao = expressao_original.copy()
    for i in range(len(expressao)):
        termo = expressao[i]
        if not ehVariavel(termo):
            continue

        chaves = termo.split(':')
        for j in range(len(chaves)):
            if chaves[j] == ALLn:
                chaves[j] = substituicao

        expressao[i] = ':'.join(chaves)

    return expressao


def expandeExpressao(expressao: list[str]) -> list[list[str]]:
    '''
    Devolve uma lista de todas as possíveis expanssões de uma expressao.
    Expande todos os `ALL` e `ALLn`.
    Consulta a secção da documentação sobre este tipo de expanção para mais detalhes.
    '''
    # já não existem mais ALL ou ALLn na expressão
    if all("ALL" not in termo for termo in expressao):
        return [expressao]

    for i in range(len(expressao)):
        termo = expressao[i]
        chaves = termo.split(':')

        if not ehVariavel(termo) or not any(chave.startswith('ALL') for chave in chaves):
            continue

        # remove os prefixos de relatorio
        if termo.startswith(':'):
            chaves2 = chaves[2:]
        else:
            chaves2 = chaves

        for j in range(len(chaves2)):
            if not chaves2[j].startswith('ALL'):
                continue

            # importante distingir ALL de ALLn
            simple_ALL = chaves2[j] == 'ALL'
            chave_all = chaves[j]
            chaves2[j] = 'ALL'
            break

        substituicoes = expandeALL(chaves2)

        # a lógica principal só expande o primeiro ALL, logo chamase a si mesma até ter expandido todos os ALLs
        expressoes_expandidas = []
        if simple_ALL:
            # é um ALL
            all_index = chaves.index('ALL')
            for substituicao in substituicoes:
                nova_variavel = ':'.join(chaves[:all_index] + [substituicao] + chaves[all_index + 1:])
                nova_expressao = expressao[:i] + [nova_variavel] + expressao[i+1:]
                expressoes_expandidas += expandeExpressao(nova_expressao)
        else:
            # é um ALLn
            for substituicao in substituicoes:
                nova_expressao = substituiALLn(expressao, chave_all, substituicao)
                expressoes_expandidas += expandeExpressao(nova_expressao)

        return expressoes_expandidas


def processaExpressao(expressao_raw: str) -> list[list[str]]:
    """
    Faz todo o processamento de uma expressao_raw.
    Fundamental para calcular o valores das expressoes e gerar o autocomplete.
    Possui três passos, cada um realizado por uma função separada:
        - parsing : separar em termos
        - tradução : substituir todos os aliases
        - expandir : expandir todos os ALL e ALLn

    Devolve uma lista de expressões.
    """
    expressao = parseExpressao(expressao_raw)
    expressao = traduzExpressao(expressao)
    return expandeExpressao(expressao)


def calculaInfo(expressoes_raw: list[str]) -> list[tuple[str, list[int | float]]]:  # what a pretty return type ;)
    """
    Recebe uma lista de expressoes_raw do utilizador e devolve uma lista de tuplos em que:
        - 1º elemento é o nome de uma expressao já processada, como `2 * vendas:produto1:intenet`
        - 2º elemento é uma lista com o valor da expressao para cada relatorio.
    """
    expressoes = []
    for expressao_raw in expressoes_raw:
        expressoes += processaExpressao(expressao_raw)

    return [(''.join(expressao), calculaInfoExpressao(expressao)) for expressao in expressoes]
