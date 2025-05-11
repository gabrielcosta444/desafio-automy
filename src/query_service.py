import requests

def buscarBaterias(token, email):
    url = "https://appsaccess.automy.com.br/api/api/desafio/custom/do/query"
    query = f"SELECT * FROM desafio.cadastro_baterias_desafio WHERE email = '{email}'"

    body = {
        "query": query.strip(),
        "db": "desafio"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()
