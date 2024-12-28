import re
import xlrd
import os

from dados_celulas import dados_celulas

RELATORIOS_DIRECTORY = "relatorios/"


def obtemCoordenadas(celula: str):
    """ Determina as coordenadas de uma celula."""
    pattern = r"(\d)([A-Z]+)(\d+)"
    match = re.match(pattern, celula)

    if match:
        sheetNumero = int(match.group(1)) - 1
        letras = match.group(2)
        numeros = match.group(3)

        coluna = 0
        linha = int(numeros) - 1

        for letra in letras:
            coluna = coluna * 26 + ord(letra) - ord("A") + 1

        coluna -= 1

        return sheetNumero, linha, coluna


def obtemTrimestre(relatorio_workbook) -> int:
    """
    Recebe um workbook correspondente a um relatório e devolve o valor do seu trimestres.
    O trimestre neste caso corresponde á ordem cronológica do relatório,
    o primeiro tem trimestre 1, o 5º tem trimestre 5 ...
    """
    coordenadasAno = obtemCoordenadas("1T3")
    coordenadasTrimestre = obtemCoordenadas("1W3")
    sheet = relatorio_workbook.sheet_by_index(0)

    ano = int(sheet.cell_value(coordenadasAno[1], coordenadasAno[2]))
    trimestre = int(sheet.cell_value(coordenadasTrimestre[1], coordenadasTrimestre[2]))

    return (ano - 2010) * 4 + trimestre


def loadRelatorios() -> None:
    """
    Carrega todos os ficheiros `.Xls` presentes em `RELATORIOS_DIRECTORY` para a lista `RELATORIOS`.
    Os relatorios ficam ordnados de acordo com o seu trimestre.
    """
    files = os.listdir(RELATORIOS_DIRECTORY)
    xls_files = filter(lambda file: file.endswith(".Xls"), files)

    relatorios_loaded = []

    for file in xls_files:
        worbook = xlrd.open_workbook(RELATORIOS_DIRECTORY + file)
        relatorios_loaded.append(worbook)

    return sorted(relatorios_loaded, key=obtemTrimestre)


def obtemValorCelula(celula: str, relatorio: int) -> int | float:
    """ Obtem o valor númerico de uma dada celula. """
    coordenadas = obtemCoordenadas(celula)

    try:
        sheet = RELATORIOS[relatorio].sheet_by_index(coordenadas[0])
        valor = sheet.cell_value(coordenadas[1], coordenadas[2])
        return valor
    except Exception:
        raise ValueError(f"A célula {celula} não existe.")


def obtemDados(chaves: list[str]) -> tuple[dict | tuple, int]:
    """
    Dadas as chaves de uma variavel vai utilizar as chaves para avaçar pelos elementos
    de `dados_celulas` até não dar mais.
    `failure_index` indica em que chave a pesquisa falhou.
    """
    dados = dados_celulas
    failure_index = 0

    for chave in chaves:
        if type(dados) is tuple:
            raise ValueError(f"variavel errada: {chave}.")

        if chave in dados:
            dados = dados[chave]
            failure_index += 1
        else:
            break

    return dados, failure_index


def obtemValorAux(chaves: list[str], relatorio: int) -> int | float:
    """
    Calcula o valor de uma variavel dadas as suas chaves relativamente a um dado relatorio.
    Já não contêm prefixo de relatorio, então `relatorio` é mesmo o relatorio para o qual o valor vai ser calculado.
    Funciona de forma recursiva de forma a lidar com chaves omitidas (faz a soma de todas as possibilidades).
    """
    dados, failure_index = obtemDados(chaves)

    if type(dados) is str:
        if failure_index == len(chaves):
            return obtemValorCelula(dados, relatorio)
        else:
            parte_mal_escrita = ":".join(chaves[failure_index:])
            raise ValueError(f"'{parte_mal_escrita}' está mal escrito.")
    else:
        return sum(obtemValorAux(chaves[:failure_index] + [chave] + chaves[failure_index:], relatorio) for chave in dados)


def obtemValor(variavel: str, relatorio: int) -> int | float:
    """
    Recebe uma variavel e calcula o seu valor dado um relatório.
    Não tem de necessariamente calcular o valor relativo ao relatório do argumento `relatorio`.
    É recomendado ver a secção da documentação sobre a syntax de variaveis.
    A variavel não deve conter aliases, ALL e ALLn.
    """
    if variavel.startswith(":"):  # prefixo de relatorio
        chaves = variavel.split(":")
        nova_variavel = ":".join(chaves[2:])

        offset = chaves[1]
        if offset.startswith("~"):
            novo_relatorio = relatorio - int(offset[1:])
        elif offset.startswith("#"):
            novo_relatorio = int(offset[1:]) - 1
        else:
            novo_relatorio = relatorio + int(offset)

        return obtemValor(nova_variavel, novo_relatorio)

    if variavel.endswith(":"):  # acesso direto a uma celula
        return obtemValorCelula(variavel[:-1], relatorio)

    # variavel normal
    chaves = variavel.split(":")
    return obtemValorAux(chaves, relatorio)


RELATORIOS = loadRelatorios()
NOME_RELATORIOS = [f"R{obtemTrimestre(x)}" for x in RELATORIOS]
NUMERO_RELATORIOS = len(RELATORIOS)
