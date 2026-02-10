from factory import Factory

# Liste des personnages pour sélection
heros = Factory.create_hero_team()
enemies = Factory.create_enemy_team()
boss = Factory.create_boss()
all_characters = heros + enemies + [boss]
all_characters.sort(key=lambda c: c.speed, reverse=True)

print("Bienvenue dans le jeu de combat !")
print("Vos personnages : ")
for hero in heros:
  hero.show_status()
print("\nVotre adversaire : ")
for enemy in enemies:
  enemy.show_status()
print('\nLe Boss : ')
boss.show_status()

print(f"\nOrdre d'attaque : {[c.name for c in all_characters]}")
#Boucle de jeu qui continue tant que les héros et les ennemis sont vivants
tour = 1

while (any(h.is_alive() for h in heros)) and any(e.is_alive() for e in enemies):
  print(f"\n--- Tour {tour} ---")
  for character in all_characters:
    if character.is_alive():
      character.perform_turn(all_characters)
  tour += 1

#Message de fin de jeu lorsque qu'une équipe est complètement vaincue
if all(e.is_alive() == False for e in enemies):
  print("Félicitations ! Vous avez vaincu tous les ennemis !")
else:
  print("Vous avez été vaincu... Essayez à nouveau !")