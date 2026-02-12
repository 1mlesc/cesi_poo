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
        choices=["Attaquer", "Utiliser un sort", "Passer", "Quitter"] if hasattr(self, 'spells') else ["Attaquer", "Passer", "Quitter"]
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
        print(f"Attaque choisie : {self.attack[attack_choice][0]}")
        self.do_attack(cible, self.attack[attack_choice][0], self.attack[attack_choice][1])
      #Si l'action est Utiliser un sort, demander le sort à utiliser puis la cible parmi les personnages vivants
      elif action == "Utiliser un sort" and hasattr(self, 'spells'):
        #Liste des sorts
        sort_choice = questionary.select(
          "Quel sort voulez-vous utiliser ?",
          choices=[spell.name for spell in self.spells]
        ).ask()
        sort_choice = next(spell for spell in self.spells if spell.name == sort_choice)
        possibles = [character for character in all_characters if character.is_alive()]
        #Sort type heal
        if sort_choice.type == 'heal':
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
        self.spell(cible, sort_choice)
      # Si "Passer", ne rien faire
      elif action == "Passer":
        self.notify('skip')
      elif action == "Quitter":
        print("Merci d'avoir joué ! À bientôt !")
        exit()
    #Initialisation du héro avec les attributs de base
    def __init__(self, name, damage, type, _health=100, mana= 2):
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
