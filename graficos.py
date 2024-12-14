from calcula_info import calculaInfo
import matplotlib.pyplot as plt

LINE_COLORS = ["blue", "red", "green", "orange", "purple", "cyan", "black"]


def configuraGrafico(maximo, minimo) -> None:
    # if minimo < 0:
    #     amplitude = maximo - minimo
    #     lowerlimit = minimo - amplitude * 0.2
    # else:
    #     amplitude = maximo
    #     lowerlimit = 0

    amplitude = maximo - minimo

    upperlimit = maximo + amplitude * 0.2
    lowerlimit = minimo - amplitude * 0.4
    # offset = 0
    # for i in range(len(trimestres)):
    #     plt.text(trimestres[i],info[i]-offset, f"{info[i]}", fontsize=10,color="black",
    #              bbox=dict(facecolor="white", alpha=0.5, edgecolor="black"))

    plt.xlabel("Trimestres")
    plt.legend(loc="lower left", fontsize=10)
    plt.ylim(bottom=lowerlimit, top=upperlimit)
    plt.axhline(y=0, color="red", linewidth=1, linestyle="--", label="y=0 line")
    plt.grid()


def criaGraficos(expressoes_raw: list[str], title: str = "Grafico") -> None:
    plt.close()

    maximo = -(10**100)
    minimo = 10**100

    info_graphs, relatorios = calculaInfo(expressoes_raw)
    relatorios = list(map(lambda n: f"Relatorio{n+1}", relatorios))
    for i in range(len(info_graphs)):
        expressao, info = info_graphs[i]

        maximo = max(max(info), maximo)
        minimo = min(min(info), minimo)

        plt.plot(
            relatorios,
            info,
            label=expressao,
            marker="o",
            color=LINE_COLORS[i % (len(LINE_COLORS))],
        )

    configuraGrafico(maximo, minimo)
    plt.title(title)

    plt.savefig(title + ".png")
    plt.show()
