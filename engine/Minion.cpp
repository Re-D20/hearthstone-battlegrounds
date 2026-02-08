#include "Minion.h"

Minion::Minion()
    : Card("", 0, 0, "Minion", "None") {
}

Minion::Minion(const std::string& name, int attack, int health, const std::string& race)
    : Card(name, attack, health, "Minion", race) {
}

Minion::~Minion() {
}
