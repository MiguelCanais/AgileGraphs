from openpyxl import load_workbook

class DadosProduto:
    def __init__(self, fileName):
        wb = load_workbook(f"./relatorios/{fileName}.xlsx")
        self.sheet = wb["Excel_1"]

        self.produzidos = {
            "produto1": self.sheet["AA13"].value,
            "produto2": self.sheet["AC13"].value,
            "produto3": self.sheet["AE13"].value,
        }

        # A quantidade de produtos que a empresa entregou
        self.entregas = {
            "produto1": {
                "ue":        self.sheet["AA18"].value,
                "nafta":     self.sheet["AA19"].value,
                "internet":  self.sheet["AA20"].value,
            },
            "produto2": {
                "ue":        self.sheet["AC18"].value,
                "nafta":     self.sheet["AC19"].value,
                "internet":  self.sheet["AC20"].value,
            },
            "produto3": {
                "ue":        self.sheet["AE18"].value,
                "nafta":     self.sheet["AE19"].value,
                "internet":  self.sheet["AE20"].value,
            },
        }

        # A quantidade de produtos requesitados
        self.encomendas = {
            "produto1": {
                "ue":        self.sheet["AA23"].value,
                "nafta":     self.sheet["AA24"].value,
                "internet":  self.sheet["AA25"].value,
            },
            "produto2": {
                "ue":        self.sheet["AC23"].value,
                "nafta":     self.sheet["AC24"].value,
                "internet":  self.sheet["AC25"].value,
            },
            "produto3": {
                "ue":        self.sheet["AE23"].value,
                "nafta":     self.sheet["AE24"].value,
                "internet":  self.sheet["AE25"].value,
            },
        }

        # A quantidade de vendas
        self.vendas = {
            "produto1": {
                "ue":        self.sheet["AA28"].value,
                "nafta":     self.sheet["AA29"].value,
                "internet":  self.sheet["AA30"].value,
            },
            "produto2": {
                "ue":        self.sheet["AC28"].value,
                "nafta":     self.sheet["AC29"].value,
                "internet":  self.sheet["AC30"].value,
            },
            "produto3": {
                "ue":        self.sheet["AE28"].value,
                "nafta":     self.sheet["AE29"].value,
                "internet":  self.sheet["AE30"].value,
            },
        }

        self.encomendasAtraso = {
            "produto1": {
                "ue":        self.sheet["AA33"].value,
                "nafta":     self.sheet["AA34"].value,
            },
            "produto2": {
                "ue":        self.sheet["AC33"].value,
                "nafta":     self.sheet["AC34"].value,
            },
            "produto3": {
                "ue":        self.sheet["AE33"].value,
                "nafta":     self.sheet["AE34"].value,
            },
        }
