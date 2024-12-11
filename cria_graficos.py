from calcula_info import calculaInfo
import matplotlib.pyplot as plt

lineColors = ["blue","green","red","orange"]

def criaGrafico(expressao: str, trimestres: list[str], title: str="Grafico"):
    info = calculaInfo(expressao, trimestres)

    plt.plot(trimestres, info, label=expressao, marker='o')
    plt.title(expressao)
    plt.xlabel("Trimestres")
    plt.legend(loc="lower left", fontsize=10)
    plt.grid()


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

