import random
import utils

user_selections = list()


def pick_word():
    print(utils.logo)
    word = random.choice(utils.words)
    mask = str()
    letters = list()
    for i in range(len(word)):
        mask += "_"
    print(mask)
    return {"word": word, "mask": mask, "letters": letters}


def user_guess(task, user_life):
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1:
        print(f"Please, type only one letter at once.\n{task['mask']}")
        return 0
    elif guess in user_selections:
        print(f"Oops, looks like the '{guess}' was already chosen. Please guess another letter.\n{task['mask']}")
        return 0
    elif guess not in task['word']:
        user_selections.append(guess)
        if user_life > 1:
            print(f"Better luck next time! You have {user_life - 1} lives left.\n{task['mask']}")
        else:
            print(f"Last chance!\n{task['mask']}")
        return 1
    else:
        user_selections.append(guess)
        replace_mask(task, guess)
        print(f"{random.choice(['Nice catch!', 'Wow!', 'Great Job!', 'You got it!', 'Correct!'])}\n{task['mask']}")
        return 0


def replace_mask(task, letter):
    letters_count = task['word'].count(letter)
    indx = 0
    while letters_count > 0:
        indx = task['word'].index(letter, indx)
        task['mask'] = task['mask'][:indx] + letter + task['mask'][indx + 1:]
        letters_count -= 1
        indx += 1


def play_game(user_life=6):
    word = pick_word()
    while user_life > 0 and word['word'] != word['mask']:
        result = user_guess(word, user_life)
        user_life -= result
        print(utils.stages[user_life])
    if user_life == 0:
        print(f"You Lose! The answer is {word['word']}.")
    else:
        print(f"You Win! The answer is {word['word']}. Congratulations!")


continue_playing = True
while continue_playing:
    play_game()
    playing = input(f'Do you want to play again? Type "y" for Yes, "n" for No. ').lower()
    if playing in ['n', 'no']:
        print('Good Bye!')
        continue_playing = False
    elif playing in ['y', 'yes']:
        user_selections.clear()
    else:
        print('Incorrect input. Game over.')
        continue_playing = False
