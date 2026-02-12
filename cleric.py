from hero import Hero
import random
from spell import Spell

class Cleric(Hero):
  def __init__(self, name, damage, type, _health=100, mana=5):
    super().__init__(name, damage, type, _health, mana)
    #Initialisation des sorts du Cleric
    Spell_1 = Spell('Soigner', random.randint(12, 23), 'heal', 3)
    Spell_2 = Spell('Boule de feu', random.randint(15, 25), 'attack', 4)
    self.spells = [Spell_1, Spell_2]

    self.attack = {
      "Coup de masse": ['attack', random.randint(10, 18)],
    }
    