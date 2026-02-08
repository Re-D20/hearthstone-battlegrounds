from game.common.schema import validate_state
from game.server.validators import validate_intent
from game.server.transitions import apply_intent


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
