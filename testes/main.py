import base64
import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

print(f"SPOTIFY_CLIENT_ID: {os.getenv('SPOTIFY_CLIENT_ID')}")
print(f"SPOTIFY_CLIENT_SECRET: {os.getenv('SPOTIFY_CLIENT_SECRET')}")

class SpotifyAPI:
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    def __auth(self) -> str:
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_header = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        headers = {'Authorization': f'Basic {auth_header}'}
        data = {'grant_type': 'client_credentials'}
        response = requests.post(auth_url, headers=headers, data=data)

        print(f"Resposta da autenticação: {response.json()}")

        response_data = response.json()
        if 'access_token' not in response_data:
            raise Exception(f"Erro na autenticação: {response_data.get('error', 'Resposta inesperada da API')}")
        return response_data['access_token']

    def get_top_songs_recommendation(self, genre: str) -> dict:
        assert genre in ['anime', 'j-rock', 'pop', 'k-pop']
        token = self.__auth()
        api_url = 'https://api.spotify.com/v1/recommendations'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'seed_genres': genre, 'market': 'BR', 'min_popularity': 40, 'limit': 100}

        # Adicionar debug para URL e parâmetros
        print(f"URL da requisição: {api_url}")
        print(f"Parâmetros enviados: {params}")

        response = requests.get(api_url, headers=headers, params=params)

        print(f"Resposta da API de recomendações (raw): {response.text}")
        print(f"Status code da API de recomendações: {response.status_code}")

        try:
            return response.json()
        except ValueError as e:
            raise Exception(f"Erro ao interpretar a resposta como JSON: {e}, Resposta: {response.text}")

def get_top_songs_recommendation(self, genre: str) -> dict:
    assert genre in ['anime', 'j-rock', 'j-pop', 'k-pop', 'pop', 'rock']  # Atualize a lista
    token = self.__auth()
    api_url = 'https://api.spotify.com/v1/recommendations'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'seed_genres': genre, 'market': 'BR', 'min_popularity': 40, 'limit': 100}

    print(f"URL da requisição: {api_url}")
    print(f"Parâmetros enviados: {params}")

    response = requests.get(api_url, headers=headers, params=params)

    print(f"Resposta da API de recomendações (raw): {response.text}")
    print(f"Status code da API de recomendações: {response.status_code}")

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError as e:
            raise Exception(f"Erro ao interpretar a resposta como JSON: {e}, Resposta: {response.text}")
    else:
        raise Exception(f"Erro na API: Status {response.status_code}, Resposta: {response.text}")


# Executa o script principal
if __name__ == "__main__":
    spotify_api = SpotifyAPI()

    try:
        genre = 'pop'  # Escolha um gênero para teste
        print(f"Obtendo recomendações para o gênero: {genre}")
        recommendations = spotify_api.get_top_songs_recommendation(genre=genre)
        print(recommendations)
    except Exception as e:
        print(f"Erro: {e}")
