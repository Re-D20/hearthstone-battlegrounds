from copy import deepcopy
from common.enums import Phase
from server.intents import IntentType


def apply_intent(state, intent_type, intent_payload):
    new_state = deepcopy(state)

    if new_state.phase == Phase.RECRUIT:
        if intent_type == IntentType.END_TURN:
            new_state.phase = Phase.COMBAT

        elif intent_type == IntentType.BUY:
            # NOTE: server.md allows server-side mutation;
            # exact buy logic is intentionally minimal here
            pass

        elif intent_type == IntentType.SELL:
            pass

    elif new_state.phase == Phase.COMBAT:
        if intent_type == IntentType.END_TURN:
            new_state.phase = Phase.RECRUIT

    return new_state
