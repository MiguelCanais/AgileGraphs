from openpyxl import load_workbook
from dados_celulas import obtemDadosRelatorio 

def calculaValor(tipo,dados):
    total = 0

    # Calcula Total
    if tipo == "total":
        for k,val in dados.items():
            if isinstance(val,dict):
                total += calculaValor(k,dados)
            else:
                total += val
    # Calcula Produto
    elif tipo in dados:
        if isinstance(dados[tipo],dict):
            for vendasMercado in dados[tipo].values():
                total += vendasMercado
        else:
            total += dados[tipo]
    
    # Calcula Mercado
    else:
        for produto in dados.values():
            total += produto[tipo]

    return total

def loadSheet(fileName):
    wb = load_workbook(f"./relatorios/{fileName}.xlsx")
    sheet = wb["Excel_1"]
    return sheet


def obtemValor(tipo: str, nomeRelatorio: str) -> int|float:
    '''
    Exemplos de tipo:
        "vendas" - Calcula o valor de todas as vendas
        "vendas:prod1" - Calcula o valor de todas as vendas do produto
        "vendas:ue" - 
        "vendas:prod1:ue"
    '''
    sheet = loadSheet(nomeRelatorio)
    dados = obtemDadosRelatorio(sheet)

    l = tipo.split(':')
    s = l[0]

    valores = dados[s]

    if len(l) == 1:
        return calculaValor("total",valores)
    elif len(l) == 2:
        s1 = l[1]
        return calculaValor(s1,valores)
    else:
        s1 = l[1]
        s2 = l[2]
        return valores[s1][s2]
    



    

