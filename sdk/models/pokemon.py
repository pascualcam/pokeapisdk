from dataclasses import dataclass
from typing import List

@dataclass
class NamedAPIResource:
    name: str
    url: str


@dataclass
class PokemonSpecies:
    name: str
    # url: str
    # id: int
    # name: str
    # order: int
    # gender_rate: int
    # capture_rate: int
    # base_happiness: int
    # is_baby: bool
    # is_legendary: bool
    # is_mythical: bool
    # hatch_counter: int
    # has_gender_differences: bool
    # forms_switchable: bool

@dataclass
class Pokemon:
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[NamedAPIResource]
    past_abilities: list
    forms: list
    game_indices: list
    held_items: list
    location_area_encounters: list
    moves: list
    past_types: list
    sprites: list
    cries: list
    stats: list
    types: list
    species: PokemonSpecies
