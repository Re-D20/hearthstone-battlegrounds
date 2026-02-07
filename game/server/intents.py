from enum import Enum


class IntentType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    PLAY = "PLAY"
    END_TURN = "END_TURN"
