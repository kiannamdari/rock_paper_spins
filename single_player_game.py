#!/home/tavaneshkade/workspace/rock_paper_spins/.venv/bin/python3
import random

from config_loader import config

def single_player_game():
    options = config.get('options')
    bot_options = ['rock', 'paper', 'scissors']
    for key, value in options.items():
        print(key,':', value)
    player_score = 0
    bot_score = 0
    while True:
        bot_choice = random.choice(bot_options)

        if bot_score == config.get('score').get('total_score'):
            print('bot win!!!!!!!!!!!!')
            break

        elif player_score == config.get('score').get('total_score'):
            print('you win!!!!!!!!!!!!')
            break
        choice = (input('Choose your number in options: '))

        if choice not in options:
            print('choose a variable in options')
            continue

        if choice == 'score':
            print('your score is', player_score)
            print('bot score is', bot_score)
            continue
        print('your choose is', config.get('options').get(choice))
        print('bot choose is', bot_choice)

        if choice == '1' and bot_choice == 'rock':
            print('tie')
            continue

        elif choice == '1' and bot_choice == 'paper':
            print('you lose')
            bot_score += 1
            continue

        elif choice == '1' and bot_choice == 'scissors':
            print('you win')
            player_score += 1
            continue

        elif choice == '2' and bot_choice == 'rock':
            print('you win')
            player_score += 1
            continue

        elif choice == '2' and bot_choice == 'paper':
            print('tie')
            continue

        elif choice == '2' and bot_choice == 'scissors':
            print('you lose')
            bot_score += 1
            continue

        elif choice == '3' and bot_choice == 'rock':
            print('you lose')
            bot_score += 1
            continue

        elif choice == '3' and bot_choice == 'paper':
            print('you win')
            player_score += 1
            continue

        elif choice == '3' and bot_choice == 'scissors':
            print('tie')
            continue

if __name__ == '__main__':
    single_player_game()





