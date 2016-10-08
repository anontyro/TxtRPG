from actors import Wizard, Creature, Dragon
import random
import time

def main():
    header()
    game_loop()

def header():
    print('-------------------------')
    print('    D&D for Wizards')
    print('-------------------------')
    
def game_loop():

    creatures = [
        Dragon('Golden Dragon', 14, True),
        Creature('Hobbit', 1),
        Creature('Bat', 15),
        Creature('Evil Wizard', 100),
    
    ]

    hero = Wizard('James', 9)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appears'.format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]un, or [c]heck? ')
        if cmd =='a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                time.sleep(5)
                print('Zzzzz you some how rest and recover from your injuries')
        elif cmd =='r':
            print('run forest run')
        elif cmd == 'c':
            print('you look blindly around')
            for c in creatures:
                print(' A {} of level {}'.format(c.name, c.level))
        else:
            break



if(__name__ =='__main__'):
    main()