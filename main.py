from factory import Factory

heros_team = Factory.create_hero_team()
enemies_team = Factory.create_enemy_team()
boss = Factory.create_boss()
all_characters = heros_team.get_alive_members() + enemies_team.get_alive_members() + [boss]
all_characters.sort(key=lambda c: c.speed, reverse=True)

def show_status_tour():
  print("Bienvenue dans le jeu de combat !")
  print("Vos personnages : ")
  for hero in heros_team.members:
      hero.show_status()

  print("\nVotre adversaire : ")
  for enemy in enemies_team.members:
      enemy.show_status()
  print('\nLe Boss : ')
  boss.show_status()

show_status_tour()
print(f"\nOrdre d'attaque : {[c.name for c in all_characters]}")
#Boucle de jeu qui continue tant que les héros et les ennemis sont vivants
tour = 1
mana_regen = 5


while not heros_team.is_defeated() and not enemies_team.is_defeated():
    print(f"\n--- Tour {tour} ---")
    all_characters = heros_team.get_alive_members() + enemies_team.get_alive_members() + ([boss] if boss.is_alive() else [])
    all_characters.sort(key=lambda c: c.speed, reverse=True)
    for character in all_characters:
        if character.is_alive():
            character.perform_turn(all_characters)
            if tour % 2 == 0:
                if hasattr(character, 'mana'):
                    character.mana = min(character.mana + mana_regen, 10)  # Regenerate mana, max 10
                    character.notify('mana_regen')
    tour += 1
    show_status_tour()

#Message de fin de jeu lorsque qu'une équipe est complètement vaincue
if enemies_team.is_defeated or boss.is_defeated():
    print("Félicitations ! Vous avez vaincu tous les ennemis !")
else:
    print("Vous avez été vaincu... Essayez à nouveau !")