from dados_celulas import DadosProduto
from utils import *

dados = DadosProduto("Report1")

print(calculaValor("produto1-ue",dados.vendas))
calulcaDiferenca("produto1-ue-vendas","produto1-")
calulcaTaxa("produto1-ue-vendas","produto1-")
