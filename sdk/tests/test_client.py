import unittest
from unittest.mock import patch, MagicMock
from sdk.client import PokeAPIClient
from sdk.models.pokemon import Pokemon
from sdk.models.generation import Generation


class TestPokeAPIClient(unittest.TestCase):

    @patch('client.requests.get')
    def test_get_pokemon(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": 1,
            "name": "bulbasaur",
            "base_experience": 64,
            "height": 7,
            "is_default": True,
            "order": 1,
            "weight": 69,
            "abilities": [],
            "forms": [],
            "game_indices": [],
            "held_items": [],
            "location_area_encounters": "",
            "moves": [],
            "past_types": [],
            "sprites": {},
            "cries": {},
            "species": {},
            "stats": [],
            "types": []
        }
        mock_get.return_value = mock_response
        
        client = PokeAPIClient()
        pokemon = client.get_pokemon(1)
        self.assertIsInstance(pokemon, Pokemon)
        self.assertEqual(pokemon.id, 1)
        self.assertEqual(pokemon.name, "bulbasaur")
        self.assertEqual(pokemon.height, 7)
        self.assertEqual(pokemon.weight, 69)
        self.assertEqual(pokemon.base_experience, 64)
    
    @patch('client.requests.get')
    def test_get_generation(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": 1,
            "name": "generation-i",
            "abilities": [],
            "names": [],
            "main_region": {},
            "moves": [],
            "pokemon_species": [],
            "types": [],
            "version_groups": []
        }
        mock_get.return_value = mock_response
        
        client = PokeAPIClient()
        generation = client.get_generation(1)
        self.assertIsInstance(generation, Generation)
        self.assertEqual(generation.id, 1)
        self.assertEqual(generation.name, "generation-i")
    
    @patch('client.requests.get')
    def test_get_pokemon_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        client = PokeAPIClient()
        with self.assertRaises(Exception):
            client.get_pokemon(99999)


if __name__ == '__main__':
    unittest.main()
