from openpyxl import load_workbook
from dados_celulas import dados_relatorio

RELATORIOS_DIRECTORY = "./relatorios/"
relatorios = {}


def loadRelatorio(relatorio: str) -> None:
    global relatorios
    relatorios[relatorio] = load_workbook(RELATORIOS_DIRECTORY + relatorio + ".xlsx")


def obtemValorCelula(celula_raw: str, relatorio: str) -> int | float:
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


def obtemValorAux(chaves: list[str], relatorio: str) -> int | float:
    valor, failure_index = obtemValorEspecifico(chaves)

    if type(valor) is str:
        return obtemValorCelula(valor, relatorio)
    else:
        return sum(obtemValorAux(chaves[:failure_index] + [chave] + chaves[failure_index:], relatorio) for chave in valor)



def obtemValor(variavel: str, relatorio: str) -> int | float:
    """
    Exemplos de tipo:
        "vendas" - Calcula o valor de todas as vendas
        "vendas:prod1" - Calcula o valor de todas as vendas do produto
        "vendas:ue" -
        "vendas:prod1:ue"
    """
    if relatorio not in relatorios:
        loadRelatorio(relatorio)

    chaves = variavel.split(':')

    if chaves[-1] == '':  # acesso direto a uma celula
        return obtemValorCelula(chaves[0], relatorio)
    else:
        return obtemValorAux(chaves, relatorio)
