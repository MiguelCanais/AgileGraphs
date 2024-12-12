import os

relatorios = "./relatorios/"


def obtemTrimestres() -> list[str]:
    """
    Obtem uma lista com os nomes de todos os relatorios de cada
    trimestre de forma ordenada
    """
    listaTrimestres = [
        file.removesuffix(".xlsx")
        for file in os.listdir(relatorios)
        if file.endswith(".xlsx")
    ]

    return sorted(listaTrimestres)


def obtemUltimosTrimestres(n: int = 1) -> list[str]:
    """
    Obtem uma lista com  os nomes dos ultimos N relatorios de cada
    trimestre
    """
    return obtemTrimestres()[-n:]
