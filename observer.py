class Observer:
    def update(self, subject, event, attacker=None, chance=None):
      if event == 'take_damage':
        print(f"{subject.name} a été attaqué et a maintenant {subject._health} points de vie. Attaqué par : {attacker.name}")
      elif event == 'heal':
        print(f"{subject.name} a été soigné et a maintenant {subject._health} points de vie.")
      elif event == 'perform_turn':
        print(f"{subject.name} effectue son tour.")
      elif event == 'spell':
        print(f"{subject.name} lance un sort.")
      elif event == 'attack':
        print(f"{subject.name} attaque une cible. (Chance de réussite : {chance}%)")
      elif event == 'distance':
        print(f"{subject.name} attaque à distance. (Chance de réussite : {chance}%)")
      elif event == 'miss':
        print(f"{subject.name} rate son action. (Chance de réussite : {chance}%)")
      elif event == 'number_spells':
        print(f"{subject.name} a maintenant {subject.mana} mana restants.")
      elif event == 'no_spells':
        print(f"{subject.name} n'a plus de mana disponibles !")
      elif event == 'dead':
        print(f"{subject.name} est mort !")
      elif event == 'status':
        print(f"{subject.name} - Vie: {'❤️' * (subject._health // 10)} ({subject._health}/{subject.max_health}) | Mana restant: {subject.mana} | Vitesse: {subject.speed}")
      elif event == 'skip':
        print(f"{subject.name} décide de passer son tour.")
      elif event == 'mana_regen':
        print(f"{subject.name} régénère du mana et a maintenant {subject.mana} mana disponibles.")

class Observable:
    def __init__(self):
        self._observers = []

    #Ajouter un observateur
    def add_observer(self, observer):
        self._observers.append(observer)

    #Supprimer un observateur
    def remove_observer(self, observer):
        self._observers.remove(observer)

    #Notifier les observateurs d'un événement
    def notify(self, event, chance=None):
      for observer in self._observers:
        observer.update(self, event, chance)
