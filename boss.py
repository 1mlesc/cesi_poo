import random
from enemy import Enemy

class Boss(Enemy):
    def perform_turn(self, heros):
        if not self.is_alive():
            return
        for i in range(2):
            print(f"{self.name} prépare son action n°{i+1}!")
            super().perform_turn(heros)
    def __init__(self, name, damage, type, _health=150, nb_sorts=3):
        super().__init__(name, damage, type, _health, nb_sorts)
        self.attack = {
            "Coup de griffe": ['attack', random.randint(12, 20)],
            "Coup de queue": ['attack', random.randint(10, 18)],
            "Cri terrifiant": ['debuff', random.randint(5, 10)],
        }
        self.sorts = {
            "Souffle de feu": ['attack', random.randint(20, 30)],
        }
    def show_status(self):
        return super().show_status()
        