from dataclasses import dataclass
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .pokemon import Ability, Region, Move, PokemonSpecies, Type, VersionGroup
    from .shared import Name


@dataclass
class Generation:
    id: int
    name: str
    abilities: list['Ability']
    names: list['Name']
    main_region: 'Region'
    moves: list['Move']
    pokemon_species: list['PokemonSpecies']
    types: list['Type']
    version_groups: list['VersionGroup']


@dataclass
class GenerationGameIndex:
    game_index: int
    generation: Generation
