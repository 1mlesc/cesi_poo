from team import Team
from warrior import Warrior
from cleric import Cleric
from goblin import Goblin
from boss import Boss
from observer import Observer

class Factory:
    @staticmethod
    def create_hero_team():
        laezel = Warrior("Laezel", 20, "Warrior", 95)
        shadowheart = Cleric("Shadowheart", 13, "Cleric", 70)
        laezel.add_observer(Observer())
        shadowheart.add_observer(Observer())
        return Team([laezel, shadowheart])

    @staticmethod
    def create_enemy_team():
        miguel_tornado = Goblin('Miguel Tornado', 20, 'Goblin', 104)
        alexis = Goblin('Alexis', 15, 'Goblin', 80)
        miguel_tornado.add_observer(Observer())
        alexis.add_observer(Observer())
        return Team([miguel_tornado, alexis])

    @staticmethod
    def create_boss():
        dominique = Boss('Dominique', 25, 'Boss', 150)
        dominique.add_observer(Observer())
        return dominique
