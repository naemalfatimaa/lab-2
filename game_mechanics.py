#  Game Mechanics
#    Student A (team lead)
# ---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    # ------------------------
    # Add your code here
    print("Welcome to trivia trek!")


welcome_message()

# ------------------------


def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    print("Choose a category:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    choice = int(input("Enter the number corresponding to your chosen category: "))
    return categories[choice - 1]

categories = ["math", "science"]
chosen_category = choose_category(categories)
print("You have chosen the following category:", chosen_category)


# ------------------------




# ---------------------------------------
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    print("Game over! Your final score is", final_score)

# ---------------------------------------

def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    round_number = 1
    score = 0
    incorrect_answers = 0

    while round_number <= 5 and not check_game_over(incorrect_answers):
        current_category = choose_category(categories)

        round_number = next_round(round_number)

    game_over_message(score)

# ---------------------------------------

def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    # ------------------------
    # Add your code here
    return player_answer == correct_answer
    # ------------------------


# ---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    # ------------------------
    # Add your code here
    if correct:
        score += 1
    return score

# ---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    # ------------------------
    # Add your code here
    return round_number + 1

# ---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    # ------------------------
    # Add your code here
    return incorrect_answers >= 3

# ------------------------


# ---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    # ------------------------
    # Add your code here
    while True:
        choice = input("Do you want to play again? ")
        if choice == "yes":
            run_game_rounds(categories)
        elif choice == "no":
            print("Thank you for playing")
            break
        else:
            print("Invalid")



# ---------------------------------------
