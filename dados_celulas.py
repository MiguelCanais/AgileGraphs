dados_relatorio = {
    "pedidos": {
        "prod1": ("sheet1", "AA12"),
        "prod2": ("sheet1", "AC12"),
        "prod3": ("sheet1", "AE12"),
    },

    "produzidos": {
        "prod1": ("sheet1", "AA13"),
        "prod2": ("sheet1", "AC13"),
        "prod3": ("sheet1", "AE13"),
    },

    "rejeitados": {
        "prod1": ("sheet1", "AA14"),
        "prod2": ("sheet1", "AC14"),
        "prod3": ("sheet1", "AE14"),
    },

    "destruidos": {
        "prod1": ("sheet1", "AA15"),
        "prod2": ("sheet1", "AC15"),
        "prod3": ("sheet1", "AE15"),
    },

    "reparados": {
        "prod1": ("sheet1", "AA45"),
        "prod2": ("sheet1", "AC45"),
        "prod3": ("sheet1", "AE45"),
    },

    "reclamacoesWebsite": {
        "prod1": ("sheet1", "AA48"),
        "prod2": ("sheet1", "AC48"),
        "prod3": ("sheet1", "AE48"),
    },

    "entregas": {
        "prod1": {
            "ue": ("sheet1", "AA18"),
            "nafta": ("sheet1", "AA19"),
            "internet": ("sheet1", "AA20"),
        },
        "prod2": {
            "ue": ("sheet1", "AC18"),
            "nafta": ("sheet1", "AC19"),
            "internet": ("sheet1", "AC20"),
        },
        "prod3": {
            "ue": ("sheet1", "AE18"),
            "nafta": ("sheet1", "AE19"),
            "internet": ("sheet1", "AE20"),
        },
    },

    # A quantidade de produtos requesitados
    "encomendas": {
        "prod1": {
            "ue": ("sheet1", "AA23"),
            "nafta": ("sheet1", "AA24"),
            "internet": ("sheet1", "AA25"),
        },
        "prod2": {
            "ue": ("sheet1", "AC23"),
            "nafta": ("sheet1", "AC24"),
            "internet": ("sheet1", "AC25"),
        },
        "prod3": {
            "ue": ("sheet1", "AE23"),
            "nafta": ("sheet1", "AE24"),
            "internet": ("sheet1", "AE25"),
        },
    },

    # A quantidade de vendas
    "vendas": {
        "prod1": {
            "ue": ("sheet1", "AA28"),
            "nafta": ("sheet1", "AA29"),
            "internet": ("sheet1", "AA30"),
        },
        "prod2": {
            "ue": ("sheet1", "AC28"),
            "nafta": ("sheet1", "AC29"),
            "internet": ("sheet1", "AC30"),
        },
        "prod3": {
            "ue": ("sheet1", "AE28"),
            "nafta": ("sheet1", "AE29"),
            "internet": ("sheet1", "AE30"),
        },
    },

    "encomendasAtraso": {
        "prod1": {
            "ue": ("sheet1", "AA33"),
            "nafta": ("sheet1", "AA34"),
        },
        "prod2": {
            "ue": ("sheet1", "AC33"),
            "nafta": ("sheet1", "AC34"),
        },
        "prod3": {
            "ue": ("sheet1", "AE33"),
            "nafta": ("sheet1", "AE34"),
        },
    },

    "inventario": {
        "prod1": {
            "ue": ("sheet1", "AA37"),
            "nafta": ("sheet1", "AA38"),
            "internet": ("sheet1", "AA39"),
        },
        "prod2": {
            "ue": ("sheet1", "AC37"),
            "nafta": ("sheet1", "AC38"),
            "internet": ("sheet1", "AC39"),
        },
        "prod3": {
            "ue": ("sheet1", "AE37"),
            "nafta": ("sheet1", "AE38"),
            "internet": ("sheet1", "AE39"),
        },
    },

    "precos": {
        "prod1": {
            "ue": ("sheet1", "G16"),
            "nafta": ("sheet1", "G17"),
            "internet": ("sheet1", "G18"),
        },
        "prod2": {
            "ue": ("sheet1", "J16"),
            "nafta": ("sheet1", "J17"),
            "internet": ("sheet1", "J18"),
        },
        "prod3": {
            "ue": ("sheet1", "M18"),
            "nafta": ("sheet1", "M19"),
            "internet": ("sheet1", "M20"),
        },
    },

    "publicidade": {
        "prod1": {
            "ue": ("sheet1", "G21"),
            "nafta": ("sheet1", "G22"),
            "internet": ("sheet1", "G23"),
        },
        "prod2": {
            "ue": ("sheet1", "J21"),
            "nafta": ("sheet1", "J22"),
            "internet": ("sheet1", "J23"),
        },
        "prod3": {
            "ue": ("sheet1", "M21"),
            "nafta": ("sheet1", "M22"),
            "internet": ("sheet1", "M23"),
        },
        "institucional": {
            "ue": ("sheet1", "E21"),
            "nafta": ("sheet1", "E22"),
            "internet": ("sheet1", "E23"),
        },
    },

    "montagem": {
        "horasDisponiveis": ("sheet1", "U14"),
        "absentismo": ("sheet1", "U15"),
        "horasUtilizadas": ("sheet1", "U16"),
    },

    "maquinacao": {
        "horasDisponiveis": ("sheet1", "U20"),
        "tempoParalizacao": ("sheet1", "U21"),
        "horasConservacao": ("sheet1", "U22"),
        "horasUtilizadas": ("sheet1", "U23"),
        "eficienciaMaquinas": ("sheet1", "U24"),
    },

    "materiaPrima": {
        "inventarioInicial": ("sheet1", "U27"),
        "comprasUltimoTrimestre": ("sheet1", "U28"),
        "destruida": ("sheet1", "U30"),
        "utilizada": ("sheet1", "U31"),
        "inventarioArmazem": ("sheet1", "U32"),
    },

    "recursosHumanos": {
        "disponivel": {
            "especializados": ("sheet1", "T40"),
            "naoEspecializados": ("sheet1", "U40"),
        },
        "recrutado": {
            "especializados": ("sheet1", "T41"),
            "naoEspecializados": ("sheet1", "U41"),
        },
        "formados": {
            "especializados": ("sheet1", "T42"),
            "naoEspecializados": ("sheet1", "U42"),
        },
        "despedidos": {
            "especializados": ("sheet1", "T43"),
            "naoEspecializados": ("sheet1", "U43"),
        },
        "abandono": {
            "especializados": ("sheet1", "T44"),
            "naoEspecializados": ("sheet1", "U44"),
        },
        "disponivelProximoTrimestre": {
            "especializados": ("sheet1", "T45"),
            "naoEspecializados": ("sheet1", "U45"),
        },
    },

    "distribuidores": {
        "disponivel": {
            "ue": ("sheet1", "S48"),
            "nafta": ("sheet1", "T48"),
            "internet": ("sheet1", "U48"),
        },
        "perdidos": {
            "ue": ("sheet1", "S49"),
            "nafta": ("sheet1", "T49"),
            "internet": ("sheet1", "U49"),
        },
        "rescindidos": {
            "ue": ("sheet1", "S50"),
            "nafta": ("sheet1", "T50"),
            "internet": ("sheet1", "U50"),
        },
        "novos": {
            "ue": ("sheet1", "S51"),
            "nafta": ("sheet1", "T51"),
            "internet": ("sheet1", "U51"),
        },
        "disponivelProximoTrimestre": {
            "ue": ("sheet1", "S52"),
            "nafta": ("sheet1", "T52"),
            "internet": ("sheet1", "U52"),
        },
    },

    "demonstracaoResultados": {
        "vendas": ("sheet2", "J5"),
        "compraMateriaPrima": ("sheet2", "J8"),
        "salariosOperariosEspecializados": ("sheet2", "J9"),
        "salariosOperariosNaoEspecializados": ("sheet2", "J10"),
        "operacaoMaquinas": ("sheet2", "J11"),
        "controloQualiade": ("sheet2", "J12"),
        "custoVendas": ("sheet2", "J14"),
        "resultadoBruto": ("sheet2", "J16"),
        "seguros": ("sheet2", "J18"),
        "rendimentosFinanceiros": ("sheet2", "J19"),
        "gastosFinanceiros": ("sheet2", "J20"),
        "depreciacoes": ("sheet2", "J22"),
        "impostos": ("sheet2", "J23"),
        "lucro": ("sheet2", "J25"),
    },
}
