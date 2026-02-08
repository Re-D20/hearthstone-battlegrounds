#include "Card.h"
#include <algorithm>

Card::Card()
    : name(""), attack(0), health(0), cardType(""), race("") {
}

Card::Card(const std::string& name, int attack, int health,
           const std::string& cardType, const std::string& race)
    : name(name), attack(attack), health(health), cardType(cardType), race(race) {
}

Card::~Card() {
}

std::string Card::getName() const {
    return name;
}

int Card::getAttack() const {
    return attack;
}

int Card::getHealth() const {
    return health;
}

std::string Card::getCardType() const {
    return cardType;
}

std::string Card::getRace() const {
    return race;
}

void Card::setName(const std::string& newName) {
    name = newName;
}

void Card::setAttack(int newAttack) {
    attack = newAttack;
}

void Card::setHealth(int newHealth) {
    health = newHealth;
}

void Card::setRace(const std::string& newRace) {
    race = newRace;
}

void Card::takeDamage(int amount) {
    if (amount < 0) return;
    health = std::max(0, health - amount);
}

void Card::heal(int amount) {
    if (amount < 0) return;
    health += amount;
}

void Card::buff(int attackDelta, int healthDelta) {
    attack += attackDelta;
    if (attack < 0) attack = 0;
    health += healthDelta;
    if (health < 0) health = 0;
}
