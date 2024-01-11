import random

# name, health, attacks 1 2 and 3, defence
squirtle = ["Squirtle", 225, 500, 700, 900, 30]
bulbasaur = ["Bulbasaur", 250, 500, 600, 900, 40]
mewtwo = ["MewTwo", 300, 800, 900, 1000, 50]
score = 0

#Task 1 (Pokemon Selection)
def choose_pokemon():
    while True:
        print("Pikachu - 1")
        print("Charmander - 2")
        print("Greninja - 3")
        p = input("Please pick a Pokemon: ")
        print()
        if p == "1":
            #name, attack 1 2 3, health defence
            pokemon = ["Pikachu",80,90,50,255,30]
            break
        elif p == "2":
            pokemon = ["Charmander",82,40,78,210,45]
            break
        elif p == "3":
            pokemon = ["Greninja",75,86,67,240,40]
            break
        else:
            print("Invalid Pokemon please pick again!")
            print()
    pokemon.append(input("What is your character's name? "))
    return pokemon

#Task 2 (Game Introduction)
def game_intro(player_pokemon):
    print(f"Welcome {player_pokemon[6]} to the World of Pokemon. You and your partner {player_pokemon[0]} \
are at the start of a long journey to become a Pokemon Trainer.")
    print("This jounery won't be easy, it will be challenging, but you must persevere. Goodluck on your journey!")
    print()

#Task 3 (Decision Making)
def get_enemy():
    num = random.randint(1,3)
    if num==1:
        enemy=squirtle
    elif num==2:
        enemy=bulbasaur
    else:
        enemy=mewtwo
    print(f"You encountered a wild {enemy[0]}!")
    return enemy
def make_decision():
    while True:
        battle_or_catch = input("Do you want to battle it or catch it? Enter 1 for battle, 2 for catch")
        if battle_or_catch == "1" or battle_or_catch=="2":
            break
        else:
            print("invalid input")
            print()
    if battle_or_catch == "1":
        while True:
            get_attack = input("which attack do you want to use? Enter 1, 2, or 3: ")
            print()
            if get_attack == "1" or get_attack == "2" or get_attack == "3":
                break
            else:
                print("invalid input")
                print()
    else:
        get_attack = False
    return battle_or_catch, get_attack

#create manage_health, which subtracts the damage taken from current health
def manage_health(current_health, damage_taken):
    new_health = current_health - damage_taken
    return new_health

#create pokemon_battle which controls the battle scenario.
def pokemon_battle(action, player_pokemon, enemy):
    #creating local variables to avoid errors
    your_health = player_pokemon[4]
    new_score = score

    #if the action is battle, not catch
    if action == "1":
        #attack is a global variable that make_decision will provide
        if attack=='1':
            damage = (player_pokemon[1]/100)*enemy[5]
        elif attack=='2':
            damage = (player_pokemon[2]/100)*enemy[5]
        elif attack=='3':
            damage = (player_pokemon[3]/100)*enemy[5]
        else:
            damage=0
        #makes the enemy's health go down
        enemy[1] = manage_health(enemy[1], damage)

        #prints the enemy's health
        if enemy[1]<=0:
            print(f"{enemy[0]} died.")
            new_score += 10
            player_pokemon[4]=False
        else:
            print(f"{enemy[0]} now has {enemy[1]} health.")

        #makes your health go down
        enemy_attack = random.randint(2, 4)
        enemy_damage = (enemy[enemy_attack]*10)/player_pokemon[5]
        player_pokemon[4] = manage_health(player_pokemon[4], enemy_damage)
        #prints your health
        if player_pokemon[4]<=0:
            print(f"{player_pokemon[0]} died.")
            print()
            new_score -=10
            player_pokemon[4] = False
        else:
            print(f"{player_pokemon[0]} took {damage} damage! It now has {player_pokemon[4]} health.")
            print()

    #if the player chooses to catch
    elif action == "2":
        #random chance if the catch is succesful or not. goes down as your health goes down
        catch_percent = (100/player_pokemon[4])*10
        if random.randint(0, 100)<catch_percent:
            print("The catch was successful!!")
            new_score = new_score + 100
            player_pokemon[4]=False
        else:
            print("Sorry, the catch failed")
            enemy_attack = random.randint(2, 4)
            enemy_damage = (enemy[enemy_attack]*10)/player_pokemon[5]
            player_pokemon[4] = manage_health(player_pokemon[4], enemy_damage)
            #prints your health
            if player_pokemon[4]<=0:
                print(f"{player_pokemon[0]} died.")
                print()
                new_score -=10
                player_pokemon[4] = False
            else:
                print(f"{player_pokemon[0]} took {enemy_damage} damage! It now has {player_pokemon[4]} health.")
                print()
    
    return player_pokemon, new_score

def print_score(score, player_pokemon):
    print(f"Congradulations {player_pokemon[6]}! You got a score of {score}")
score = 0
player_pokemon = choose_pokemon()
game_intro(player_pokemon)
enemy = get_enemy()
while player_pokemon[4]:
    battle_or_catch, attack = make_decision()
    player_pokemon, score = pokemon_battle(battle_or_catch, player_pokemon, enemy)
print_score(score, player_pokemon)