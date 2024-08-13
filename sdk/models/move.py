from dataclasses import dataclass
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .generation import Generation
    from .pokemon import Pokemon
    from .shared import (
        AbilityEffectChange, 
        ContestCombosSets, 
        ContestType, 
        Description, 
        Effect, 
        FlavorText, Language, 
        MachineVersionDetail,  
        MoveDamageClass, 
        Name, 
        Type, 
        VerboseEffect, 
        VersionGroup,
        Stat
    )

@dataclass
class Move:
    id: int
    name: str
    accuracy: int
    effect_chance: int
    pp: int
    priority: int
    power: int
    contest_combos: 'ContestCombosSets'
    contest_type: 'ContestType'
    contest_effect: 'ContestEffect'
    damage_class: 'MoveDamageClass'
    effect_entries: list['VerboseEffect']
    effect_changes: list['AbilityEffectChange']
    learned_by_pokemon: list['Pokemon']
    flavor_text_entries: list['MoveFlavorText']
    generation: 'Generation'
    machines: list['MachineVersionDetail']
    meta: 'MoveMetaData'
    names: list['Name']
    past_values: list["PastMoveStatValues"]
    stat_changes: list["MoveStatChange"]
    super_contest_effect: "SuperContestEffect"
    target: "MoveTarget"
    type: 'Type'


@dataclass
class PastMoveStatValues:
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: list['VerboseEffect']
    type: 'Type'
    version_group: 'VersionGroup'


@dataclass
class SuperContestEffect:
    id: int
    appeal: int
    flavor_text_entries: list['FlavorText']
    moves: list['Move']


@dataclass
class MoveTarget:
    id: int
    name: str
    descriptions: list['Description']
    moves: list['Move']
    names: list['Name']


@dataclass
class ContestEffect:
    id: int
    appeal: int
    jam: int
    effect_entries: list['Effect']
    flavor_text_entries: list['FlavorText']


@dataclass
class MoveFlavorText:
    flavor_text: str
    language: 'Language'
    version_group: 'VersionGroup'


@dataclass
class MoveMetaData:
    ailment: 'MoveAilment'
    category: 'MoveCategory'
    min_hits: int
    max_hits: int
    min_turns: int
    max_turns: int
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


@dataclass
class MoveCategory:
    id: int
    name: str
    moves: list['Move']
    descriptions: list['Description']


@dataclass
class MoveAilment:
    id: int
    name: str
    moves: list['Move']
    names: list['Name']


@dataclass
class MoveStatChange:
    change: int
    stat: 'Stat'


@dataclass
class MoveStatAffectSets:
    increase: list['MoveStatAffect']
    decrease: list['MoveStatAffect']


@dataclass
class MoveBattleStylePreference:
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: 'MoveBattleStyle'


@dataclass
class MoveBattleStyle:
    id: int
    name: str
    names: list['Name']


@dataclass
class MoveStatAffect:
    change: int
    move: 'Move'
