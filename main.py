from single_player_game import single_player_game
from two_player_game import two_player_game

def main():
    print("are you ready to game ?")
    while True:
        game_type= input("you have two choice: two player game, single player game: ")
        if game_type != "single player game" and game_type != "two player game":
            print("please choose another option")
            continue
        elif game_type == "single player game":
            single_player_game()
            break

        elif game_type == "two player game":
            two_player_game()
            break

if __name__ == "__main__":
    main()