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
        - `get_pokemon -> Pokemon`: get a single pokemon by id or name
        - `get_generation -> Generation`: get a generation by id or name
        - `get_species_by_generation -> List[str]`: get a list of all the species released for a specified generation
        - `get_pokemons_list -> List[Pokemon]`: get a list of all or `n` pokemons available
        - `get_generations_list -> List[Generation]`: get a list of all generations available

- Assumptions

    - This SDK relies on the data integrity of the PokeAPI
    - The availability of the API is assumed whenever the client is utilized
    - The data format relied upon by this SDK is JSON
    - The SDK contains basic error handling and a logger is included for debugging

- Limitations

    - No rate limiting is implemented or whatsoever
    - No data accuracy or checks are implemented - the SDK assumes all data from the source is correct
    - A simple pagination is implemented as part of this SDK but specific behavior must be added
    - This SDK is intended to be compatible with `v2` of the PokeAPI

- Pagination

    - Pagination is implemented to manage data transfer efficiently. 
    - Limit and offset are not part of the implementation
      - limit
      - offset

### Tools

- The PokeAPI SDK relies heavily on the [Requests](https://pypi.org/project/requests/) library to handle HTTP requests, responses to the PokeAPI endpoints via JSON data, as well as providing HTTP status codes for the requests. 

- This SDK also makes extensive use of the [dataclasses](https://docs.python.org/3/library/dataclasses.html) library to simplify the modeling of the PokeAPI class instances.
