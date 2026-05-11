def test_deve_cancelar_pedido_com_sucesso(client):
    # TODO: criar cliente
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})

    # TODO: criar produto
    client.post("/produtos", json={"codigo": 1, "valor": 10, "tipo": 1, "desconto_percentual": 10})

    # TODO: criar pedido
    client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 10})

    response = client.post("/lanchonete/pedidos/1/cancelar")

    assert response.status_code == 200

    data = response.json()

    # TODO: validar se data["ok"] é True
    assert data['ok'] == True

    # TODO: validar mensagem de sucesso
    assert data['mensagem'] == "Pedido cancelado com sucesso"

def test_nao_deve_cancelar_pedido_inexistente(client):
    response = client.post("/lanchonete/pedidos/999/cancelar")

    # TODO: validar status_code
    assert response.status_code == 400

    data = response.json()

    # TODO: validar mensagem de erro
    assert data['detail'] == "Pedido não encontrado ou não pode ser cancelado"

def test_nao_deve_cancelar_pedido_finalizado(client):
    # TODO: criar cliente
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})

    # TODO: criar produto
    client.post("/produtos", json={"codigo": 1, "valor": 10, "tipo": 1, "desconto_percentual": 10})

    # TODO: criar pedido
    client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 10})


    # TODO: finalizar pedido
    client.post("/lanchonete/pedidos/1/finalizar")

    response = client.post("/lanchonete/pedidos/1/cancelar")

    # TODO: validar erro
    assert response.status_code == 400

def test_deve_listar_pedidos_cancelados(client):
    # TODO: criar cliente
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})

    # TODO: criar produto
    client.post("/produtos", json={"codigo": 1, "valor": 10, "tipo": 1, "desconto_percentual": 10})

    # TODO: criar pedido
    client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 10})

    # TODO: cancelar pedido
    client.post("/lanchonete/pedidos/1/cancelar")

    response = client.get("/lanchonete/pedidos/cancelados")

    assert response.status_code == 200

    data = response.json()

    # TODO: validar se retornou uma lista
    assert isinstance(data, list)

    # TODO: validar se existe pelo menos um pedido cancelado
    assert len(data) > 0

    # TODO: validar se esta_cancelado é True
    assert data[0]["esta_cancelado"] == True