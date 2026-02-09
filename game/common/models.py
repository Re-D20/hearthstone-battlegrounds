from dataclasses import dataclass
from typing import List, Optional
from .enums import Phase

@dataclass
class MinionState:
    id: str
    attack: int
    health: int

@dataclass
class PlayerState:
    id: str
    board: List[MinionState]
    health: int

@dataclass
class GameState:
    phase: Phase
    players: List[PlayerState]

@dataclass
class PlayerState:
    id: str
    board: List[MinionState]
    health: int
    shop: list  # NEW

