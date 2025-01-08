import os
from dotenv import load_dotenv
import requests
import base64

# Carregar variáveis do arquivo .env
load_dotenv()

# Agora as variáveis podem ser acessadas
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Exibir as variáveis para depuração
print(f"{SPOTIFY_CLIENT_ID}")
print(f"{SPOTIFY_CLIENT_SECRET}")
print(f"{SPOTIFY_REDIRECT_URI}")

## Spotify Credentials
#SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
#SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
#SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
#
## Função para autenticar e obter o token
#def get_spotify_token():
#    auth_url = "https://accounts.spotify.com/api/token"
#    auth_data = {
#        "grant_type": "client_credentials"
#    }
#    # Codifique as credenciais em Base64
#    client_credentials = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
#    base64_credentials = base64.b64encode(client_credentials.encode()).decode()
#    auth_headers = {
#        "Authorization": f"Basic {base64_credentials}"
#    }
#    response = requests.post(auth_url, data=auth_data, headers=auth_headers)
#    if response.status_code == 200:
#        return response.json().get("access_token")
#    else:
#        raise Exception(f"Erro ao obter token: {response.text}")

