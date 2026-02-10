import random
from character import Character

class Enemy(Character):
    #Fonction faire un tour pour l'ennemi
    def perform_turn(self, heros):
      if not self.is_alive():
        return
      #Choisir une cible parmi les héros vivants
      vivants = [h for h in heros if h.is_alive()]
      if vivants:
        cible = random.choice(vivants)
        #Choisir aléatoirement entre attaquer ou utiliser un sort (si disponible)
        if hasattr(self, 'sorts') and self.nb_sorts > 0 and random.random() < 0.5:
          sort_choice = random.choice(list(self.sorts.keys()))
          self.spell(cible, sort_choice, self.sorts[sort_choice][1], self.sorts[sort_choice])
        else:
          attack_name, (attack_type, attack_damage) = random.choice(list(self.attack.items()))
          self.do_attack(cible, attack_name, attack_damage, attack_type)
    #Initialisation de l'ennemi avec les attributs de base
    def __init__(self, name, damage, type, _health=100 , nb_sorts= 2):
      super().__init__(name, _health)
      self.damage = damage
      self.type = type
      self.nb_sorts = nb_sorts