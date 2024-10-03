import random
from art import logo


def deal_card():
    """
    Returns a random card from the deck.

    The deck consists of numbers 2-10, Jack (10), Queen (10), King (10),
    and Ace (11).
    """
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card)


def calc_score(cards):
    """
    Calculates the total score of the given cards.

    If the total score is greater than 21 and the player has an Ace (11),
    the Ace is counted as 1 to avoid busting.

    Args:
    cards (list): List of card values.

    Returns:
    int: The total score after adjustments for Aces.
    """
    score = sum(cards)

    # Convert Ace (11) to 1 if score exceeds 21
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return score


def check_limits(user_score, computer_score):
    """
    Checks if either the user or computer has exceeded a score of 21.

    Args:
    user_score (int): Player's total score.
    computer_score (int): Computer's total score.

    Returns:
    int: Returns 1 if the user is busted (score > 21),
         2 if the computer is busted, or None if no one is busted.
    """
    if user_score > 21:
        return 1
    elif computer_score > 21:
        return 2


def check_winner(user_score, computer_score):
    """
    Compares the scores and prints the result of the game.

    Args:
    user_score (int): Player's total score.
    computer_score (int): Computer's total score.
    """
    if computer_score < user_score < 21:
        print("You win.")
    elif user_score == 21:
        print("It is a Blackjack, you win")

    if user_score < computer_score and computer_score < 21:
        print("You lose.")
    elif computer_score == 21:
        print("It is a computer's Blackjack, you lose")
    elif user_score < 21 < computer_score:
        print("You win.")

    if computer_score == user_score:
        print("It is a draw")


def play_game():
    """
    Main function to play the Blackjack game.
    It deals initial cards to both user and computer, and checks for any immediate
    Blackjack or bust conditions. Then it prompts the user if they want another card
    and handles the computer's turn based on its score.
    """
    print(logo)

    # Initialize cards for both user and computer
    user_cards = []
    computer_cards = []
    game_over = False

    # Deal two cards each to user and computer at the start
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Continue game until either game over conditions are met
    while not game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        # Display the current cards and score of the user and computer
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        # Check if the user or computer is busted
        if check_limits(user_score, computer_score) == 1:
            print(f"   Your final hand: {user_cards}, final score: {user_score}")
            print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("You lose, Busted")
            game_over = True
        elif check_limits(user_score, computer_score) == 2:
            print(f"   Your final hand: {user_cards}, final score: {user_score}")
            print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("Computer loses, Busted")
            game_over = True
        elif user_score == 21:
            print(f"   Your final hand: {user_cards}, final score: {user_score}")
            print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("It is a Blackjack. You win!")
            game_over = True
        elif computer_score == 21:
            print(f"   Your final hand: {user_cards}, final score: {user_score}")
            print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("It is a computer's Blackjack. You lose.")
            game_over = True

        # If game is still ongoing, prompt the user for action
        if not game_over:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_deal == 'y':
                # User requests another card
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
            else:
                # User passes, computer continues if score is less than 17
                game_over = True
                while computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calc_score(computer_cards)

                # Final comparison of scores after computer completes its turn
                print(f"   Your final hand: {user_cards}, final score: {user_score}")
                print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
                check_winner(user_score, computer_score)


# Main loop to start and repeat the game
program_run = True

while program_run:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        play_game()
    else:
        print("Thanks for playing Blackjack game.")
        program_run = False