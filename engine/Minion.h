#pragma once
#include "Card.h"

class Minion : public Card {
public:
    Minion();
    Minion(const std::string& name, int attack, int health, const std::string& race);

    ~Minion();

};
