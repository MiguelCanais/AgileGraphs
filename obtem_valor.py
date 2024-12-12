from openpyxl import load_workbook
from dados_celulas import dados_relatorio

relatorios_dir = "./relatorios/"
relatorios = {}


def loadRelatorio(nomeRelatorio: str) -> None:
    global relatorios
    wb = load_workbook(relatorios_dir + nomeRelatorio + ".xlsx")
    relatorios[nomeRelatorio] = {
        "sheet1": wb["Excel_1"],
        "sheet2": wb["Excel_2"],
    }


def obtemValorEspecifico(chaves: list[str]) -> tuple[dict | tuple, int]:
    valor = dados_relatorio
    failure_index = 0
    for chave in chaves:
        if type(valor) is tuple:
            print("variavel errada:", chave)
            exit()

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



def obtemValor(tipo: str, relatorio: str) -> int | float:
    """
    Exemplos de tipo:
        "vendas" - Calcula o valor de todas as vendas
        "vendas:prod1" - Calcula o valor de todas as vendas do produto
        "vendas:ue" -
        "vendas:prod1:ue"
    """
    if relatorio not in relatorios:
        loadRelatorio(relatorio)

    chaves = tipo.split(':')
    return obtemValorAux(chaves, relatorio)
