#!/home/tavaneshkade/workspace/rock_paper_spins/.venv/bin/python3
from config_loader import config

def two_player_game():
    options = config.get('options')
    for key, value in options.items():
        print(key,':', value)
    
    player_one_score = 0
    player_two_score = 0
    
    while True:
    
        if player_two_score == config.get('score').get('total_score'):
            print('player two, you win!!!!!!!!!!!!')
            break

        elif player_one_score == config.get('score').get('total_score'):
            print('player one, you win!!!!!!!!!!!!')
            break
        player_one_choice = (input('player one, Choose your item in options: '))
        if player_one_choice == 'score':
            print('player one, your score is', player_one_score)
            print('player two, your score is', player_two_score)
            continue
        if player_one_choice not in options:
            print('player one or player two, choose a item in options!')
            continue
        player_two_choice = (input('player two, Choose your item in options: '))
        
        if player_two_choice not in options:
            print('player one or player two, choose a item in options!')
            continue

        if player_two_choice == 'score':
            print('player one, your score is', player_one_score)
            print('player two, your score is', player_two_score)
            continue
        print('player one, your choose is', config.get('options').get(player_one_choice))
        print('player two, your choose is', config.get('options').get(player_two_choice))

        if player_one_choice == '1' and player_two_choice == '1':
            print('tie')
            continue

        elif player_one_choice == '1' and player_two_choice == '2':
            print('player one lose')
            print('player two win')
            player_two_score += 1
            continue

        elif player_one_choice == '1' and player_two_choice == '3':
            print('player one win')
            print('player two lose')
            player_one_score += 1
            continue

        elif player_one_choice == '2' and player_two_choice == '1':
            print('player one win')
            print('player two lose')
            player_one_score += 1
            continue

        elif player_one_choice == '2' and player_two_choice == '2':
            print('tie')
            continue

        elif player_one_choice == '2' and player_two_choice == '3':
            print('player one lose')
            print('player two win')
            player_two_score += 1
            continue

        elif player_one_choice == '3' and player_two_choice == '1':
            print('player one  lose')
            print('player two win')
            player_two_score += 1
            continue

        elif player_one_choice == '3' and player_two_choice == '2':
            print('player one win')
            print('player two lose')
            player_one_score += 1
            continue

        elif player_one_choice == '3' and player_two_choice == '3':
            print('tie')
            continue

if __name__ == '__main__':
    two_player_game()




