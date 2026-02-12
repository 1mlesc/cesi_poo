from abc import ABC
import random
from character import Character

class Enemy(Character, ABC):
    #Fonction faire un tour pour l'ennemi
    def perform_turn(self, all_characters):
      if not self.is_alive():
        return
      #Choisir une cible parmi les héros vivants
      heros = [c for c in all_characters if isinstance(c, Enemy) == False and c.is_alive()]
      if heros:
        cible = random.choice(heros)
        #Choisir aléatoirement entre attaquer ou utiliser un sort (si disponible)
        if hasattr(self, 'spells') and self.mana > 0 and random.random() < 0.5:
          sort_choice = random.choice(list([spell.name for spell in self.spells]))
          sort_choice = next(spell for spell in self.spells if spell.name == sort_choice)
          self.spell(cible, sort_choice)
        else:
          (attack_type, attack_damage) = random.choice(list(self.attack.items()))
          self.do_attack(cible, attack_type, attack_damage)

    #Initialisation de l'ennemi avec les attributs de base
    def __init__(self, name, damage, type, _health=100 , mana= 2):
      super().__init__(name, _health)
      self.damage = damage
      self.type = type
      self.mana = mana
    
    #Ajouter un observateur
    def add_observer(self, observer):
      super().add_observer(observer)

    #Enlever un observateur
    def remove_observer(self, observer):
      super().remove_observer(observer)