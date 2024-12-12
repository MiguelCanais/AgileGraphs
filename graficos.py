from interpreta_expressao import interpretaExpressao
import matplotlib.pyplot as plt

lineColors = ["blue","green","red","orange"]

def criaGrafico(expressao: str, trimestres: list[str], title: str="Grafico"):
    info = interpretaExpressao(expressao, trimestres)

    amplitude = max(info) - min(info)

    upperlimit = max(info) * 1.3
    lowerlimit = min(info) * 1.3 if min(info) < 0 else 0

    offset = 0#upperlimit-lowerlimit * 0.01

    plt.plot(trimestres, info, label=expressao, marker='o')
    plt.title(expressao)
    plt.xlabel("Trimestres")
    plt.legend(loc="lower left", fontsize=10)
    plt.grid()
    plt.ylim(bottom=lowerlimit,top=upperlimit)
    plt.axhline(y=0, color="red", linewidth=1, linestyle='--', label='y=0 line')
    

    for i in range(len(trimestres)):
        plt.text(trimestres[i],info[i]-offset, f"{info[i]}", fontsize=10,color="black",
                 bbox=dict(facecolor="white", alpha=0.5, edgecolor="black"))

    plt.savefig("grafico.png")
    plt.show()


def criaGraficos(expressoes: list[str], trimestres: list[str], title: str="Grafico"):
    for i,expressao in enumerate(expressoes):
        info = calculaInfo(expressao, trimestres)
        plt.plot(trimestres, info, label=expressao, marker='o',color=lineColors[i%3])

    plt.title(title)
    plt.xlabel("Trimestres")
    plt.legend(loc="lower left", fontsize=10)
    plt.grid()

    plt.savefig("grafico.png")
    plt.show()

