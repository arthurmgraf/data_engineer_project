import os
from dotenv import load_dotenv
import requests

# Carregar variáveis do arquivo .env
load_dotenv()

# Spotify Credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Função para autenticar e obter o token
def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_data = {
        "grant_type": "client_credentials"
    }
    auth_headers = {
        "Authorization": f"Basic {os.getenv('SPOTIFY_CLIENT_ID')}:{os.getenv('SPOTIFY_CLIENT_SECRET')}"
    }
    response = requests.post(auth_url, data=auth_data, headers=auth_headers)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Erro ao obter token: {response.text}")

# Teste a autenticação
if __name__ == "__main__":
    token = get_spotify_token()
    print(f"Token obtido com sucesso: {token}")
