from openpyxl import load_workbook
from dados_celulas import obtemDadosRelatorio

relatorios = "./relatorios/"

loadedRelatorios = {}


def loadRelatorio(fileName: str):
    """
    Retorna as duas folhas de excel do relatorio
    """
    if fileName not in loadedRelatorios:
        wb = load_workbook(f"{relatorios}{fileName}.xlsx")
        sheet1 = wb["Excel_1"]
        sheet2 = wb["Excel_2"]

        dados = obtemDadosRelatorio(sheet1, sheet2)
        loadedRelatorios[fileName] = dados

        return dados
    else:
        return loadedRelatorios[fileName]


def calculaValor(tipo, dados):
    total = 0

    if tipo == "TOTAL":
        for k, val in dados.items():
            if isinstance(val, dict):
                total += calculaValor(k, dados)
            else:
                total += val
    elif tipo in dados:
        if isinstance(dados[tipo], dict):
            for vendasMercado in dados[tipo].values():
                total += vendasMercado
        else:
            total += dados[tipo]
    else:
        for produto in dados.values():
            total += produto[tipo]

    return total


def obtemValor(tipo: str, nomeRelatorio: str) -> int | float:
    """
    Exemplos de tipo:
        "vendas" - Calcula o valor de todas as vendas
        "vendas:prod1" - Calcula o valor de todas as vendas do produto
        "vendas:ue" -
        "vendas:prod1:ue"
    """
    dados = loadRelatorio(nomeRelatorio)

    filtros = tipo.split(":")

    valoresCategoria = dados[filtros[0]]

    if len(filtros) == 1:
        return calculaValor("TOTAL", valoresCategoria)
    elif len(filtros) == 2:
        s1 = filtros[1]
        return calculaValor(s1, valoresCategoria)
    else:
        s1 = filtros[1]
        s2 = filtros[2]
        return valoresCategoria[s1][s2]
