#pragma once
#include <string>

class Card {
protected:
    std::string name;
    int attack;
    int health;
    std::string cardType;  
    std::string race;      

public:
    Card();
    Card(const std::string& name, int attack, int health,
         const std::string& cardType, const std::string& race);

    virtual ~Card();

    std::string getName() const;
    int getAttack() const;
    int getHealth() const;
    std::string getCardType() const;
    std::string getRace() const;

    void setName(const std::string& newName);
    void setAttack(int newAttack);
    void setHealth(int newHealth);
    void setRace(const std::string& newRace);

    virtual void takeDamage(int amount);

    virtual void heal(int amount);

    virtual void buff(int attackDelta, int healthDelta);
};
