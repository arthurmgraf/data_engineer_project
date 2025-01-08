import os
import base64
import requests

def spotify_api_block():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    # Autenticação com Spotify API
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {'Authorization': f'Basic {auth_header}'}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(auth_url, headers=headers, data=data)
    
    if response.status_code != 200:
        raise Exception(f"Erro na autenticação: {response.text}")
    
    token = response.json().get('access_token')
    
    # Obter recomendações
    api_url = 'https://api.spotify.com/v1/recommendations'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'seed_genres': 'j-rock', 'market': 'BR', 'min_popularity': 50, 'limit': 10}
    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Erro ao obter dados: {response.text}")
    
    return response.json()
