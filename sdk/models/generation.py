from dataclasses import dataclass
from .pokemon import PokemonSpecies


@dataclass
class Generation:
    id: int
    name: str
    abilities: list
    names: list
    main_region: list
    moves: list
    types: list
    version_groups: list
    pokemon_species: list[PokemonSpecies]
