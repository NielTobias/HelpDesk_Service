import requests

BASE_URL = "http://localhost:5000/api/chamados"

# 1. Criar um chamado (POST)
novo_chamado = {
    "titulo": "Teste API",
    "descricao": "Chamado criado via script",
    "categoria": "TI",
    "prioridade": "Alta",
    "status": "Aberto",
    "solicitante": "Daniel"
}
resp_post = requests.post(BASE_URL, json=novo_chamado)
print("POST:", resp_post.status_code, resp_post.json())

# Pegar o ID do chamado criado
chamado_id = resp_post.json().get("id")

# 2. Listar chamados (GET)
resp_get_all = requests.get(BASE_URL)
print("GET todos:", resp_get_all.status_code, resp_get_all.json())

# 3. Buscar chamado específico (GET)
resp_get_one = requests.get(f"{BASE_URL}/{chamado_id}")
print("GET um:", resp_get_one.status_code, resp_get_one.json())

# 4. Atualizar chamado (PUT)
atualizacao = {"status": "Resolvido", "tecnico": "Suporte"}
resp_put = requests.put(f"{BASE_URL}/{chamado_id}", json=atualizacao)
print("PUT:", resp_put.status_code, resp_put.json())

# 5. Excluir chamado (DELETE)
resp_delete = requests.delete(f"{BASE_URL}/{chamado_id}")
print("DELETE:", resp_delete.status_code, resp_delete.json())

# 6. Confirmar exclusão (GET novamente)
resp_get_deleted = requests.get(f"{BASE_URL}/{chamado_id}")
print("GET após DELETE:", resp_get_deleted.status_code)
