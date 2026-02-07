from common.schema import validate_state
from server.validators import validate_intent
from server.transitions import apply_intent


def process_intent(state, intent: dict):
    """
    Input:
      - state: GameState
      - intent: dict (from client)

    Output:
      - new GameState
    """

    intent_type = validate_intent(intent, state)
    new_state = apply_intent(state, intent_type, intent)

    # Ensure we never emit invalid state
    validate_state(new_state.to_dict())

    return new_state
