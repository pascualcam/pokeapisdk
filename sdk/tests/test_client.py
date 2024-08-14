import unittest
import requests
from unittest.mock import patch, MagicMock
from sdk.client import PokeAPIClient
from sdk.models.pokemon import Pokemon
from sdk.models.generation import Generation


class TestPokeAPIClient(unittest.TestCase):

    @patch('sdk.client.requests.get')
    def test_get_pokemon(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": 1,
            "name": "bulbasaur",
            "base_experience": 64,
            "species": {
                "name": "bulbasaur",
                "url": "https://pokeapi.co/api/v2/pokemon-species/1/",
            }
        }
        mock_get.return_value = mock_response
        
        client = PokeAPIClient()
        pokemon = client.get_pokemon(1)
        self.assertIsInstance(pokemon, Pokemon)
        self.assertEqual(pokemon.id, 1)
        self.assertEqual(pokemon.name, "bulbasaur")
        self.assertEqual(pokemon.base_experience, 64)
    
    @patch('sdk.client.requests.get')
    def test_get_generation(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": 1,
            "name": "generation-i",
            "main_region": {
                "name": "kanto",
                "url": "https://pokeapi.co/api/v2/region/1/",
            },
            "pokemon_species": [],
        }
        mock_get.return_value = mock_response
        
        client = PokeAPIClient()
        generation = client.get_generation(1)
        self.assertIsInstance(generation, Generation)
        self.assertEqual(generation.id, 1)
        self.assertEqual(generation.name, "generation-i")
        self.assertEqual(generation.main_region.name, "kanto")

    @patch('sdk.client.requests.get')
    def test_get_species_by_generation(self, mock_get):
        mock_get.side_effect = [
            # Mock response for get_generation
            MagicMock(
                json=MagicMock(
                    return_value={
                        "id": 1,
                        "name": "generation-i",
                        "main_region": {
                            "name": "kanto",
                            "url": "https://pokeapi.co/api/v2/region/1/",
                        },
                        "pokemon_species": [
                            {
                                "name": "bulbasaur",
                                "url": "https://pokeapi.co/api/v2/pokemon/1/",
                            },
                        ],
                    }
                )
            ),
            # Mock response for get_species_by_generation
            MagicMock(
                json=MagicMock(
                    return_value={
                        "results": [
                            {"name": "bulbasaur"},
                        ]
                    }
                )
            ),
        ]
        
        client = PokeAPIClient()
        species = client.get_species_by_generation(1)
        self.assertIsInstance(species, list)
        self.assertEqual(len(species), 1)
        self.assertEqual(species[0], "bulbasaur")
    
    @patch('sdk.client.requests.get')
    def test_get_pokemon_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Not Found")
        mock_get.return_value = mock_response
        
        client = PokeAPIClient()
        with self.assertRaises(requests.exceptions.HTTPError):
            client.get_pokemon(1400)


if __name__ == '__main__':
    unittest.main()
