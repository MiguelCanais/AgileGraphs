def obtemDadosRelatorio(sheet1,sheet2):
    return {
        "pedidos": {
            "prod1": sheet1["AA12"].value,
            "prod2": sheet1["AC12"].value,
            "prod3": sheet1["AE12"].value,
        },

        "produzidos": {
            "prod1": sheet1["AA13"].value,
            "prod2": sheet1["AC13"].value,
            "prod3": sheet1["AE13"].value,
        },

        "rejeitados": {
            "prod1": sheet1["AA14"].value,
            "prod2": sheet1["AC14"].value,
            "prod3": sheet1["AE14"].value,
        },

        "destruidos": {
            "prod1": sheet1["AA15"].value,
            "prod2": sheet1["AC15"].value,
            "prod3": sheet1["AE15"].value,
        },

        "reparados": {
            "prod1": sheet1["AA45"].value,
            "prod2": sheet1["AC45"].value,
            "prod3": sheet1["AE45"].value,
        },

        "reclamacoesWebsite": {
            "prod1": sheet1["AA48"].value,
            "prod2": sheet1["AC48"].value,
            "prod3": sheet1["AE48"].value,
        },

        "entregas": {
            "prod1": {
                "ue":        sheet1["AA18"].value,
                "nafta":     sheet1["AA19"].value,
                "internet":  sheet1["AA20"].value,
            },
            "prod2": {
                "ue":        sheet1["AC18"].value,
                "nafta":     sheet1["AC19"].value,
                "internet":  sheet1["AC20"].value,
            },
            "prod3": {
                "ue":        sheet1["AE18"].value,
                "nafta":     sheet1["AE19"].value,
                "internet":  sheet1["AE20"].value,
            },
        },

        # A quantidade de produtos requesitados
        "encomendas": {
            "prod1": {
                "ue":        sheet1["AA23"].value,
                "nafta":     sheet1["AA24"].value,
                "internet":  sheet1["AA25"].value,
            },
            "prod2": {
                "ue":        sheet1["AC23"].value,
                "nafta":     sheet1["AC24"].value,
                "internet":  sheet1["AC25"].value,
            },
            "prod3": {
                "ue":        sheet1["AE23"].value,
                "nafta":     sheet1["AE24"].value,
                "internet":  sheet1["AE25"].value,
            },
        },

        # A quantidade de vendas
        "vendas": {
            "prod1": {
                "ue":        sheet1["AA28"].value,
                "nafta":     sheet1["AA29"].value,
                "internet":  sheet1["AA30"].value,
            },
            "prod2": {
                "ue":        sheet1["AC28"].value,
                "nafta":     sheet1["AC29"].value,
                "internet":  sheet1["AC30"].value,
            },
            "prod3": {
                "ue":        sheet1["AE28"].value,
                "nafta":     sheet1["AE29"].value,
                "internet":  sheet1["AE30"].value,
            },
        },

        "encomendasAtraso": {
            "prod1": {
                "ue":        sheet1["AA33"].value,
                "nafta":     sheet1["AA34"].value,
            },
            "prod2": {
                "ue":        sheet1["AC33"].value,
                "nafta":     sheet1["AC34"].value,
            },
            "prod3": {
                "ue":        sheet1["AE33"].value,
                "nafta":     sheet1["AE34"].value,
            },
        },

        "inventario": {
            "prod1": {
                "ue":        sheet1["AA37"].value,
                "nafta":     sheet1["AA38"].value,
                "internet":  sheet1["AA39"].value,
            },
            "prod2": {
                "ue":        sheet1["AC37"].value,
                "nafta":     sheet1["AC38"].value,
                "internet":  sheet1["AC39"].value,
            },
            "prod3": {
                "ue":        sheet1["AE37"].value,
                "nafta":     sheet1["AE38"].value,
                "internet":  sheet1["AE39"].value,
            },
        },

        "precos": {
            "prod1": {
                "ue":        sheet1["G16"].value,
                "nafta":     sheet1["G17"].value,
                "internet":  sheet1["G18"].value,
            },
            "prod2": {
                "ue":        sheet1["J16"].value,
                "nafta":     sheet1["J17"].value,
                "internet":  sheet1["J18"].value,
            },
            "prod3": {
                "ue":        sheet1["M18"].value,
                "nafta":     sheet1["M19"].value,
                "internet":  sheet1["M20"].value,
            },
        },

        "publicidade": {
            "prod1": {
                "ue":        sheet1["G21"].value,
                "nafta":     sheet1["G22"].value,
                "internet":  sheet1["G23"].value,
            },
            "prod2": {
                "ue":        sheet1["J21"].value,
                "nafta":     sheet1["J22"].value,
                "internet":  sheet1["J23"].value,
            },
            "prod3": {
                "ue":        sheet1["M21"].value,
                "nafta":     sheet1["M22"].value,
                "internet":  sheet1["M23"].value,
            },
            "institucional": {
                "ue":        sheet1["E21"].value,
                "nafta":     sheet1["E22"].value,
                "internet":  sheet1["E23"].value,
            },
        },

        "montagem": {
            "horasDisponiveis": sheet1["U14"].value,
            "absentismo":       sheet1["U15"].value,
            "horasUtilizadas":  sheet1["U16"].value,
        },

        "maquinacao": {
            "horasDisponiveis": sheet1["U20"].value, 
            "tempoParalizacao": sheet1["U21"].value, 
            "horasConservacao": sheet1["U22"].value, 
            "horasUtilizadas": sheet1["U23"].value, 
            "eficienciaMaquinas": sheet1["U24"].value, 
        },

        "materiaPrima": {
            "inventarioInicial": sheet1["U27"].value,
            "comprasUltimoTrimestre": sheet1["U28"].value,
            "destruida": sheet1["U30"].value,
            "utilizada": sheet1["U31"].value,
            "inventarioArmazem": sheet1["U32"].value,
        },

        "recursosHumanos": {
            "disponivel": {
                "especializados": sheet1["T40"].value,
                "naoEspecializados": sheet1["U40"].value,
            },
            "recrutado": {
                "especializados": sheet1["T41"].value,
                "naoEspecializados": sheet1["U41"].value,
            },
            "formados": {
                "especializados": sheet1["T42"].value,
                "naoEspecializados": sheet1["U42"].value,
            },
            "despedidos": {
                "especializados": sheet1["T43"].value,
                "naoEspecializados": sheet1["U43"].value,
            },
            "abandono": {
                "especializados": sheet1["T44"].value,
                "naoEspecializados": sheet1["U44"].value,
            },
            "disponivelProximoTrimestre": {
                "especializados": sheet1["T45"].value,
                "naoEspecializados": sheet1["U45"].value,
            },
        },

        "distribuidores": {
            "disponivel": {
                "ue": sheet1["S48"].value,
                "nafta": sheet1["T48"].value,
                "internet": sheet1["U48"].value,
            },
            "perdidos": {
                "ue": sheet1["S49"].value,
                "nafta": sheet1["T49"].value,
                "internet": sheet1["U49"].value,
            },
            "rescindidos": {
                "ue": sheet1["S50"].value,
                "nafta": sheet1["T50"].value,
                "internet": sheet1["U50"].value,
            },
            "novos": {
                "ue": sheet1["S51"].value,
                "nafta": sheet1["T51"].value,
                "internet": sheet1["U51"].value,
            },
            "disponivelProximoTrimestre": {
                "ue": sheet1["S52"].value,
                "nafta": sheet1["T52"].value,
                "internet": sheet1["U52"].value,
            },
        },

        "demonstracaoResultados": {
            "vendas":                             sheet2["J5"].value,
            "compraMateriaPrima":                 sheet2["J8"].value,
            "salariosOperariosEspecializados":    sheet2["J9"].value,
            "salariosOperariosNaoEspecializados": sheet2["J10"].value,
            "operacaoMaquinas":                   sheet2["J11"].value,
            "controloQualiade":                   sheet2["J12"].value,
            "custoVendas":                        sheet2["J14"].value,
            "resultadoBruto":                     sheet2["J16"].value,
            "seguros":                            sheet2["J18"].value,
            "rendimentosFinanceiros":             sheet2["J19"].value,
            "gastosFinanceiros":                  sheet2["J20"].value,
            "depreciacoes":                       sheet2["J22"].value,
            "impostos":                           sheet2["J23"].value,
            "lucro":                              sheet2["J25"].value,
        },
    }
