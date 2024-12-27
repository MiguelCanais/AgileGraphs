import matplotlib.pyplot as plt
from numpy import nanmax, nanmin

from calcula_info import calculaInfo
from obtem_valor import NOME_RELATORIOS

LINE_COLORS = ["blue", "red", "green", "orange", "purple", "cyan", "black"]


def configuraGrafico(maximo: int, minimo: int) -> None:
    amplitude = maximo - minimo

    upperlimit = maximo + amplitude * 0.2
    lowerlimit = minimo - amplitude * 0.3

    plt.xlabel("Relatorios")
    plt.legend(loc="lower left", fontsize=10)
    plt.ylim(bottom=lowerlimit, top=upperlimit)
    plt.axhline(y=0, color="red", linewidth=1, linestyle="--", label="y=0 line")
    plt.grid()


def criaGraficos(expressoes_raw: list[str]) -> None:
    plt.close()

    maximo = -(10**100)
    minimo = 10**100

    info_graphs = calculaInfo(expressoes_raw)
    for i in range(len(info_graphs)):
        expressao, info = info_graphs[i]

        maximo = max(nanmax(info), maximo)
        minimo = min(nanmin(info), minimo)

        plt.plot(
            NOME_RELATORIOS,
            info,
            label=expressao,
            marker="o",
            color=LINE_COLORS[i % (len(LINE_COLORS))],
        )

    configuraGrafico(maximo, minimo)

    plt.savefig("Grafico.png")
    plt.show()
