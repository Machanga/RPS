import random

choices = ['R','S','P']

def get_player_choice():
    try:
        player_choice = input("Pick  a choice (R = rock, P = paper, S = scissors): ")
    except:
        if player_choice.upper() not in choices:
            print("Kindly pick R, P, or S: (R=rock, P=paper, S=scissors)")
            player_choice = input("Pick  a choice (R = rock, P = paper, S = scissors): ")
    return player_choice.upper()

def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice

def check_if_draw(player_choice, computer_choice):
    if player_choice == computer_choice:
        return player_choice

def print_winner(player_choice, computer_choice):
    if player_choice == 'R' and computer_choice == 'S':
        print('Rock smashes scissors! Player wins!')
    elif player_choice == 'S' and computer_choice == 'P':
        print('Scissors cuts paper! Player wins!')
    elif player_choice == 'P' and computer_choice == 'R':
        print('Paper covers rock! Player wins!')
    else:
        print('Computer wins!')
        print("{} beats {}").format(computer_choice, player_choice)

def rock_paper_scissors():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if check_if_draw(player_choice, computer_choice):
        print("It's a draw! Both players picked {}: ".format(player_choice))
        rock_paper_scissors()
    else:
        print(f"\nPlayer {player_choice} : CPU {computer_choice}.\n")
        print_winner(player_choice, computer_choice)
        
rock_paper_scissors()