import random
score = 0
def choose_superhero():
    print("Super archer: 1")
    print("Super knight: 2")
    print("Super cavelry unit: 3")
    character = input("what class would you like to be? ")
    player_name = input("what is your character's name? ")
    return character, player_name

def game_intro(player_superhero):
    print(f"Welcome {player_superhero}, to the world of Gorlan! You will be tasked with ridding this world of the black lord Morgorath")

def make_decision():
     print("Morgorath is attacking the castle! Do you go stop him, or seek help from Sir. Digby the knight")   
     decision = input("1 for face him, 2 for get help")  
     while True:
        if decision=="1" or decision=="2":
            return decision
        else:
            print()

def health_managment(current_health, damage_taken):
    return current_health-damage_taken

def superhero_mission(action, player_superhero):
    function_score = score
    if action=="1":
        if player_superhero=="1":
            print("You face the black lord, and your arrows go through his heart. You return victorious")
            function_score +=10

        else:
            print("you find the black lord armed and ready for your attack. Prepare to fight")
            running = True
            while running:
                stroke = input("What attack would you like to do? 1 for thrust, 2 for overhand, 3 for sideswipe")
                if stroke=="1":
                    if random.randint(0,100)<90:
                        print("your stroke connects and finishes the black lord off. You return home victorious")
                        function_score +=20
                    else:
                        print("Your attack failed, leaving you vunerable to a counterattack. You don't return home")
                        function_score-=20
                    running = False
                elif stroke=="2" or stroke=="3":
                    if random.randint(0,100)<50:
                        print("your stroke connects and finishes the black lord off. You return home victorious")
                        function_score+=30
                    else:
                        print("Your attack failed, leaving you vunerable to a counterattack. You don't return home")
                        function_score-=10
                    running = False
                else:
                    print("invalid input")
                    
    elif action=="2":
        if player_superhero=="1":
            print("You and Sir Digby find Morgorath occupying the capitol. He has the royal army at his disposal, and you stand no chance. Neither of you return home")
        else:
            print("You find him dismounted and unarmed. The fight was done after one stroke. You return home victorious")
    return score
character, player_name = choose_superhero()
game_intro(player_name)
decision = make_decision()
score = superhero_mission(decision, character)
print(f"your score was {score}")