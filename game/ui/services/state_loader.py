# game/ui/services/state_loader.py

import json
from game.common.models import GameState, PlayerState, MinionState
from game.common.enums import Phase

def load_state_from_file(path: str) -> GameState:
    with open(path, "r") as f:
        raw = json.load(f)
    return load_state_from_dict(raw)

def load_state_from_dict(raw: dict) -> GameState:
    # If "phase" is missing, default to RECRUIT (for safety)
    phase_str = raw.get("phase", "RECRUIT")
    phase = Phase(phase_str)

    players = []
    for p in raw["players"]:
        board = [
            MinionState(
                id=m.get("card_id", m.get("id", "unknown")),
                attack=m.get("attack", 0),
                health=m.get("health", 1),
            )
            for m in p.get("board", [])
        ]
        players.append(
            PlayerState(
                id=p.get("player_id", p.get("id", "unknown")),
                health=p.get("health", 30),
                board=board,
            )
        )

    return GameState(phase=phase, players=players)
