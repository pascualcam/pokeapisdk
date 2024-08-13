from dataclasses import dataclass

from .shared import Name, Version

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
