from hero import Hero
import random

class Cleric(Hero):
  def __init__(self, name, damage, type, _health=100, nb_sorts=5):
    super().__init__(name, damage, type, _health, nb_sorts)
    self.sorts = {
      "Soigner": ['heal', random.randint(12, 23)],
      "Boule de feu": ['attack', random.randint(15, 25)],
    }
    self.attack = {
      "Coup de masse": ['attack', random.randint(10, 18)],
    }
    