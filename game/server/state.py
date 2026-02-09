# game/server/state.py

from dataclasses import dataclass, field
from typing import List, Dict
from game.common.enums import Phase


@dataclass
class Minion:
    id: str
    attack: int
    health: int


@dataclass
class Player:
    player_id: str
    health: int
    board: List[Minion] = field(default_factory=list)
    shop: List[dict] = field(default_factory=list)


@dataclass
class ServerState:
    phase: Phase
    players: List[Player]

    @staticmethod
    def initial():
        p1 = Player(
            player_id="p1",
            health=40,
            board=[],
            shop=[
                {"card_id": "BG_FRONT_001"},
                {"card_id": "BG_FRONT_006"},
                {"card_id": "BG_FRONT_009"}
            ]
        )
        p2 = Player(player_id="p2", health=35, board=[], shop=[])
        return ServerState(phase=Phase.RECRUIT, players=[p1, p2])


    def to_payload(self) -> Dict:
        # Convert to JSON-friendly dict for the client
        return {
            "phase": self.phase.value,
            "players": [
                {
                    "player_id": p.player_id,
                    "health": p.health,
                    "board": [
                        {
                            "card_id": m.id,
                            "attack": m.attack,
                            "health": m.health,
                        }
                        for m in p.board
                    ],
                    "shop": p.shop
                }
                for p in self.players
            ],
        }
