import requests


class PokeAPIClient:
    def __init__(self, base_url="https://pokeapi.co/api/v2/"):
        self.base_url = base_url

    def _get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_pokemon(self, identifier):
        '''
        Get a pokemon by name or id
        '''
        return self._get(f"pokemon/{identifier}")
    
    def get_generation(self, identifier):
        '''
        Get a pokemon generation by name or id
        '''
        return self._get(f"generation/{identifier}")
