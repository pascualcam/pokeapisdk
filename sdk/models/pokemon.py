from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class NamedAPIResource:
    name: str
    url: str


@dataclass
class PokemonSpecies:
    name: str
    url: str
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
    base_experience: Optional[int] = None
    species: Optional[PokemonSpecies] = None
    height: Optional[int] = None
    is_default: Optional[bool] = None
    order: Optional[int] = None
    weight: Optional[int] = None
    abilities: Optional[List[NamedAPIResource]] = field(default_factory=list)
    past_abilities: Optional[list] = field(default_factory=list)
    forms: Optional[list] = field(default_factory=list)
    game_indices: Optional[list] = field(default_factory=list)
    held_items: Optional[list] = field(default_factory=list)
    location_area_encounters: Optional[list] = field(default_factory=list)
    moves: Optional[list] = field(default_factory=list)
    past_types: Optional[list] = field(default_factory=list)
    sprites: Optional[list] = field(default_factory=list)
    cries: Optional[list] = field(default_factory=list)
    stats: Optional[list] = field(default_factory=list)
    types: Optional[list] = field(default_factory=list)
