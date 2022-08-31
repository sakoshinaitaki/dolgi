from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    SUPER_PUNCH = 3
    HACKER_ATTACK = 4
    THOR_ABILITY = 5
    GOLEM_SHIELD = 6



class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        self.__defence = value

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def choose_defence(self, heroes):
        chosen_hero = choice(heroes)
        self.__defence = chosen_hero.super_ability

    def __str__(self):
        return f'BOSS {self.name} health: {self.health} damage: {self.damage} ' \
               f'defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        GameEntity.__init__(self, name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            self.__super_ability = None
            raise AttributeError("Wrong data type for super_ability")
        else:
            self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0:
            boss.health -= self.damage

    def apply_super_ability(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_ability(self, boss, heroes):
        coeffient = randint(2, 6)
        boss.health -= self.damage * coeffient
        print(f'Critical damage: {self.damage * coeffient}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Deku(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SUPER_PUNCH)

    def apply_super_ability(self, boss, heroes):
        a = [0.2, 0.5, 2]
        choice_a = choice(a)
        boss.health -= self.damage + self.damage * choice_a
        if choice_a == a[0]:
            self.health -= self.damage * 0.2
        elif choice_a == a[1]:
            self.health -= self.damage * 0.5
        elif choice_a == a[-1]:
            self.health -= self.damage * 2
        print(f'super punch: {self.damage + self.damage * choice_a}')









class Hacker(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.HACKER_ATTACK)


    def apply_super_ability(self, boss, heroes):
        hundred = [i for i in range(1, 101)]
        evens = list(filter(lambda x: x % 2 == 0, hundred))

        if round_counter == evens:
            pass
        else:
            choice_hacker = choice(heroes)
            boss.health -= 20
            choice_hacker.health += 20


class Thor(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.THOR_ABILITY)

    def apply_super_ability(self, boss, heroes):
        ra = randint(1, 5)
        if ra == 3:
            for i in heroes:
                i.health += 50
            print(f'{Thor.name} оглушает Босса и Босс пропускает раунд')

class Golem(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.GOLEM_SHIELD)

    def apply_super_ability(self, boss, heroes):
        for i in heroes:
            if i != self:
                i.health += boss.damage * 0.2
            self.health -= boss.damage * 0.2 * len(heroes)-1

round_counter = 0


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0:
            hero.hit(boss)
            hero.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


def start():
    boss = Boss("Alex", 1000, 50)
    warrior = Warrior("Ahiles", 280, 10)
    doc = Medic("Aibolit", 250, 5, 20)
    deku = Deku("Kiyoma", 300, 15)
    hacker = Hacker("Rob", 190, 45)
    assistant = Medic("Watson", 290, 10, 5)
    thor = Thor('Odin', 300, 15)
    golem = Golem('Tiny', 550, 5)
    heroes_list = [warrior, doc, deku, hacker, assistant, thor, golem]

    print_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


def print_statistics(boss, heroes):
    print(f'ROUND {round_counter} ------------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead


start()