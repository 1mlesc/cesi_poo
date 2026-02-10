from enemy import Enemy
import random

class Goblin(Enemy):
  def __init__(self, name, damage, type, _health=100, nb_sorts=2):
    super().__init__(name, damage, type, _health, nb_sorts)
    self.sorts = {
      "Poison": ['attack', random.randint(10, 20)],
    }
    self.attack = {
      "Coup de griffe": ['attack', random.randint(8, 15)],
    }
  
