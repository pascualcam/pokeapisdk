from dataclasses import dataclass

from .pokemon import Pokemon
from .shared import Description, Effect, EvolutionChain, MachineVersionDetail, Name, VerboseEffect, Version, VersionGroupFlavorText
from .generation import GenerationGameIndex

@dataclass
class Item:
    id: int
    name: str
    cost: int
    fling_power: int
    fling_effect: 'ItemFlingEffect'
    attributes: list['ItemAttribute']
    category: 'ItemCategory'
    effect_entries: list[VerboseEffect]
    flavor_text_entries: list[VersionGroupFlavorText]
    game_indices: list[GenerationGameIndex]
    names: list[Name]
    sprites: "ItemSprites"
    held_by_pokemon: list['ItemHolderPokemon']
    baby_trigger_for: EvolutionChain
    machines: list[MachineVersionDetail]


@dataclass
class ItemAttribute:
    id: int
    name: str
    items: list[Item]
    names: list[Name]
    descriptions: list[Description]


@dataclass
class ItemHolderPokemon:
    pokemon: Pokemon
    version_details: "ItemHolderPokemonVersionDetail"


@dataclass
class ItemHolderPokemonVersionDetail:
    rarity: int
    version: Version

@dataclass
class ItemSprites:
    default: str


@dataclass
class ItemCategory:
    id: int
    name: str
    items: list[Item]
    names: list[Name]
    pocket: "ItemPocket"


@dataclass
class ItemPocket:
    id: int
    name: str
    categories: list[ItemCategory]
    names: list[Name]


@dataclass
class ItemFlingEffect:
    id: int
    name: str
    effect_entries: list["Effect"]
    items: list[Item]


@dataclass
class ItemFlavorText:
    text: str
