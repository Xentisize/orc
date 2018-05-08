import random
import textwrap


def high_lighted(msg):
    return '\033[1m' + msg + '\033[0m'


def print_dotted_line(width=72):
    print('-' * width)


def show_theme_message(width=72):
    print_dotted_line()
    print(high_lighted('Attack of The Orcs v0.0.1:'))
    msg = '''The war between humans and their arch enemies, Orcs, was in the offing. Sir Foo, one of the brave knights guarding the southern plains began a long journey towards the east through an unknown dense forest. On his way, he spotted a small isolated settlement. Tired and hoping to replensih his food stock, he decided to take a detour. As he approached the village, he saw five huts. There was no one to be seen around. Hesitantly, he decided to enter...'''
    print(textwrap.fill(msg, width))


def show_game_mission():
    print(high_lighted('Mission:'))
    print('\tChoose a hut where Sir Foo can rest...')
    print(high_lighted('TIP:'))
    print('\tBe careful as there are enemies lurking around!')
    print_dotted_line()


def occupy_huts(occupants, number_of_huts=5,):
    huts = []
    while len(huts) < number_of_huts:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts


def process_user_choice(number_of_huts=5):
    msg = high_lighted(f'Choose a hut number to enter (1-{number_of_huts}): ')
    user_choice = input('\n' + msg)
    idx = int(user_choice)
    return idx


def reveal_occupants(idx, huts):
    """Print the occupants of the hut."""
    msg = ''
    print('Revealing the occupants...')
    for i in range(len(huts)):
        occupant_info = '<%d:%s>' % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = high_lighted(occupant_info)
        msg += occupant_info
    print('\t' + msg)
    print_dotted_line()


def enter_hut(idx, huts):
    print(high_lighted('Entering hut %d... ' % idx), end=' ')

    if huts[idx - 1] == 'enemy':
        print(high_lighted('YOU LOSE! Better luck next time!'))
    else:
        print(high_lighted('Congratulation! You win!'))
    print_dotted_line()


def run_application():
    keep_playing = 'y'
    occupants = ['enemy', 'friend', 'unoccupied']
    width = 72
    dotted_line = '-' * width

    show_theme_message(width)
    show_game_mission()

    while keep_playing == 'y':
        huts = occupy_huts(occupants)
        idx = process_user_choice(len(huts))
        reveal_occupants(idx, huts)
        enter_hut(idx, huts)
        keep_playing = input('Play again? Yes(y)/No(n): ')


if __name__ == '__main__':
    run_application()

