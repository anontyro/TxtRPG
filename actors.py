import random

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def attack(self, creature):
        print('The Wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        my_roll = random.randint(1,12) * self.level
        creature_roll = random.randint(1,12) * creature.level

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature.name, creature_roll))

        if(my_roll >= creature_roll):
            print('You bashed in the head of {}'.format(creature.name))
            return True
        else:
            print('The {} ravaged your body, all that is left is a dismembered corpse'.format(creature.name))

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Creature {} of level {}'.format(self.name, self.level)


class Dragon(Creature):

    def __init__(self, name, level, flying):
        super().__init__(name,level)
        if(flying == True):
            self.flying = True
        else:
            self.flying = False


    