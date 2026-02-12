import random
from observer import Observable

class Character(Observable):
    def __init__(self, name, _health=100):
      super().__init__()
      self.name = name
      self.speed = random.randint(0, 10)
      self._health = _health
      self.max_health = _health

    def action_success(self):
     # chance = random.randint(40, 100)
      #reussite = random.randint(40, 100)
      #return reussite <= chance, chance

      return True, 100

  #@staticmethod
  #def randomize(attack):
   # return random.randint(attack * 0.90, attack * 1.10)

    #Fonction pour attaquer une cible
    def do_attack(self, target, attack_type, attack_damage):
      success, chance = self.action_success()
      if success:
        print(f"Attaque type : {attack_type}")
        if attack_type == 'attack':
          target.take_damage(attack_damage, self)
          self.notify('attack', chance)
        elif attack_type == 'distance':
          target.take_damage(attack_damage, self)
          self.notify('distance', chance)
      else:
        self.notify('miss', chance)

    #Fonction pour lancer un sort sur une cible
    def spell(self, target, spell):
      if self.mana >= spell.mana_cost:
        self.mana -= spell.mana_cost
        success, chance = self.action_success()
        self.notify('spell', chance)
        if spell.type == 'attack':
          if success:
            target.take_damage(spell.damage, self)
            self.notify('number_spells', self.mana)
          elif spell.type == 'heal':
            target._health += spell.damage
            if target._health > target.max_health:
              target._health = target.max_health
            self.notify('heal')
            self.notify('number_spells')
        else:
          self.notify('miss', chance)
        self.mana -= 1
      else:
        self.notify('no_spells')

    #Fonction pour recevoir des dégâts, vérifier si le personnage est vivant et afficher son statut
    def take_damage(self, amount, attacker):
      self._health -= amount
      if self._health < 0:
        self._health = 0
        self.notify('dead')
      self.notify('take_damage', attacker)

    #Fonction pour vérifier si le personnage est vivant
    def is_alive(self):
      return self._health > 0
  
    #Affichage du statut du personnage avec des cœurs pour représenter la vie
    def show_status(self):
      self.notify('status')

    def add_observer(self, observer):
      super().add_observer(observer)

    def remove_observer(self, observer):
      super().remove_observer(observer)
