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
