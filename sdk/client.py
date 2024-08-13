import requests
from typing import Union
from models.pokemon import Pokemon
from models.generation import Generation


class PokeAPIClient:
    def __init__(self, base_url="https://pokeapi.co/api/v2/"):
        self.base_url = base_url

    def get_pokemon(self, identifier: Union[str, int]) -> Pokemon:
        '''
        Get a pokemon by name or id
        '''
        response = self._get(f"pokemon/{identifier}")
        return Pokemon(**response)

    def get_generation(self, identifier: Union[str, int]) -> Generation:
        '''
        Get a pokemon generation by name or id
        '''
        response = self._get(f"generation/{identifier}")
        return Generation(**response)
    
    def _get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
