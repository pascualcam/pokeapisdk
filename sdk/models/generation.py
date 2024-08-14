from dataclasses import dataclass
from typing import List
from .pokemon import NamedAPIResource, PokemonSpecies


@dataclass
class Generation:
    id: int
    name: str
    abilities: List[NamedAPIResource] = None
    names: List[dict] = None
    main_region: NamedAPIResource = None
    moves: List[NamedAPIResource] = None
    pokemon_species: List[NamedAPIResource] = None
    types: List[NamedAPIResource] = None
    version_groups: List[NamedAPIResource] = None
