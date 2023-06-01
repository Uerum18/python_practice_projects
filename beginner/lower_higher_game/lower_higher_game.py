import random
import game_data
import logo

selected_accounts = list()
user_score = 0


def pick_account():
    """
    Picks random uniq account which wasn't selected previously.
    """
    account = False
    account_pick = ""
    while not account:
        account_pick = random.choice(game_data.data)
        if account_pick not in selected_accounts:
            selected_accounts.append(account_pick)
            account = True
    return account_pick


def check_results(acc_a, acc_b, user_pick):
    """
    Takes both of accounts and user choice. Returns True if user guessed else - False.
    """
    if user_pick.lower() == 'a':
        return True if acc_a['follower_count'] > acc_b['follower_count'] else False
    elif user_pick.lower() == 'b':
        return True if acc_a['follower_count'] < acc_b['follower_count'] else False
    else:
        print('Error: Invalid selection.')
        return False


def game(acc_a=None):
    global user_score
    acc_a = acc_a or pick_account()
    print(f"Compare A: {acc_a['name']}, a {acc_a['description']} from {acc_a['country']}.")
    print(logo.vs)
    acc_b = pick_account()
    print(f"Against B: {acc_b['name']}, a {acc_b['description']} from {acc_b['country']}.")
    user_pick = input("Who has more followers? Type 'A' or 'B': ")
    if check_results(acc_a, acc_b, user_pick):
        user_score += 1
        print(f"You're right! Your score is {user_score}.")
        game(acc_b)
    else:
        print(f"Sorry. That's wrong. Your final score is {user_score}.")


if __name__ == "__main__":
    print(logo.logo)
    game()
