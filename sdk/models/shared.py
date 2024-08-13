from dataclasses import dataclass
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .item import Item
    from .move import Move, MoveBattleStylePreference, MoveStatAffectSets
    from .generation import Generation, GenerationGameIndex
    from .pokemon import (
        AbilityPokemon,
        Pokemon,
        PokemonEncounter,
        PokemonSpecies,
        Pokedex
    )

@dataclass
class NamedAPIResource:
    name: str
    url: str


@dataclass
class Language:
    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: list['Name']


@dataclass
class Name:
    name: str
    language: Language


@dataclass
class Ability:
    id: int
    name: str
    is_main_series: bool
    generation: 'Generation'
    names: list[Name]
    effect_entries: list['VerboseEffect']
    effect_changes: list['AbilityEffectChange']
    flavor_text_entries: list['AbilityFlavorText']
    pokemon: list['AbilityPokemon']


@dataclass
class VerboseEffect:
    effect: str
    short_effect: str
    language: Language


@dataclass
class AbilityEffectChange:
    effect_entries: list['Effect']
    version_group: 'VersionGroup'


@dataclass
class Effect:
    effect: str
    language: Language


@dataclass
class AbilityFlavorText:
    flavor_text: str
    languague: Language
    version_group: 'VersionGroup'


@dataclass
class Location:
    id: int
    string: str
    region: 'Region'
    names: list[Name]
    game_indices: list['GenerationGameIndex']
    areas: list['LocationArea']


@dataclass
class LocationArea:
    id: int
    name: str
    game_index: int
    encounter_method_rates: list['EncounterMethodRate']
    location: Location
    names: list[Name]
    pokemon_encounters: list['PokemonEncounter']


@dataclass
class Stat:
    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: 'MoveStatAffectSets'
    affecting_natures: 'NatureStatAffectSets'
    characteristics: list["Characteristic"]
    move_damage_class: "MoveDamageClass"
    names: list[Name]

    
@dataclass
class NatureStatAffectSets:
    increase: list['Nature']
    decrease: list['Nature']
    
@dataclass
class Nature:
    id: int
    name: str
    decreased_stat: Stat
    increased_stat: Stat
    hates_flavor: 'BerryFlavor'
    likes_flavor: 'BerryFlavor'
    pokeathlon_stat_changes: list['NatureStatChange']
    move_battle_style_preferences: list['MoveBattleStylePreference']
    names: list[Name]
    
@dataclass
class Characteristic:
    id: int
    gene_modulo: int
    possible_values: list[int]
    highest_stat: Stat
    descriptions: list['Description']
    
@dataclass
class MoveDamageClass:
    id: int
    name: str
    descriptions: list['Description']
    moves: list['Move']
    names: list[Name]
    
@dataclass
class NatureStatChange:
    max_change: int
    pokeathlon_stat: 'PokeathlonStat'

@dataclass
class PokeathlonStat:
    id: int
    name: str
    names: list[Name]
    affecting_natures: 'NaturePokeathlonStatAffectSets'

@dataclass
class NaturePokeathlonStatAffectSets:
    increase: list['NaturePokeathlonStatAffect']
    decrease: list['NaturePokeathlonStatAffect']

@dataclass
class NaturePokeathlonStatAffect:
    max_change: int
    nature: Nature


@dataclass
class FlavorText:
    flavor_text: str
    language: Language
    version: 'Version' 


@dataclass
class ContestCombosSets:
    normal: 'ContestComboDetail'
    super: 'ContestComboDetail'


@dataclass
class ContestComboDetail:
    use_before: list['Move']
    use_after: list['Move']


@dataclass
class ContestType:
    id: int
    name: str
    berry_flavor: 'BerryFlavor'
    names: list[Name]


@dataclass
class BerryFlavor:
    id: int
    name: str
    berries: list['FlavorBerryMap']
    contest_type: 'ContestType'
    names: list[Name]


@dataclass
class FlavorBerryMap:
    potency: int
    berry: 'Berry'


