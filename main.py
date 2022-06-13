import random

choices = ['R','S','P']

def get_player_choice():
    try:
        Player = input("Pick  a choice (R = rock, P = paper, S = scissors): ")
    except:
        if Player.upper() not in choices:
            print("Kindly pick R, P, or S: (R=rock, P=paper, S=scissors)")
            Player = input("Pick  a choice (R = rock, P = paper, S = scissors): ")
    return Player.upper()

def get_computer_choice():
    CPU = random.choice(choices)
    return CPU

def check_if_draw(Player, CPU):
    if Player == CPU:
        return Player

def print_winner(Player, CPU):
    if Player == 'R' and CPU == 'S':
        print('Rock smashes scissors! Player wins!')
    elif Player == 'S' and CPU == 'P':
        print('Scissors cuts paper! Player wins!')
    elif Player == 'P' and CPU == 'R':
        print('Paper covers rock! Player wins!')
    else:
        print('Computer wins!')
        print("%s smashes/covers/cuts %s" % (CPU, Player))

def rock_paper_scissors():
    Player = get_player_choice()
    CPU = get_computer_choice()
    if check_if_draw(Player, CPU):
        print(f"\nIt's a draw! Both players picked {Player}.\n")
        rock_paper_scissors()
    else:
        print(f"\nPlayer {Player} : CPU {CPU}.\n")
        print_winner(Player, CPU)
        
rock_paper_scissors()
