import random

class Character:
    def __init__(self, name, _health=100):
      self.name = name
      self._health = _health
      self.max_health = _health

    def action_success(self):
      chance = random.randint(30, 100)
      reussite = random.randint(30, 100)
      return reussite <= chance, chance

  #@staticmethod
  #def randomize(attack):
   # return random.randint(attack * 0.90, attack * 1.10)

    #Fonction pour attaquer une cible
    def do_attack(self, target, attack_name, attack_damage, attack_type):
      success, chance = self.action_success()
      if success:
        if attack_type == 'attack':
          target.take_damage(attack_damage)
          print(f"{self.name} utilise {attack_name} sur {target.name} et inflige {attack_damage} points de dégâts. (Chance de réussite : {chance}%)")
          print("\n")
        elif attack_type == 'distance':
          target.take_damage(attack_damage)
          print(f"{self.name} utilise {attack_name} sur {target.name} et inflige {attack_damage} points de dégâts. (Chance de réussite : {chance}%)")
          print("\n")
      else:
        print(f"{self.name} attaque {target.name} mais rate son attaque ! (Chance de réussite : {chance}%)")
        print("\n")

    #Fonction pour lancer un sort sur une cible
    def spell(self, target, sort_name, sort_damage, sort_effect):
      if self.nb_sorts > 0:
        success, chance = self.action_success()
        print(f"{self.name} utilise le sort {sort_name} sur {target.name} ! (Chance de réussite : {chance}%)")
        if sort_effect[0] == 'attack':
          if success:
            target.take_damage(sort_damage)
          elif sort_effect[0] == 'heal':
            target._health += sort_damage
            if target._health > target.max_health:
              target._health = target.max_health
            print(f"{self.name} soigne {target.name} de {sort_damage} points de vie et a maintenant {target._health} points de vie.")
            print("\n")
        else:
          print(f"Le sort de {self.name} échoue !")
        self.nb_sorts -= 1
        print(f"{self.name} a maintenant {self.nb_sorts} sorts restants.")
        print("\n")
      else:
        print(f"{self.name} n'a plus de sorts disponibles !")
        print("\n")

    #Fonction pour recevoir des dégâts, vérifier si le personnage est vivant et afficher son statut
    def take_damage(self, amount):
      self._health -= amount
      if self._health < 0:
        self._health = 0
      print(f"{self.name} prend {amount} points de dégâts et a maintenant {self._health} points de vie.")
      print("\n")

    #Fonction pour vérifier si le personnage est vivant
    def is_alive(self):
      return self._health > 0
  
    #Affichage du statut du personnage avec des cœurs pour représenter la vie
    def show_status(self):
      print(f"{self.name} - Vie: {'❤️' * (self._health // 10)} ({self._health}/{self.max_health}) | Sorts restants: {self.nb_sorts}")
