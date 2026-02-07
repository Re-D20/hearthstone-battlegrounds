from common.enums import Phase
from server.intents import IntentType


class InvalidIntent(Exception):
    pass


def validate_intent(intent: dict, state):
    if "type" not in intent:
        raise InvalidIntent("Intent missing 'type'")

    try:
        intent_type = IntentType(intent["type"])
    except ValueError:
        raise InvalidIntent(f"Unknown intent type: {intent['type']}")

    # Phase-based validation (from server.md philosophy)
    if state.phase == Phase.COMBAT:
        if intent_type != IntentType.END_TURN:
            raise InvalidIntent("Only END_TURN allowed during COMBAT")

    if state.phase == Phase.RECRUIT:
        if intent_type == IntentType.BUY and "minion_id" not in intent:
            raise InvalidIntent("BUY intent requires minion_id")

    return intent_type
