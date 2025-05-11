import requests

def getToken():
    url = "https://appsaccess.automy.com.br/login"
    body = {
        "username": "fldoaogopdege",
        "password": "ygalepsm"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()['token']