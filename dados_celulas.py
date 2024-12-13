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

    "transportes": {
        "distanciaViagem": {
            "ue": ("sheet1", "AA51"),
            "nafta": ("sheet1", "AC51"),
            "internet": ("sheet1", "AE51"),
        },
        "numeroCargas": {
            "ue": ("sheet1", "AA52"),
            "nafta": ("sheet1", "AC52"),
            "internet": ("sheet1", "AE52"),
        },
    },

    "website": {
        "portasDisponiveis":  ("sheet1", "J51"),
        "visitas":            ("sheet1", "J52"),
        "tentativasFalhadas": ("sheet1", "J53"),
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
            "ue": ("sheet1", "M16"),
            "nafta": ("sheet1", "M17"),
            "internet": ("sheet1", "M18"),
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

    "tempoMontagem": {
        "prod1": ("sheet1", "G25"),
        "prod2": ("sheet1", "J25"),
        "prod3": ("sheet1", "M25"),
    },

    "investigacao": {
        "prod1": ("sheet1", "G27"),
        "prod2": ("sheet1", "J27"),
        "prod3": ("sheet1", "M27"),
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

    "balanco": {
        "ativoFixoTangivel": ("sheet2","Q6"),
        "maquinas": ("sheet2","Q7"),
        "ativoNaoCorrente": ("sheet2","R8"),
        "inventarioProdutos": ("sheet2","R9"),
        "inventarioMateriaPrima": ("sheet2","R10"),
        "clientes": ("sheet2","R11"),
        "depositosBancarios": ("sheet2","R12"),
        "outrosAtivos": ("sheet2","R13"),
        "totalAtivo": ("sheet2","R14"),
        "estado": ("sheet2","R17"),
        "fornecedores": ("sheet2","R18"),
        "financiamentos": ("sheet2","R19"),
        "emprestimosSemGarantia": ("sheet2","R20"),
        "passivoCorrente": ("sheet2","R21"),
        "emprestimosMedioPrazo": ("sheet2","R22"),
        "capitalProprioPassivo": ("sheet2","R23"),
        "capitalSocial": ("sheet2","R26"),
        "resultadosTransitados": ("sheet2","R27"),
        "capitaisProprios": ("sheet2","R28"),
    },

    "acoes": {
        "empresa1": ("sheet2","D32"),
        "empresa2": ("sheet2","E32"),
        "empresa3": ("sheet2","F32"),
        "empresa4": ("sheet2","G32"),
        "empresa5": ("sheet2","H32"),
        "empresa6": ("sheet2","I32"),
        "empresa7": ("sheet2","J32"),
    },

    "quotasMercado": {
        "empresa1": {
            "prod1": {
                "ue": ("sheet2", "Q32"),
                "nafta": ("sheet2", "Q33"),
                "internet": ("sheet2", "Q34"),
            },
            "prod2": {
                "ue": ("sheet2", "Q35"),
                "nafta": ("sheet2", "Q36"),
                "internet": ("sheet2", "Q37"),
            },
            "prod3": {
                "ue": ("sheet2", "Q38"),
                "nafta": ("sheet2", "Q39"),
                "internet": ("sheet2", "Q40"),
            },
        },
        "empresa2": {
            "prod1": {
                "ue": ("sheet2", "R32"),
                "nafta": ("sheet2", "R33"),
                "internet": ("sheet2", "R34"),
            },
            "prod2": {
                "ue": ("sheet2", "R35"),
                "nafta": ("sheet2", "R36"),
                "internet": ("sheet2", "R37"),
            },
            "prod3": {
                "ue": ("sheet2", "R38"),
                "nafta": ("sheet2", "R39"),
                "internet": ("sheet2", "R40"),
            },
        },
        "empresa3": {
            "prod1": {
                "ue": ("sheet2", "S32"),
                "nafta": ("sheet2", "S33"),
                "internet": ("sheet2", "S34"),
            },
            "prod2": {
                "ue": ("sheet2", "S35"),
                "nafta": ("sheet2", "S36"),
                "internet": ("sheet2", "S37"),
            },
            "prod3": {
                "ue": ("sheet2", "S38"),
                "nafta": ("sheet2", "S39"),
                "internet": ("sheet2", "S40"),
            },
        },
        "empresa4": {
            "prod1": {
                "ue": ("sheet2", "T32"),
                "nafta": ("sheet2", "T33"),
                "internet": ("sheet2", "T34"),
            },
            "prod2": {
                "ue": ("sheet2", "T35"),
                "nafta": ("sheet2", "T36"),
                "internet": ("sheet2", "T37"),
            },
            "prod3": {
                "ue": ("sheet2", "T38"),
                "nafta": ("sheet2", "T39"),
                "internet": ("sheet2", "T40"),
            },
        },
        "empresa5": {
            "prod1": {
                "ue": ("sheet2", "U32"),
                "nafta": ("sheet2", "U33"),
                "internet": ("sheet2", "U34"),
            },
            "prod2": {
                "ue": ("sheet2", "U35"),
                "nafta": ("sheet2", "U36"),
                "internet": ("sheet2", "U37"),
            },
            "prod3": {
                "ue": ("sheet2", "U38"),
                "nafta": ("sheet2", "U39"),
                "internet": ("sheet2", "U40"),
            },
        },
        "empresa6": {
            "prod1": {
                "ue": ("sheet2", "V32"),
                "nafta": ("sheet2", "V33"),
                "internet": ("sheet2", "V34"),
            },
            "prod2": {
                "ue": ("sheet2", "V35"),
                "nafta": ("sheet2", "V36"),
                "internet": ("sheet2", "V37"),
            },
            "prod3": {
                "ue": ("sheet2", "V38"),
                "nafta": ("sheet2", "V39"),
                "internet": ("sheet2", "V40"),
            },
        },
        "empresa7": {
            "prod1": {
                "ue": ("sheet2", "W32"),
                "nafta": ("sheet2", "W33"),
                "internet": ("sheet2", "W34"),
            },
            "prod2": {
                "ue": ("sheet2", "W35"),
                "nafta": ("sheet2", "W36"),
                "internet": ("sheet2", "W37"),
            },
            "prod3": {
                "ue": ("sheet2", "W38"),
                "nafta": ("sheet2", "W39"),
                "internet": ("sheet2", "W40"),
            },
        },
    },

    "balancoEmpresas": {
        "empresa1": {
            "ativoFixoTangivel": ("sheet2", "Q45"),
            "maquinas": ("sheet2", "Q46"),
            "inventarioProdutos": ("sheet2", "Q47"),
            "inventarioMateriaPrima": ("sheet2", "Q48"),
            "clientes": ("sheet2", "Q49"),
            "caixa": ("sheet2", "Q50"),    
            "impostos": ("sheet2", "Q53"),
            "fornecedores": ("sheet2", "Q54"),
            "financiamentos": ("sheet2", "Q55"),
            "emprestimosSemGarantia": ("sheet2", "Q56"),
            "emprestimosMedioPrazo": ("sheet2", "Q57"),
            "capitalProprioPassivo": ("sheet2", "Q58"),
            "capitalSocial": ("sheet2", "Q60"),
            "resultadosTransitados": ("sheet2", "Q61"),
            "capitaisProprios": ("sheet2", "Q62"),
        },
        "empresa2": {
            "ativoFixoTangivel": ("sheet2", "R45"),
            "maquinas": ("sheet2", "R46"),
            "inventarioProdutos": ("sheet2", "R47"),
            "inventarioMateriaPrima": ("sheet2", "R48"),
            "clientes": ("sheet2", "R49"),
            "caixa": ("sheet2", "R50"),    
            "impostos": ("sheet2", "R53"),
            "fornecedores": ("sheet2", "R54"),
            "financiamentos": ("sheet2", "R55"),
            "emprestimosSemGarantia": ("sheet2", "R56"),
            "emprestimosMedioPrazo": ("sheet2", "R57"),
            "capitalProprioPassivo": ("sheet2", "R58"),
            "capitalSocial": ("sheet2", "R60"),
            "resultadosTransitados": ("sheet2", "R61"),
            "capitaisProprios": ("sheet2", "R62"),
        },
        "empresa3": {
            "ativoFixoTangivel": ("sheet2", "S45"),
            "maquinas": ("sheet2", "S46"),
            "inventarioProdutos": ("sheet2", "S47"),
            "inventarioMateriaPrima": ("sheet2", "S48"),
            "clientes": ("sheet2", "S49"),
            "caixa": ("sheet2", "S50"),    
            "impostos": ("sheet2", "S53"),
            "fornecedores": ("sheet2", "S54"),
            "financiamentos": ("sheet2", "S55"),
            "emprestimosSemGarantia": ("sheet2", "S56"),
            "emprestimosMedioPrazo": ("sheet2", "S57"),
            "capitalProprioPassivo": ("sheet2", "S58"),
            "capitalSocial": ("sheet2", "S60"),
            "resultadosTransitados": ("sheet2", "S61"),
            "capitaisProprios": ("sheet2", "S62"),
        },
        "empresa4": {
            "ativoFixoTangivel": ("sheet2", "T45"),
            "maquinas": ("sheet2", "T46"),
            "inventarioProdutos": ("sheet2", "T47"),
            "inventarioMateriaPrima": ("sheet2", "T48"),
            "clientes": ("sheet2", "T49"),
            "caixa": ("sheet2", "T50"),    
            "impostos": ("sheet2", "T53"),
            "fornecedores": ("sheet2", "T54"),
            "financiamentos": ("sheet2", "T55"),
            "emprestimosSemGarantia": ("sheet2", "T56"),
            "emprestimosMedioPrazo": ("sheet2", "T57"),
            "capitalProprioPassivo": ("sheet2", "T58"),
            "capitalSocial": ("sheet2", "T60"),
            "resultadosTransitados": ("sheet2", "T61"),
            "capitaisProprios": ("sheet2", "T62"),
        },
        "empresa5": {
            "ativoFixoTangivel": ("sheet2", "U45"),
            "maquinas": ("sheet2", "U46"),
            "inventarioProdutos": ("sheet2", "U47"),
            "inventarioMateriaPrima": ("sheet2", "U48"),
            "clientes": ("sheet2", "U49"),
            "caixa": ("sheet2", "U50"),    
            "impostos": ("sheet2", "U53"),
            "fornecedores": ("sheet2", "U54"),
            "financiamentos": ("sheet2", "U55"),
            "emprestimosSemGarantia": ("sheet2", "U56"),
            "emprestimosMedioPrazo": ("sheet2", "U57"),
            "capitalProprioPassivo": ("sheet2", "U58"),
            "capitalSocial": ("sheet2", "U60"),
            "resultadosTransitados": ("sheet2", "U61"),
            "capitaisProprios": ("sheet2", "U62"),
        },
        "empresa6": {
            "ativoFixoTangivel": ("sheet2", "V45"),
            "maquinas": ("sheet2", "V46"),
            "inventarioProdutos": ("sheet2", "V47"),
            "inventarioMateriaPrima": ("sheet2", "V48"),
            "clientes": ("sheet2", "V49"),
            "caixa": ("sheet2", "V50"),    
            "impostos": ("sheet2", "V53"),
            "fornecedores": ("sheet2", "V54"),
            "financiamentos": ("sheet2", "V55"),
            "emprestimosSemGarantia": ("sheet2", "V56"),
            "emprestimosMedioPrazo": ("sheet2", "V57"),
            "capitalProprioPassivo": ("sheet2", "V58"),
            "capitalSocial": ("sheet2", "V60"),
            "resultadosTransitados": ("sheet2", "V61"),
            "capitaisProprios": ("sheet2", "V62"),
        },
        "empresa7": {
            "ativoFixoTangivel": ("sheet2", "W45"),
            "maquinas": ("sheet2", "W46"),
            "inventarioProdutos": ("sheet2", "W47"),
            "inventarioMateriaPrima": ("sheet2", "W48"),
            "clientes": ("sheet2", "W49"),
            "caixa": ("sheet2", "W50"),    
            "impostos": ("sheet2", "W53"),
            "fornecedores": ("sheet2", "W54"),
            "financiamentos": ("sheet2", "W55"),
            "emprestimosSemGarantia": ("sheet2", "W56"),
            "emprestimosMedioPrazo": ("sheet2", "W57"),
            "capitalProprioPassivo": ("sheet2", "W58"),
            "capitalSocial": ("sheet2", "W60"),
            "resultadosTransitados": ("sheet2", "W61"),
            "capitaisProprios": ("sheet2", "W62"),
        },
    },

    "precosEmpresas": {
        "empresa1": {
            "prod1": {
                "ue": ("sheet2", "D38"),
                "nafta": ("sheet2", "D39"),
                "internet": ("sheet2", "D40"),
            },
            "prod2": {
                "ue": ("sheet2", "D41"),
                "nafta": ("sheet2", "D42"),
                "internet": ("sheet2", "D43"),
            },
            "prod3": {
                "ue": ("sheet2", "D44"),
                "nafta": ("sheet2", "D45"),
                "internet": ("sheet2", "D46"),
            },
        },
        "empresa2": {
            "prod1": {
                "ue": ("sheet2", "E38"),
                "nafta": ("sheet2", "E39"),
                "internet": ("sheet2", "E40"),
            },
            "prod2": {
                "ue": ("sheet2", "E41"),
                "nafta": ("sheet2", "E42"),
                "internet": ("sheet2", "E43"),
            },
            "prod3": {
                "ue": ("sheet2", "E44"),
                "nafta": ("sheet2", "E45"),
                "internet": ("sheet2", "E46"),
            },
        },
        "empresa3": {
            "prod1": {
                "ue": ("sheet2", "F38"),
                "nafta": ("sheet2", "F39"),
                "internet": ("sheet2", "F40"),
            },
            "prod2": {
                "ue": ("sheet2", "F41"),
                "nafta": ("sheet2", "F42"),
                "internet": ("sheet2", "F43"),
            },
            "prod3": {
                "ue": ("sheet2", "F44"),
                "nafta": ("sheet2", "F45"),
                "internet": ("sheet2", "F46"),
            },
        },
        "empresa4": {
            "prod1": {
                "ue": ("sheet2", "G38"),
                "nafta": ("sheet2", "G39"),
                "internet": ("sheet2", "G40"),
            },
            "prod2": {
                "ue": ("sheet2", "G41"),
                "nafta": ("sheet2", "G42"),
                "internet": ("sheet2", "G43"),
            },
            "prod3": {
                "ue": ("sheet2", "G44"),
                "nafta": ("sheet2", "G45"),
                "internet": ("sheet2", "G46"),
            },
        },
        "empresa5": {
            "prod1": {
                "ue": ("sheet2", "H38"),
                "nafta": ("sheet2", "H39"),
                "internet": ("sheet2", "H40"),
            },
            "prod2": {
                "ue": ("sheet2", "H41"),
                "nafta": ("sheet2", "H42"),
                "internet": ("sheet2", "H43"),
            },
            "prod3": {
                "ue": ("sheet2", "H44"),
                "nafta": ("sheet2", "H45"),
                "internet": ("sheet2", "H46"),
            },
        },
        "empresa6": {
            "prod1": {
                "ue": ("sheet2", "I38"),
                "nafta": ("sheet2", "I39"),
                "internet": ("sheet2", "I40"),
            },
            "prod2": {
                "ue": ("sheet2", "I41"),
                "nafta": ("sheet2", "I42"),
                "internet": ("sheet2", "I43"),
            },
            "prod3": {
                "ue": ("sheet2", "I44"),
                "nafta": ("sheet2", "I45"),
                "internet": ("sheet2", "I46"),
            },
        },
        "empresa7": {
            "prod1": {
                "ue": ("sheet2", "J38"),
                "nafta": ("sheet2", "J39"),
                "internet": ("sheet2", "J40"),
            },
            "prod2": {
                "ue": ("sheet2", "J41"),
                "nafta": ("sheet2", "J42"),
                "internet": ("sheet2", "J43"),
            },
            "prod3": {
                "ue": ("sheet2", "J44"),
                "nafta": ("sheet2", "J45"),
                "internet": ("sheet2", "J46"),
            },
        },
    },

    "informacoesEmpresas": {
        "empresa1": {
            "totalEmpregados": ("sheet2", "D47"),
            "salario": ("sheet2", "D48"),
            "distribuidores": ("sheet2", "D49"),
            "publicidade": ("sheet2", "D53"),
            "investigacao": ("sheet2", "D54"),
            "eficienciaWebsite": ("sheet2", "D59"),
        },
        "empresa2": {
            "totalEmpregados": ("sheet2", "E47"),
            "salario": ("sheet2", "E48"),
            "distribuidores": ("sheet2", "E49"),
            "publicidade": ("sheet2", "E53"),
            "investigacao": ("sheet2", "E54"),
            "eficienciaWebsite": ("sheet2", "E59"),
        },
        "empresa3": {
            "totalEmpregados": ("sheet2", "F47"),
            "salario": ("sheet2", "F48"),
            "distribuidores": ("sheet2", "F49"),
            "publicidade": ("sheet2", "F53"),
            "investigacao": ("sheet2", "F54"),
            "eficienciaWebsite": ("sheet2", "F59"),
        },
        "empresa4": {
            "totalEmpregados": ("sheet2", "G47"),
            "salario": ("sheet2", "G48"),
            "distribuidores": ("sheet2", "G49"),
            "publicidade": ("sheet2", "G53"),
            "investigacao": ("sheet2", "G54"),
            "eficienciaWebsite": ("sheet2", "G59"),
        },
        "empresa5": {
            "totalEmpregados": ("sheet2", "H47"),
            "salario": ("sheet2", "H48"),
            "distribuidores": ("sheet2", "H49"),
            "publicidade": ("sheet2", "H53"),
            "investigacao": ("sheet2", "H54"),
            "eficienciaWebsite": ("sheet2", "H59"),
        },
        "empresa6": {
            "totalEmpregados": ("sheet2", "I47"),
            "salario": ("sheet2", "I48"),
            "distribuidores": ("sheet2", "I49"),
            "publicidade": ("sheet2", "I53"),
            "investigacao": ("sheet2", "I54"),
            "eficienciaWebsite": ("sheet2", "I59"),
        },
        "empresa7": {
            "totalEmpregados": ("sheet2", "J47"),
            "salario": ("sheet2", "J48"),
            "distribuidores": ("sheet2", "J49"),
            "publicidade": ("sheet2", "J53"),
            "investigacao": ("sheet2", "J54"),
            "eficienciaWebsite": ("sheet2", "J59"),
        },
    },
}
