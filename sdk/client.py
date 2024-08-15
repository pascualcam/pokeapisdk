import requests
from typing import List
from sdk.models.pokemon import Pokemon, PokemonSpecies, NamedAPIResource
from sdk.models.generation import Generation


class PokeAPIClient:
    def __init__(self, base_url="https://pokeapi.co/api/v2/"):
        self.base_url = base_url

    def get_paginated(self, url: str, limit: int = None, offset: int = 0):
        results = []
        while url:
            if limit is not None:
                url_params = f"{url}?limit={limit}&offset={offset}"
            else:
                url_params = url
                
            response = self._get(url_params)
            results.extend(response.get("results", []))
            
            if limit is not None:
                offset += len(response.get("results", []))
                
            url = response.get("next")
            if url:
                url = url.replace(self.base_url, "")
        return results
    
    def get_pokemon(self, identifier: str | int) -> Pokemon:
        """Get a pokemon by name or id"""
        response = self._get(f"pokemon/{identifier}")
        return Pokemon(
            id=response["id"],
            name=response["name"],
            base_experience=response["base_experience"],
            species=PokemonSpecies(
                name=response["species"]["name"],
                url=response["species"]["url"],
            ),
        )

    def get_pokemons_list(self) -> List[Pokemon]:
        """Get a list of pokemons"""
        response = self.get_paginated("pokemon")
        pokemons = []
        for i, p in enumerate(response, 1):
            pokemon_data = {
                "id": i,
                "name": p["name"],
                "base_experience": None,
            }
            pokemons.append(Pokemon(**pokemon_data))
        return pokemons

    def get_generation(self, identifier: str | int) -> Generation:
        """Get a pokemon generation by name or id"""
        response = self._get(f"generation/{identifier}")
        main_region = NamedAPIResource(**response["main_region"])
        pokemon_species = [NamedAPIResource(**species) for species in response["pokemon_species"]]
        return Generation(
            id=response["id"],
            name=response["name"],
            main_region=main_region,
            pokemon_species=pokemon_species,            
        )
    
    def get_generations_list(self) -> List[Generation]:
        """Get a list of pokemon generations"""
        response = self.get_paginated("generation")
        generations = []
        for g in response:
            generation_details = self._get(g["url"])
            generations.append(Generation(**generation_details))
        return generations
    
    def get_species_by_generation(self, generation_id: str | int) -> List[str]:
        """Get a list of species introduced in the specified generation"""
        generation = self.get_generation(generation_id)
        species_names = [species.name for species in generation.pokemon_species]
        return species_names
    
    def _get(self, endpoint):
        if endpoint.startswith("http"):
            url = endpoint 
        else:
            url = f"{self.base_url}{endpoint}"

        response = requests.get(url)
        response.raise_for_status()
        return response.json()
