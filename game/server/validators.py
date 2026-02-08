# game/server/validators.py

from game.server.intents import IntentType
from game.common.enums import Phase
from game.server.state import ServerState


class InvalidIntent(Exception):
    pass


def validate_intent(intent: dict, state: ServerState) -> IntentType:
    if "type" not in intent:
        raise InvalidIntent("Intent missing 'type'")

    try:
        intent_type = IntentType(intent["type"])
    except ValueError:
        raise InvalidIntent(f"Unknown intent type: {intent['type']}")

    # Only allow END_TURN during COMBAT
    if state.phase == Phase.COMBAT and intent_type != IntentType.END_TURN:
        raise InvalidIntent("Only END_TURN allowed during COMBAT")

    return intent_type

