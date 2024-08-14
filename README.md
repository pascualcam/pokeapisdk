# PokeAPI Python SDK

Easily interact with the best [Pokemon](https://pokeapi.co/) database in the web, in Python. 

## User guide

### Installation

`pip install git+https://github.com/pascualcam/pokeapisdk/`

### Usage

```python
import pokeapisdk
from pokeapisdk.client import PokeAPIClient

poke = PokeAPIClient()

pokemons = poke.get_pokemons_list()

for pokemon in pokemons:
    print(pokemon.name)
    print(pokemon.base_experience)

```

### Testing

A test file `test_client.py` includes simple scenarios to test the SDK. Specifically, it tests:

- get_pokemon
- get_generation
- get_species_by_generation

## SDK Design

### Key aspects

- temp
- temp

### Tools

- The PokeAPI SDK relies heavily on the [Requests](https://pypi.org/project/requests/) library to handle HTTP requests, responses to the PokeAPI endpoints via JSON data, as well as providing HTTP status codes for the requests. 

- This SDK also makes extensive use of the dataclasses library to simplify the modeling of the PokeAPI class instances.
