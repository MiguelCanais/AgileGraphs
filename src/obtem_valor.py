import re
import xlrd
import os

from dados_celulas import dados_relatorio

RELATORIOS_DIRECTORY = "relatorios/"

def loadRelatorios():
    files = os.listdir(RELATORIOS_DIRECTORY)
    xls_files = [file for file in files if file.endswith(".Xls")]

    relatorios_loaded = []

    for file in xls_files:
        worbook = xlrd.open_workbook(RELATORIOS_DIRECTORY+file)
        relatorios_loaded.append(worbook)

    return sorted(relatorios_loaded, key=lambda x: obtemTrimestre(x))


def obtemCoordenada(celula_raw):
    pattern = r"(\d)([A-Z]+)(\d+)"
    match = re.match(pattern,celula_raw)

    if match:
        sheetNumero = int(match.group(1))-1
        letras = match.group(2)
        numeros = match.group(3)

        coluna = 0 
        linha = int(numeros)-1

        for letra in letras:
            coluna = coluna*26 + ord(letra) - ord('A') + 1

        coluna -= 1

        return sheetNumero,linha,coluna


def obtemValorCelula(celula_raw: str, relatorio: int) -> int|float:
    coordenada = obtemCoordenada(celula_raw)
    
    try:
        sheet = RELATORIOS[relatorio].sheet_by_index(coordenada[0])
        val = sheet.cell_value(coordenada[1],coordenada[2])
        return val
    except Exception:
        raise ValueError(f"A célula {celula_raw} não existe.")



def obtemTrimestre(relatorio):
    coordenadaAno = obtemCoordenada("1T3")
    coordenadaTrimestre = obtemCoordenada("1W3") 
    sheet = relatorio.sheet_by_index(0)

    ano = int(sheet.cell_value(coordenadaAno[1],coordenadaAno[2]))
    trimestre = int(sheet.cell_value(coordenadaTrimestre[1],coordenadaTrimestre[2]))

    v = (ano - 2010)*4 + trimestre

    return v


def obtemValorEspecifico(chaves: list[str]) -> tuple[dict | tuple, int]:
    valor = dados_relatorio
    failure_index = 0
    for chave in chaves:
        if type(valor) is tuple:
            raise ValueError(f"variavel errada: {chave}.")

        if chave in valor:
            valor = valor[chave]
            failure_index += 1
        else:
            break

    return valor, failure_index


def obtemValorAux(chaves: list[str], relatorio: int) -> int | float:
    valor, failure_index = obtemValorEspecifico(chaves)

    if type(valor) is str:
        if failure_index == len(chaves):
            return obtemValorCelula(valor, relatorio)
        else:
            parte_mal_escrita = ':'.join(chaves[failure_index:])
            raise ValueError(f"'{parte_mal_escrita}' está mal escrito.")
    else:
        return sum(obtemValorAux(chaves[:failure_index] + [chave] + chaves[failure_index:], relatorio) for chave in valor)


def obtemValor(variavel: str, relatorio: int) -> int | float:
    if variavel.startswith(':'):  # acesso a outro relatorio
        chaves = variavel.split(':')
        nova_variavel = ':'.join(chaves[2:])

        offset = chaves[1]
        if offset.startswith('~'):
            novo_relatorio = relatorio - int(offset[1:])
        elif offset.startswith('#'):
            novo_relatorio = int(offset[1:]) - 1
        else:
            novo_relatorio = relatorio + int(offset)

        return obtemValor(nova_variavel, novo_relatorio)

    if variavel.endswith(':'):  # acesso direto a uma celula
        return obtemValorCelula(variavel[:-1], relatorio)

    # variavel normal
    chaves = variavel.split(':')
    return obtemValorAux(chaves, relatorio)


RELATORIOS = loadRelatorios()
NOME_RELATORIOS = [f"R{obtemTrimestre(x)}" for x in RELATORIOS]
NUMERO_RELATORIOS = len(RELATORIOS)
