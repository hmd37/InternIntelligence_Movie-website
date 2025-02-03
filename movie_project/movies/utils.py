import requests
from django.conf import settings

def fetch_movies_from_tmdb(query):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'query': query,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {'error': 'Failed to fetch data from TMDB'}
