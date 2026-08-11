import pytest
import requests

BASE_URL = "http://localhost:5000/api/chamados"

@pytest.fixture
def novo_chamado():
    return {
        "titulo": "Chamado Teste",
        "descricao": "Criado via pytest",
        "categoria": "TI",
        "prioridade": "Alta",
        "status": "Aberto",
        "solicitante": "Daniel"
    }

def test_criar_chamado(novo_chamado):
    resp = requests.post(BASE_URL, json=novo_chamado)
    assert resp.status_code == 201
    data = resp.json()
    assert "chamado" in data
    assert "id" in data["chamado"]
    chamado_id = data["chamado"]["id"]
    return chamado_id

def test_listar_chamados():
    resp = requests.get(BASE_URL)
    assert resp.status_code == 200
    assert isinstance(resp.json(), list) or "chamados" in resp.json()

def test_buscar_chamado(novo_chamado):
    # cria primeiro
    resp = requests.post(BASE_URL, json=novo_chamado)
    chamado_id = resp.json()["chamado"]["id"]

    # busca
    resp_get = requests.get(f"{BASE_URL}/{chamado_id}")
    assert resp_get.status_code == 200
    data = resp_get.json()
    assert "id" in data
    assert data["titulo"] == "Chamado Teste"


def test_atualizar_chamado(novo_chamado):
    resp = requests.post(BASE_URL, json=novo_chamado)
    chamado_id = resp.json()["chamado"]["id"]

    update = {"status": "Resolvido"}
    resp_put = requests.put(f"{BASE_URL}/{chamado_id}", json=update)
    assert resp_put.status_code == 200
    data = resp_put.json()
    assert "chamado" in data
    assert data["chamado"]["status"] == "Resolvido"

def test_excluir_chamado(novo_chamado):
    resp = requests.post(BASE_URL, json=novo_chamado)
    chamado_id = resp.json()["chamado"]["id"]

    resp_delete = requests.delete(f"{BASE_URL}/{chamado_id}")
    assert resp_delete.status_code == 200
    data = resp_delete.json()
    assert "message" in data
    assert data["message"] == "Chamado excluído com sucesso"

    # confirma exclusão
    resp_get = requests.get(f"{BASE_URL}/{chamado_id}")
    assert resp_get.status_code == 404
