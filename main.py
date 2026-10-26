# dicionario cardapio

cardapio = {
 "hamburguer": 25.0,
 "sanduiche": 18.0,
 "batata": 12.0,
 "suco": 8.0,
 "agua": 5.0
}

# lista pedido

pedido = [
 {"produto": "HAMBURGUER", "quantidade": 2},
 {"produto": "batata", "quantidade": 1},
 {"produto": "Suco", "quantidade": 3},
 {"produto": "pizza", "quantidade": 1},
 {"produto": "agua", "quantidade": 0}
]

# dados do pedido

nome = "Felipe"
cupom = "SIM"

# cupom minusculo

patterncupom = cupom.lower()

# dicionario cardapio minusculo

patterncardapio =  {k.lower(): v for k, v in cardapio.items()}

# lista pedido minusculo

patternpedido = [
    {**item, "produto": item["produto"].lower()} 
    for item in pedido
]

# verifica se o item existe no cardápio

def validar_item(produto, quantidade, cardapio):

    if produto not in cardapio or quantidade <= 0:
        return False
    return True

# calcula o subtotal

def calcular_subtotal(quantidade, preco_unitario):
    return quantidade * preco_unitario

# função pedido

def pedido_feito(lista_pedido, dicionario_cardapio):
    itens_validos = []
    subtotal_pedido = 0.0
    linhas_validas = 0
    total_unidades = 0
    
    print("--- Verificação dos Itens ---")
    for item in lista_pedido:
        produto_nome = item["produto"].lower().strip()
        quantidade = item["quantidade"]
        
        # valida o item

        if not validar_item(produto_nome, quantidade, dicionario_cardapio):
            erros_do_item = []
            
            # verifica a existência no cardápio

            if produto_nome not in dicionario_cardapio:
                erros_do_item.append("produto não existe no cardápio")
                
            # verifica quantidade válida

            if quantidade <= 0:
                erros_do_item.append(f"quantidade inválida ({quantidade})")

            # mostra todos os erros do item inválido
            
            motivos = " e ".join(erros_do_item)
            print(f"Item Inválido: '{item['produto']}' Motivo: {motivos}.")
            continue
            
        # consulta o preço e calcula subtotal

        preco_unitario = dicionario_cardapio[produto_nome]
        subtotal_item = calcular_subtotal(quantidade, preco_unitario)
        
        # acumula os totais globais do pedido

        subtotal_pedido += subtotal_item
        linhas_validas += 1
        total_unidades += quantidade
        
        # adiciona o item na lista com seu subtotal calculado

        itens_validos.append({
            "produto": produto_nome,
            "quantidade": quantidade,
            "subtotal": subtotal_item
        })
    
    # verifica a existência de itens válidos no pedido

    if linhas_validas == 0:
        print("Pedido sem itens válidos")
        return [], 0.0, 0, 0
        
    return itens_validos, subtotal_pedido, linhas_validas, total_unidades

# execução da função pedido feito

itens, subtotal, linhas, unidades = pedido_feito(patternpedido, patterncardapio)

# função de classificar pedido

def classificar_pedido(subtotal):
    pedido = subtotal
    if pedido <= 50:
        tipo_de_pedido = "Pedido pequeno"
    elif pedido <= 100:
        tipo_de_pedido = "Pedido médio" 
    else:
        tipo_de_pedido = "Pedido grande"
    return tipo_de_pedido

tipo_de_pedido = classificar_pedido(subtotal)

#função desconto

def calcular_desconto(subtotal, cupom,tipo_de_pedido):

    if cupom == "sim":
        if tipo_de_pedido == "Pedido pequeno":
            return subtotal*0.05
        elif tipo_de_pedido == "Pedido médio" :
            return subtotal*0.1
        elif tipo_de_pedido == "Pedido grande":
            return subtotal*0.15
    if cupom == "nao":
        if tipo_de_pedido == "Pedido pequeno":
            return 0
        elif tipo_de_pedido == "Pedido médio" :
            return subtotal*0.05
        elif tipo_de_pedido == "Pedido grande":
            return subtotal*0.10
    return 0

# desconto total

descontototal = calcular_desconto(subtotal,patterncupom,tipo_de_pedido)

total = subtotal - descontototal
