from dataclasses import dataclass
from typing import List

@dataclass
class Person:
    name: str
    birth_year: str
    gender: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    homeworld: str
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    url: str
    created: str
    edited: str

# Future dataclasses for other endpoints:
# @dataclass
# class Planet:
#     ...
# @dataclass
# class Film:
#     ...