def obtemDadosRelatorio(sheet):
    return {
        "pedidos": {
            "prod1": sheet["AA12"].value,
            "prod2": sheet["AC12"].value,
            "prod3": sheet["AE12"].value,
        },

        "produzidos": {
            "prod1": sheet["AA13"].value,
            "prod2": sheet["AC13"].value,
            "prod3": sheet["AE13"].value,
        },

        "rejeitados": {
            "prod1": sheet["AA14"].value,
            "prod2": sheet["AC14"].value,
            "prod3": sheet["AE14"].value,
        },

        "destruidos": {
            "prod1": sheet["AA15"].value,
            "prod2": sheet["AC15"].value,
            "prod3": sheet["AE15"].value,
        },

        "reparados": {
            "prod1": sheet["AA45"].value,
            "prod2": sheet["AC45"].value,
            "prod3": sheet["AE45"].value,
        },

        "reclamacoesWebsite": {
            "prod1": sheet["AA48"].value,
            "prod2": sheet["AC48"].value,
            "prod3": sheet["AE48"].value,
        },

        "entregas": {
            "prod1": {
                "ue":        sheet["AA18"].value,
                "nafta":     sheet["AA19"].value,
                "internet":  sheet["AA20"].value,
            },
            "prod2": {
                "ue":        sheet["AC18"].value,
                "nafta":     sheet["AC19"].value,
                "internet":  sheet["AC20"].value,
            },
            "prod3": {
                "ue":        sheet["AE18"].value,
                "nafta":     sheet["AE19"].value,
                "internet":  sheet["AE20"].value,
            },
        },

        # A quantidade de produtos requesitados
        "encomendas": {
            "prod1": {
                "ue":        sheet["AA23"].value,
                "nafta":     sheet["AA24"].value,
                "internet":  sheet["AA25"].value,
            },
            "prod2": {
                "ue":        sheet["AC23"].value,
                "nafta":     sheet["AC24"].value,
                "internet":  sheet["AC25"].value,
            },
            "prod3": {
                "ue":        sheet["AE23"].value,
                "nafta":     sheet["AE24"].value,
                "internet":  sheet["AE25"].value,
            },
        },

        # A quantidade de vendas
        "vendas": {
            "prod1": {
                "ue":        sheet["AA28"].value,
                "nafta":     sheet["AA29"].value,
                "internet":  sheet["AA30"].value,
            },
            "prod2": {
                "ue":        sheet["AC28"].value,
                "nafta":     sheet["AC29"].value,
                "internet":  sheet["AC30"].value,
            },
            "prod3": {
                "ue":        sheet["AE28"].value,
                "nafta":     sheet["AE29"].value,
                "internet":  sheet["AE30"].value,
            },
        },

        "encomendasAtraso": {
            "prod1": {
                "ue":        sheet["AA33"].value,
                "nafta":     sheet["AA34"].value,
            },
            "prod2": {
                "ue":        sheet["AC33"].value,
                "nafta":     sheet["AC34"].value,
            },
            "prod3": {
                "ue":        sheet["AE33"].value,
                "nafta":     sheet["AE34"].value,
            },
        },

        "inventario": {
            "prod1": {
                "ue":        sheet["AA37"].value,
                "nafta":     sheet["AA38"].value,
                "internet":  sheet["AA39"].value,
            },
            "prod2": {
                "ue":        sheet["AC37"].value,
                "nafta":     sheet["AC38"].value,
                "internet":  sheet["AC39"].value,
            },
            "prod3": {
                "ue":        sheet["AE37"].value,
                "nafta":     sheet["AE38"].value,
                "internet":  sheet["AE39"].value,
            },
        },

        "montagem": {
            "horasDisponiveis": sheet["U14"].value,
            "absentismo":       sheet["U15"].value,
            "horasUtilizadas":  sheet["U16"].value,
        },

        "maquinacao": {
            "horasDisponiveis": sheet["U20"].value, 
            "tempoParalizacao": sheet["U21"].value, 
            "horasConservacao": sheet["U22"].value, 
            "horasUtilizadas": sheet["U23"].value, 
            "eficienciaMaquinas": sheet["U24"].value, 
        },

        "materiaPrima": {
            "inventarioInicial": sheet["U27"].value,
            "comprasUltimoTrimestre": sheet["U28"].value,
            "destruida": sheet["U30"].value,
            "utilizada": sheet["U31"].value,
            "inventarioArmazem": sheet["U32"].value,
        },

        "recursosHumanos": {
            "disponivel": {
                "especializados": sheet["T40"].value,
                "naoEspecializados": sheet["U40"].value,
            },
            "recrutado": {
                "especializados": sheet["T41"].value,
                "naoEspecializados": sheet["U41"].value,
            },
            "formados": {
                "especializados": sheet["T42"].value,
                "naoEspecializados": sheet["U42"].value,
            },
            "despedidos": {
                "especializados": sheet["T43"].value,
                "naoEspecializados": sheet["U43"].value,
            },
            "abandono": {
                "especializados": sheet["T44"].value,
                "naoEspecializados": sheet["U44"].value,
            },
            "disponivelProximoTrimestre": {
                "especializados": sheet["T45"].value,
                "naoEspecializados": sheet["U45"].value,
            },
        },

        "distribuidores": {
            "disponivel": {
                "ue": sheet["S48"].value,
                "nafta": sheet["T48"].value,
                "internet": sheet["U48"].value,
            },
            "perdidos": {
                "ue": sheet["S49"].value,
                "nafta": sheet["T49"].value,
                "internet": sheet["U49"].value,
            },
            "rescindidos": {
                "ue": sheet["S50"].value,
                "nafta": sheet["T50"].value,
                "internet": sheet["U50"].value,
            },
            "novos": {
                "ue": sheet["S51"].value,
                "nafta": sheet["T51"].value,
                "internet": sheet["U51"].value,
            },
            "disponivelProximoTrimestre": {
                "ue": sheet["S52"].value,
                "nafta": sheet["T52"].value,
                "internet": sheet["U52"].value,
            },
        }
    }
