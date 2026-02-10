import questionary
from character import Character
from enemy import Enemy

class Hero(Character):

    #Fonction faire un tour pour le héro
    def perform_turn(self, all_characters):
      if not self.is_alive():
        return
      action = questionary.select(
        f"Que doit faire {self.name} ?",
        choices=["Attaquer", "Utiliser un sort", "Passer"] if hasattr(self, 'sorts') else ["Attaquer", "Passer"]
      ).ask()
      #Si l'action est Attaquer, demander la cible parmi les ennemis vivants
      if action == "Attaquer":
        #Liste des attaques
        attack_choice = questionary.select(
          "Quel attaque voulez-vous utiliser ?",
          choices=list(self.attack.keys())
        ).ask()
        possibles = [c for c in all_characters if c.is_alive()]
        #Demander la cible
        cible_nom = questionary.select(
          "Qui voulez-vous cibler avec l'attaque ?",
          choices=[c.name for c in possibles if isinstance(c, Enemy)]
        ).ask()
        cible = next(c for c in possibles if c.name == cible_nom)
        self.do_attack(cible, attack_choice, self.attack[attack_choice][1], self.attack[attack_choice])
      #Si l'action est Utiliser un sort, demander le sort à utiliser puis la cible parmi les personnages vivants
      elif action == "Utiliser un sort" and hasattr(self, 'sorts'):
        #Liste des sorts
        sort_choice = questionary.select(
          "Quel sort voulez-vous utiliser ?",
          choices=list(self.sorts.keys())
        ).ask()
        possibles = [character for character in all_characters if character.is_alive()]
        #Sort type heal
        if self.sorts[sort_choice][0] == 'heal':
          temp_possibles = []
          for character in possibles:
            if isinstance(character, Hero):
              temp_possibles.append(character)
          possibles = temp_possibles
        else:
        #Autre sort (attack)
          possibles = [character for character in possibles if isinstance(character, Enemy)]
        #Demander la cible
        cible_nom = questionary.select(
          "Qui voulez-vous cibler avec le sort ?",
          choices=[c.name for c in possibles]
        ).ask()
        cible = next(c for c in possibles if c.name == cible_nom)
        self.spell(cible, sort_choice, self.sorts[sort_choice][1], self.sorts[sort_choice])
      # Si "Passer", ne rien faire
      elif action == "Passer":
        print(f"{self.name} décide de passer son tour.")
    
    #Initialisation du héro avec les attributs de base
    def __init__(self, name, damage, type, _health=100, nb_sorts= 2):
      super().__init__(name, _health)
      self.damage = damage
      self.type = type
      self.nb_sorts = nb_sorts
