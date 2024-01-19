FIGHTER = {"health": 5, "attack": 3, "dodge": 2}
THIEF = {"health": 3, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}


TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}


class Character:
    _health = 0
    _attack = 0
    _dodge = 0

    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()

    def _assign_attributes(self):
        type_dict = TYPES[self._char_type]
        self._health = type_dict["health"]
        self._attack = type_dict["attack"]
        self._dodge = type_dict["dodge"]


def main():
    fighter_character = Character("fighter")
    print(fighter_character._char_type)


if __name__ == "__main__":
    main()