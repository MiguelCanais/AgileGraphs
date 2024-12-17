import os

RELATORIOS_DIRECTORY = "./relatorios/"

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

def maiorPrefixoComum(l):
    """
    Dado uma lista de strings encontra o maior prefixo comum a todas
    as strings

    Por exemplo:
    l = ["produto1", "produto2", "produto3"]
    O maior prefixo comum é "produto"
    """
    if len(l) == 0: return ""

    i = 0
    while True:
        letra = 0
        for s in l:
            if len(s) == i:
                return s

            if letra == 0:
                letra = s[i]
            elif s[i] != letra:
                return s[:i]

        i += 1

def obtemRelatorios() -> list[str]:
    """
    Obtem uma lista com os nomes de todos os relatorios de cada
    trimestre de forma ordenada
    """
    listaTrimestres = [
        file.removesuffix(".xlsx")
        for file in os.listdir(RELATORIOS_DIRECTORY)
        if file.endswith(".xlsx")
    ]

    return sorted(listaTrimestres)


def obtemUltimosRelatorios(n: int = 1) -> list[str]:
    """
    Obtem uma lista com  os nomes dos ultimos N relatorios de cada
    trimestre
    """
    return obtemRelatorios()[-n:]


RELATORIOS = obtemRelatorios()
NUMERO_RELATORIOS = len(RELATORIOS)
