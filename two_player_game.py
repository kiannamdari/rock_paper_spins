#!/home/tavaneshkade/workspace/rock_paper_spins/.venv/bin/python3
import json

from config_loader import config

def two_player_game():
    options = config.get('options')
    for key, value in options.items():
        print(key,':', value)
    
    player_one_score = 0
    player_two_score = 0
    game_history = {
        "round_one": {},
        "round_two": {},
        "round_three": {},
        "round_four": {},
        "round_five": {},
    }
    round_counter = 1
    while True:
        if player_one_score != 3 and player_two_score != 3:
            player_one_choice = (input('player one, Choose your item in options: '))

            if player_one_choice == 'score':
                print('player one, your score is', player_one_score)
                print('player two, your score is', player_two_score)
                continue
            
            if player_one_choice not in options:
                print('player one or player two, choose a item in options!')
                continue

            player_one_act = config["options"][player_one_choice]
            player_two_choice = (input('player two, Choose your item in options: '))

            if player_two_choice not in options:
                print('player one or player two, choose a item in options!')
                continue

            if player_two_choice == 'score':
                print('player one, your score is', player_one_score)
                print('player two, your score is', player_two_score)
                continue
            
            player_two_act = config["options"][player_two_choice]

            print('player one, your choose is', config.get('options').get(player_one_choice))
            print('player two, your choose is', config.get('options').get(player_two_choice))

            if player_one_choice == '1' and player_two_choice == '1':
                print('tie')
                continue

            elif player_one_choice == '1' and player_two_choice == '2':
                print('player one lose')
                print('player two win')
                player_two_score += 1
                
            elif player_one_choice == '1' and player_two_choice == '3':
                print('player one win')
                print('player two lose')
                player_one_score += 1
                
            elif player_one_choice == '2' and player_two_choice == '1':
                print('player one win')
                print('player two lose')
                player_one_score += 1
                
            elif player_one_choice == '2' and player_two_choice == '2':
                print('tie')
                continue

            elif player_one_choice == '2' and player_two_choice == '3':
                print('player one lose')
                print('player two win')
                player_two_score += 1

            elif player_one_choice == '3' and player_two_choice == '1':
                print('player one  lose')
                print('player two win')
                player_two_score += 1
        
            elif player_one_choice == '3' and player_two_choice == '2':
                print('player one win')
                print('player two lose')
                player_one_score += 1
                continue

            elif player_one_choice == '3' and player_two_choice == '3':
                print('tie')
                continue
            
            if round_counter == 1:
                round_one = {
                    "player_one_score": player_one_score,
                    "player_two_score": player_two_score,
                    "player_one_choice": player_one_act,
                    "player_two_choice": player_two_act,
                }
                game_history.update({"round_one": round_one})
        
            elif round_counter == 2:
                round_two = {
                    "player_one_score": player_one_score,
                    "player_two_score": player_two_score,
                    "player_one_choice": player_one_act,
                    "player_two_choice": player_two_act,
                }
                game_history.update({"round_two": round_two})
        
            elif round_counter == 3:
                round_three = {
                    "player_one_score": player_one_score,
                    "player_two_score": player_two_score,
                    "player_one_choice": player_one_act,
                    "player_two_choice": player_two_act,
                }
                game_history.update({"round_three": round_three})
        
            elif round_counter == 4:
                round_four = {
                    "player_one_score": player_one_score,
                    "player_two_score": player_two_score,
                    "player_one_choice": player_one_act,
                    "player_two_choice": player_two_act,
                }
                game_history.update({"round_four": round_four})

            elif round_counter == 5:
                round_five = {
                    "player_one_score": player_one_score,
                    "player_two_score": player_two_score,
                    "player_one_choice": player_one_act,
                    "player_two_choice": player_two_act,
                }
                game_history.update({"round_five": round_five})                     

            round_counter += 1

        elif player_two_score == config.get('score').get('total_score'):
            print('player two is winner !!!!!!!!!!!!')
            break

        elif player_one_score == config.get('score').get('total_score'):
            print('player one is winner !!!!!!!!!!!!')
            break
    with open("two_player_game_history.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(game_history, indent=4))
