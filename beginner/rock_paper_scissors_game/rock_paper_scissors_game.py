import random
import output


def get_user_choice():
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
    if user_choice.lower() in ["0", "rock"]:
        return 0
    elif user_choice.lower() in ["1", "paper"]:
        return 1
    elif user_choice.lower() in ["2", "scissors"]:
        return 2
    else:
        return None


def print_choices(user_choice, python_choice, cheat=False):
    print("Your choice:")
    if user_choice is not None:
        if user_choice == 0:
            print(output.rock)
        elif user_choice == 1:
            print(output.paper)
        elif user_choice == 2:
            print(output.scissors)
    else:
        cheat = True
        print(f"Not a valid choice.")

    print("Python choice:")
    if cheat:
        print(output.cheat)
    elif python_choice == 0:
        print(output.rock)
    elif python_choice == 1:
        print(output.paper)
    elif python_choice == 2:
        print(output.scissors)
    return cheat


def determine_winner(user_choice, python_choice, cheat):
    if not cheat:
        if python_choice == user_choice:
            print("Tie!")
            return 0
        elif (python_choice - user_choice) in [2, -1]:
            print("You win!")
            return 1
        else:
            print("You lose!")
            return -1
    else:
        return -10


def play_round():
    user_choice = get_user_choice()
    python_choice = random.randint(0, 2)
    cheat = print_choices(user_choice, python_choice)
    results = determine_winner(user_choice, python_choice, cheat)
    return results

def play_game():
    score = {'Your Score': 0, 'Python Score': 0}
    while score['Your Score'] < 3 and score['Python Score'] < 3:
        result = play_round()
        if result == 0:
            print(score)
            continue
        elif result == 1:
            score['Your Score'] += 1
            print(score)
        elif result == -1:
            score['Python Score'] += 1
            print(score)
        else:
            print(f'You are cheating! Game over.')
            break

continue_playing = True
while continue_playing:
    play_game()
    playing = input(f'Do you want to play again? Type "y" for Yes, "n" for No. ').lower()
    if playing in ['n', 'no']:
        print('Good Bye!')
        continue_playing = False
    elif playing in ['y', 'yes']:
        continue
    else:
        print('Incorrect input. Good Bye!')
        continue_playing = False