@dataclass
class BerryFlavorMap:
    potency: int
    flavor: 'BerryFlavor'


@dataclass
class Berry:
    id: int
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: 'BerryFirmness'
    flavors: list['BerryFlavorMap']
    item: 'Item'
    natural_gift_type: 'Type'


@dataclass
class BerryFirmness:
    id: int
    name: str
    berries: list[Berry]
    names: list[Name]
    

@dataclass
class MoveLearnMethod:
    id: int
    name: str
    descriptions: list['Description']
    names: list[Name]
    version_groups: list['VersionGroup'] 


@dataclass
class PalParkEncounterArea:
    base_score: int
    rate: int
    area: 'PalParkArea'


@dataclass
class PalParkArea:
    id: int
    name: str
    names: list[Name]
    pokemon_encounters: list['PalParkEncounterSpecies']


@dataclass
class PalParkEncounterSpecies:
    base_score: int
    rate: int
    pokemon_species: 'PokemonSpecies'

    
@dataclass
class Description:
    description: str
    language: Language


@dataclass
class Genus:
    genus: str
    language: Language

    
@dataclass
class GrowthRate:
    id: int
    name: str
    formula: str
    description: list[Description]
    levels: list['GrowthRateExperienceLevel']
    pokemon_species: list['PokemonSpecies']


@dataclass
class GrowthRateExperienceLevel:
    level: int
    experience: int


@dataclass
class Region:
    id: int
    locations: list[Location]
    name: str
    names: list[Name]
    main_generation: 'Generation'
    pokedexes: list['Pokedex']
    version_groups: list['VersionGroup']


@dataclass
class Version:
    id: int
    name: str
    names: list[Name]
    version_group: 'VersionGroup'


@dataclass
class Machine:
    id: int
    item: 'Item'
    move: 'Move'
    version_group: 'VersionGroup'


@dataclass
class MachineVersionDetail:
    machine: 'Machine'
    version_group: 'VersionGroup'


@dataclass
class VersionGroup:
    id: int
    name: str
    order: int
    generation: 'Generation'
    move_learn_methods: list['MoveLearnMethod']
    pokedexes: list['Pokedex']
    regions: list[Region]
    versions: Version


@dataclass
class VersionGroupFlavorText:
    text: str
    language: Language
    version_group: VersionGroup


@dataclass
class Type:
    id: int
    name: str
    damage_relations: 'TypeRelations'
    past_damage_relations: list['TypeRelationsPast']
    game_indices: list['GenerationGameIndex']
    generation: 'Generation'
    move_damage_class: 'MoveDamageClass'
    names: list[Name]
    pokemon: list['Pokemon']
    moves: list['Move']


@dataclass
class TypeRelations:
    no_damage_to: list['Type']
    half_damage_to: list['Type']
    double_damage_to: list['Type']
    no_damage_from: list['Type']
    half_damage_from: list['Type']
    double_damage_from: list['Type']


@dataclass
class TypeRelationsPast:
    generation: 'Generation'
    damage_relations: 'TypeRelations'


@dataclass
class EncounterMethodRate:
    encounter_method: "EncounterMethod"
    version_details: list["EncounterVersionDetails"]


@dataclass
class EncounterVersionDetails:
    rate: int
    version: Version


@dataclass
class VersionEncounterDetail:
    version: "Version"
    max_chance: int
    encounter_details: list["Encounter"]


@dataclass
class Encounter:
    min_level: int
    max_level: int
    condition_values: list["EncounterConditionValue"]
    chance: int
    method: "EncounterMethod"


@dataclass
class EncounterConditionValue:
    id: int
    name: str
    condition: "EncounterCondition"
    names: list[Name]


@dataclass
class EncounterCondition:
    id: int
    name: str
    names: list[Name]
    values: list["EncounterConditionValue"]


@dataclass
class EncounterMethod:
    id: int
    name: str
    order: int
    names: list[Name]
