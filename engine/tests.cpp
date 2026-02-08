#include "Card.h"
#include "Minion.h"
#include <cassert>

int main() {
    Card c("TestCard", 5, 10, "Card", "None");
    assert(c.getName() == "TestCard");
    assert(c.getAttack() == 5);
    assert(c.getHealth() == 10);

    c.takeDamage(3);
    assert(c.getHealth() == 7);

    c.heal(4);
    assert(c.getHealth() == 11);

    c.buff(2, -5);
    assert(c.getAttack() == 7);
    assert(c.getHealth() == 6);

    c.takeDamage(100);
    assert(c.getHealth() == 0);

    Minion m("TestMinion", 2, 3, "Beast");
    assert(m.getCardType() == "Minion");
    assert(m.getRace() == "Beast");
    assert(m.getAttack() == 2);
    assert(m.getHealth() == 3);

    m.buff(-5, 10);
    assert(m.getAttack() == 0);
    assert(m.getHealth() == 13);

    return 0;
}
