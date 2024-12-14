from openpyxl import load_workbook
from dados_celulas import dados_relatorio

RELATORIOS_DIRECTORY = "./relatorios/"
relatorios = {}


def loadRelatorio(nomeRelatorio: str) -> None:
    global relatorios
    wb = load_workbook(RELATORIOS_DIRECTORY + nomeRelatorio + ".xlsx")
    relatorios[nomeRelatorio] = {
        "sheet1": wb["Excel_1"],
        "sheet2": wb["Excel_2"],
    }


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

    if type(valor) is tuple:
        sheet, celula = valor
        return relatorios[relatorio][sheet][celula].value
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

    if '' == chaves[-1]:  # acesso direto a uma celula
        try:
            sheet = "sheet" + chaves[0][0]
            celula = chaves[0][1:]
            return relatorios[relatorio][sheet][celula].value
        except Exception:
            if chaves[0][0] not in ('1', '2'):
                raise ValueError(f"A sheet 'sheet{chaves[0][0]}' não existe")
            raise ValueError(f"A célula {chaves[0][1:]} não existe")
    else:
        return obtemValorAux(chaves, relatorio)
