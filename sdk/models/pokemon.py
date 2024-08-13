from dataclasses import dataclass

from sdk.models.encounter import VersionEncounterDetail
from .generation import Generation
from .shared import (
    Name,
    NamedAPIResource, 
    Ability, 
    EggGroup,
    EvolutionChain,
    PalParkEncounterArea,
    FlavorText,
    Description,
    Genus,
    GrowthRate,
    VersionGroup,
    Type
)

@dataclass
class PokemonEntry:
    entry_number: int
    pokemon_species: 'PokemonSpecies'

@dataclass
class Pokedex:
    id: int
    name: str
    is_main_series: bool
    descriptions: list[Description]
    names: list[Name]
    pokemon_entries: list[PokemonEntry]
    region: VersionGroup
    version_groups: list[VersionGroup]

@dataclass
class PokemonSpeciesDexEntry:
    entry_number: int
    pokedex: Pokedex
    
@dataclass
class PokemonFormType:
    slot: int
    type: Type
    
@dataclass
class PokemonFormSprites:
    front_default: str
    front_shiny: str
    back_default: str
    back_shiny: str 
    
@dataclass
class PokemonColor:
    id: int
    name: str
    names: list[Name]
    
@dataclass
class PokemonShape:
    id: int
    name: str
    names: list[Name]
    pokemon_species: 'PokemonSpecies'


@dataclass
class PokemonSpeciesVariety:
    is_default: bool
    pokemon: 'Pokemon'
    
@dataclass
class PokemonHabitat:
    id: int
    name: str
    names: list[Name]
    pokemon_species: list['PokemonSpecies']

@dataclass
class AbilityPokemon:
    is_hidden: bool
    slot: int
    pokemon: 'Pokemon'

@dataclass
class PokemonAbility:
    is_hidden: bool
    slot: int
    ability: 'Ability'

@dataclass
class PokemonStat:
    stat: NamedAPIResource
    effort: int
    base_stat: int
    
@dataclass
class PokemonType:
    slot: int
    type
    
@dataclass    
class PokemonForm:
    id: int
    name: str
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: NamedAPIResource
    types: PokemonFormType
    sprites: PokemonFormSprites
    version_group: NamedAPIResource
    names: list[Name]
    form_names: list[Name]
    
@dataclass
class VersionGameIndex:
    game_index: int
    version: NamedAPIResource

@dataclass
class PokemonHeldItemVersion:
    version: NamedAPIResource
    rarity: int

@dataclass
class PokemonHeldItem:
    item: NamedAPIResource
    version_details: list[PokemonHeldItemVersion]

@dataclass
class PokemonMoveVersion:
    move_learn_method: NamedAPIResource
    version_group: NamedAPIResource
    level_learned_at: int

@dataclass
class PokemonMove:
    move: NamedAPIResource
    version_group_details: list[PokemonMoveVersion]

@dataclass
class PokemonEncounter:
    pokemon: 'Pokemon'
    version_details: list[VersionEncounterDetail]


@dataclass
class PokemonSprites:
    front_default: str
    front_shiny: str
    front_female: str
    front_shiny_female: str
    back_default: str
    back_shiny: str
    back_female: str
    back_shiny_female: str
    
@dataclass
class PokemonCries:
    latest: str
    legacy: str

@dataclass
class PokemonSpecies:
    id: int
    name: str
    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    hatch_counter: int
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: GrowthRate
    pokedex_numbers: list[PokemonSpeciesDexEntry]
    egg_groups: list[EggGroup]
    color: PokemonColor
    shape: PokemonShape
    evolves_from_species: 'PokemonSpecies'
    evolution_chain: EvolutionChain
    habitat: PokemonHabitat
    generation: Generation
    names: list[Name]
    pal_park_encounters: list[PalParkEncounterArea]
    flavor_text_entries: list[FlavorText]
    form_descriptions: list[Description]
    genera: list[Genus]
    varieties: list[PokemonSpeciesVariety]    

@dataclass
class Pokemon:
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: list[PokemonAbility]
    forms: list[PokemonForm]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    location_area_encounters: str
    moves: list[PokemonMove]
    past_types: list[PokemonType]
    sprites: PokemonSprites
    cries: PokemonCries
    species: PokemonSpecies
    stats: list[PokemonStat]
    types: list[PokemonType]
