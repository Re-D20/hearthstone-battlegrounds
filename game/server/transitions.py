
from copy import deepcopy
from game.common.enums import Phase
from game.server.intents import IntentType
from game.server.state import ServerState, Minion


def apply_intent(state: ServerState, intent_type: IntentType, intent_payload: dict) -> ServerState:
    new_state = deepcopy(state)

    # For simplicity, always modify player 1 (index 0)
    player = new_state.players[0]

    if new_state.phase == Phase.RECRUIT:
        if intent_type == IntentType.END_TURN:
            new_state.phase = Phase.COMBAT

        elif intent_type == IntentType.BUY:
            # Add a dummy minion
            m = Minion(id="DummyMinion", attack=3, health=2)
            player.board.append(m)

        elif intent_type == IntentType.SELL:
            if player.board:
                player.board.pop(0)

        elif intent_type == IntentType.PLAY:
            # Same as BUY for now
            m = Minion(id="PlayedMinion", attack=2, health=3)
            player.board.append(m)

    elif new_state.phase == Phase.COMBAT:
        if intent_type == IntentType.END_TURN:
            # Simple "combat": both players lose 1 HP, then back to RECRUIT
            for p in new_state.players:
                p.health -= 1
            new_state.phase = Phase.RECRUIT

    return new_state
