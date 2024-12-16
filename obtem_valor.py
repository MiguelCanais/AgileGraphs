from os import listdir
from openpyxl import load_workbook
from dados_celulas import dados_relatorio

RELATORIOS_DIRECTORY = "./relatorios/"
relatorios = [load_workbook(RELATORIOS_DIRECTORY + relatorio) for relatorio in sorted(listdir(RELATORIOS_DIRECTORY))]
numero_relatorios = len(relatorios)


def obtemValorCelula(celula_raw: str, relatorio: int) -> int | float:
    sheet = "Excel_" + celula_raw[0]
    celula = celula_raw[1:]

    if sheet not in ("Excel_1", "Excel_2"):
        raise ValueError(f"A folha '{sheet}' não existe")

    try:
        return relatorios[relatorio][sheet][celula].value
    except Exception:
        raise ValueError(f"A célula {celula} não existe")


def obtemValorEspecifico(chaves: list[str]) -> tuple[dict | tuple, int]:
    valor = dados_relatorio
    failure_index = 0
    for chave in chaves:
        if type(valor) is tuple:
            raise ValueError("variavel errada:", chave)

        if chave in valor:
            valor = valor[chave]
            failure_index += 1
        else:
            break

    return valor, failure_index


def obtemValorAux(chaves: list[str], relatorio: int) -> int | float:
    valor, failure_index = obtemValorEspecifico(chaves)

    if type(valor) is str:
        return obtemValorCelula(valor, relatorio)
    else:
        return sum(obtemValorAux(chaves[:failure_index] + [chave] + chaves[failure_index:], relatorio) for chave in valor)


def obtemValor(variavel: str, relatorio: int) -> int | float:
    """
    Exemplos de tipo:
        "vendas" - Calcula o valor de todas as vendas
        "vendas:prod1" - Calcula o valor de todas as vendas do produto
        "vendas:ue" -
        "vendas:prod1:ue"
    """
    if variavel.startswith(':'):  # acesso a outro relatorio
        chaves = variavel.split(':')
        nova_variavel = ':'.join(chaves[2:])

        offset = chaves[1]
        if offset.startswith('~'):
            novo_relatorio = relatorio - int(offset[1:])
        else:
            novo_relatorio = relatorio + int(offset)

        return obtemValor(nova_variavel, novo_relatorio)

    if variavel.endswith(':'):  # acesso direto a uma celula
        return obtemValorCelula(variavel[:-1], relatorio)

    # variavel normal
    chaves = variavel.split(':')
    return obtemValorAux(chaves, relatorio)
