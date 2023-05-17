This is a simple rock-paper-scissors game played against the computer. 
Here's how it works:

1. The code imports an output module that contains ASCII art for rock, paper, and scissors images.
2. The get_user_choice function prompts the user to enter their choice of rock, paper, or scissors. The input is converted to lowercase and checked against valid choices. The corresponding numerical values (0 for rock, 1 for paper, 2 for scissors) are returned. If the input is not valid, None is returned.
3. The print_choices function takes the user's choice, the computer's choice, and a cheat flag. It prints the ASCII art corresponding to the user's choice and the computer's choice.
4. The determine_winner function compares the user's choice and the computer's choice to determine the winner. If the cheat flag is True, it returns a value of -10 to indicate cheating. Otherwise, it determines the winner based on the rules of rock-paper-scissors: a tie (0), the user wins (1), or the computer wins (-1).
5. The play_game function orchestrates a single round of the game. It obtains the user's choice, generates a random choice for the computer, and calls the print_choices and determine_winner functions. It returns the result of the game (-10 for cheating, 0 for a tie, 1 for a user win, -1 for a computer win).
6. The score dictionary keeps track of the user's and computer's scores.
7. The game is played within a while loop that continues until either the user or the computer reaches a score of 3.
8. In each iteration, the play_game function is called, and the result is stored in the result variable.
9. If the user cheats (enters unexpected value), the loop is terminated, and a message is displayed.
10. Once the loop is finished, the final scores are displayed.
