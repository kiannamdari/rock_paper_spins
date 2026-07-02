import random

from config_loader import config

def play():
    options = config.get('options')
    for key, value in options.items():
        print(key,':', value)
    player_score = 0
    bot_score = 0
    while True:
        bot = random.randint(1, 3)

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
        print('bot choose is', bot)

        if choice == '1' and bot == 1:
            print('tie')
            continue

        elif choice == '1' and bot == 2:
            print('you lose')
            bot_score += 1
            continue

        elif choice == '1' and bot == 3:
            print('you win')
            player_score += 1
            continue

        elif choice == '2' and bot == 1:
            print('you win')
            player_score += 1
            continue

        elif choice == '2' and bot == 2:
            print('tie')
            continue

        elif choice == '2' and bot == 3:
            print('you lose')
            bot_score += 1
            continue

        elif choice == '3' and bot == 1:
            print('you lose')
            bot_score += 1
            continue

        elif choice == '3' and bot == 2:
            print('you win')
            player_score += 1
            continue

        elif choice == '3' and bot == 3:
            print('tie')
            continue

result = play()





