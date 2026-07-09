#!/home/tavaneshkade/workspace/rock_paper_spins/.venv/bin/python3
import random
import json
from config_loader import config

def single_player_game():
    options = config.get('options')
    bot_options = ['rock', 'paper', 'scissors']
    for key, value in options.items():
        print(key,':', value)
    player_score = 0
    bot_score = 0
    game_history = {
        "round_one": {},
        "round_two": {},
        "round_three": {},
        "round_four": {},
        "round_five": {},
    }
    round_counter = 1
    while True:
        bot_choice = random.choice(bot_options)

        if player_score != config["score"]["total_score"] and bot_score != config["score"]["total_score"]:
            choice = (input('Choose your number in options: '))


            if choice not in options:
                print('choose a variable in options')
                continue

            if choice == 'score':
                print('your score is', player_score)
                print('bot score is', bot_score)
                continue
            act = config["options"][choice]
            print('your choose is', config.get('options').get(choice))
            print('bot choose is', bot_choice)

            if choice == '1' and bot_choice == 'rock':
                print('tie')
                continue

            elif choice == '1' and bot_choice == 'paper':
                print('you lose')
                bot_score += 1


            elif choice == '1' and bot_choice == 'scissors':
                print('you win')
                player_score += 1


            elif choice == '2' and bot_choice == 'rock':
                print('you win')
                player_score += 1


            elif choice == '2' and bot_choice == 'paper':
                print('tie')
                continue

            elif choice == '2' and bot_choice == 'scissors':
                print('you lose')
                bot_score += 1


            elif choice == '3' and bot_choice == 'rock':
                print('you lose')
                bot_score += 1


            elif choice == '3' and bot_choice == 'paper':
                print('you win')
                player_score += 1

            elif choice == '3' and bot_choice == 'scissors':
                print('tie')
                continue

            if round_counter == 1:
                round_one = {
                    "player_choice": act,
                    "bot_choice": bot_choice,
                    "player_score": player_score,
                    "bot_score": bot_score
                }
                game_history.update({"round_one": round_one})

            if round_counter == 2:
                 round_two = {
                    "player_choice": act,
                    "bot_choice": bot_choice,
                    "player_score": player_score,
                    "bot_score": bot_score
                 }
                 game_history.update({"round_two": round_two})

            if round_counter == 3:
                round_three = {
                "player_choice": act,
                "bot_choice": bot_choice,
                "player_score": player_score,
                "bot_score": bot_score
                }
                game_history.update({"round_three": round_three})

            if round_counter == 4:
                round_four = {
                "player_choice": act,
                "bot_choice": bot_choice,
                "player_score": player_score,
                "bot_score": bot_score
                }
                game_history.update({"round_four": round_four})

            if round_counter == 5:
                round_five = {
                "player_choice": act,
                "bot_choice": bot_choice,
                "player_score": player_score,
                "bot_score": bot_score
                }
                game_history.update({"round_five": round_five})

            round_counter += 1
            continue

        elif player_score == config.get("score").get("total_score"):
            print("you are winner !!!!!!!!!!!!")
            break

        elif bot_score == config.get("score").get("total_score"):
            print("bot is winner !!!!!!!!!!!!!")
            break

    with open("single_player_game_history.json", "w" , encoding="utf-8") as f:
        f.write(json.dumps(game_history, indent=4))

if __name__ == '__main__':
    single_player_game()
