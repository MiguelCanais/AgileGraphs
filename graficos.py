from interpreta_expressao import calculaInfo
import matplotlib.pyplot as plt

lineColors = ["blue", "green", "red", "orange"]


def configuraGrafico(maximo, minimo):
    if minimo < 0:
        amplitude = maximo - minimo
        lowerlimit = minimo - amplitude * 0.2
    else:
        amplitude = maximo
        lowerlimit = 0

    upperlimit = maximo + amplitude * 0.2

    # offset = 0
    # for i in range(len(trimestres)):
    #     plt.text(trimestres[i],info[i]-offset, f"{info[i]}", fontsize=10,color="black",
    #              bbox=dict(facecolor="white", alpha=0.5, edgecolor="black"))

    plt.xlabel("Trimestres")
    plt.legend(loc="lower left", fontsize=10)
    plt.ylim(bottom=lowerlimit, top=upperlimit)
    plt.axhline(y=0, color="red", linewidth=1, linestyle="--", label="y=0 line")
    plt.grid()


def criaGraficos(expressoes: list[str] | str, trimestres: list[str], title: str = "Grafico"):
    if type(expressoes) is str:
        expressoes = [expressoes]

    maximo = -(10**100)
    minimo = 10**100

    for i, expressao in enumerate(expressoes):
        info = calculaInfo(expressao, trimestres)
        maximo = max(max(info), maximo)
        minimo = min(min(info), minimo)
        plt.plot(
            trimestres,
            info,
            label=expressao,
            marker="o",
            color=lineColors[i % (len(lineColors)-1)],
        )

    configuraGrafico(maximo, minimo)

    plt.title(title)
    plt.savefig(title + ".png")
    plt.show()
