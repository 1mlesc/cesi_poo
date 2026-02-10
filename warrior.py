import random
from hero import Hero

class Warrior(Hero):
  def __init__(self, name, damage, type, _health=100, nb_sorts=0):
    super().__init__(name, damage, type, _health, nb_sorts)
    self.attack = {
      "Coup puissant": ['attack', random.randint(18, 30)],
      "Frappe rapide": ['attack', random.randint(12, 22)],
      "Flèche pointue": ['distance', random.randint(10, 18)],
    }
  