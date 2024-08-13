from dataclasses import dataclass

from sdk.models.item import Item
from sdk.models.pokemon import PokemonSpecies
from sdk.models.shared import Location, Move, Name, Type


@dataclass
class EggGroup:
    id: int
    name: str
    names: list[Name]
    pokemon_species: list[PokemonSpecies]


@dataclass
class EvolutionChain:
    id: int
    baby_trigger_item: Item
    chain: "ChainLink"


@dataclass
class ChainLink:
    is_baby: bool
    species: PokemonSpecies
    evolution_details: list['EvolutionDetail']
    evolves_to: list['ChainLink']


@dataclass
class EvolutionDetail:
    item: Item
    trigger: 'EvolutionTrigger'
    gender: int
    held_item: Item
    knwon_move: Move
    knwon_move_type: Type
    location: Location
    min_level: int
    min_happiness: int
    min_beauty: int
    min_affection: int
    needs_overworld_rain: bool
    party_species: PokemonSpecies
    party_type: Type
    relative_physical_stats: int
    time_of_day: str
    trade_species: PokemonSpecies
    turn_upside_down: bool


@dataclass
class EvolutionTrigger:
    id: int
    name: str
    names: list[Name]
    pokemon_species: list[PokemonSpecies]
