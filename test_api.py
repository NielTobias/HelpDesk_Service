import requests


url = "http://127.0.0.1:5000/api/chamados"


dados = {
    "titulo": "Teste da API REST",
    "descricao": "Chamado criado através da API.",
    "categoria": "Software",
    "prioridade": "Média",
    "solicitante": "Teste API"
}


resposta = requests.post(
    url,
    json=dados
)


print("Status:", resposta.status_code)
print("Resposta:")
print(resposta.json())