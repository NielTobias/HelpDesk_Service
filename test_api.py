import requests


url = "http://127.0.0.1:5000/api/chamados/7"


dados = {
    "status": "Em andamento",
    "prioridade": "Alta",
    "tecnico": "Carlos"
}


resposta = requests.delete(
    url,
    json=dados
)


print("Status:", resposta.status_code)

print("Resposta:")

print(resposta.json())

