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

A test file `test_client.py` includes simple scenarios to test the SDK. Specifically, it tests the following endpoints:

- `get_pokemon`
- `get_generation`
- `get_species_by_generation`

## SDK Design

### Key aspects

- Design

    The design of the SDK

    - Endpoints:
        - `get_pokemon`: get a single pokemon by id or name
        - `get_generation`: get a generation by id or name
        - `get_species_by_generation`: get a list of all the species released for a specified generation
        - `get_pokemons_list`: get a list of all or `n` pokemons available
        - `get_generations_list`: get a list of all generations available

- Assumptions

    The assumptions of the SDK

- Limitations

    The limitations of the SDK

- Pagination

    Some text about pagination

### Tools

- The PokeAPI SDK relies heavily on the [Requests](https://pypi.org/project/requests/) library to handle HTTP requests, responses to the PokeAPI endpoints via JSON data, as well as providing HTTP status codes for the requests. 

- This SDK also makes extensive use of the [dataclasses](https://docs.python.org/3/library/dataclasses.html) library to simplify the modeling of the PokeAPI class instances.
