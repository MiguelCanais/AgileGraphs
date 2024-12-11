from calcula_info import calculaInfo
import matplotlib.pyplot as plt



def criaGraficos(expressao: str, trimestres: list[str]) -> None:
    info = calculaInfo(expressao, trimestres)

    plt.plot(trimestres, info, marker='o')
    plt.title(expressao)
    plt.xlabel("trimestres")
    plt.grid()

    plt.show()
