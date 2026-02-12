from enemy import Enemy
import random

class Goblin(Enemy):
  def __init__(self, name, damage, type, _health=100, mana=3):
    super().__init__(name, damage, type, _health, mana)
    self.sorts = {
      "Poison": ['attack', random.randint(10, 20), 2],
    }
    self.attack = {
      "Coup de griffe": ['attack', random.randint(8, 15)],
    }
  
