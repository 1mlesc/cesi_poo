from warrior import Warrior
from cleric import Cleric
from goblin import Goblin

class Factory:
  #Création de l'équipe des héros
  @staticmethod
  def create_hero_team():
    laezel = Warrior("Laezel", 20, "Warrior", 95)
    shadowheart = Cleric("Shadowheart", 13, "Cleric", 70)
    return [laezel, shadowheart]
  
  #Création de l'équipe des ennemis
  @staticmethod
  def create_enemy_team():
    miguel_tornado = Goblin('Miguel Tornado', 20, 'Goblin', 104)
    alexis = Goblin('Alexis', 15, 'Goblin', 80)
    return [miguel_tornado, alexis]