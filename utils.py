def calcula(tipo,dados):
    tipo = tipo.lower()
    total = 0

    # Calcula Total
    if tipo == "total":
        for produto,val in dados.items():
            if isinstance(val,dict):
                total += calcula(produto,dados)
            else:
                total += val

    # Calcula Produto
    elif tipo.startswith("produto"):
        if isinstance(dados[tipo],dict):
            for vendasMercado in dados[tipo].values():
                total += vendasMercado
        else:
            total += dados[tipo]
    
    # Calcula Mercado
    else:
        for produto in dados.values():
            total += produto[tipo]

    return total
