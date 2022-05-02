import random
import os

# 1 is equal to 11 until we reach total of 21. all royalty cards equal to 10.

over21 = False
lose = False
endloop = False


def dealcard():
    allcards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(allcards)
    return card


def calculate_score(cards: list):
    # returns the sum of the score. or 0 in case of blackjack
    cards_sum = sum(cards)
    if cards_sum == 21 and len(cards) == 2:
        return 0
    # if the score reaches 21, check whether the cards contain any aces('11'). if so, turn the aces to '1'
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(userscore, compscore):
    if userscore > 21 and compscore > 21:
        return "You went over 21. you lose."
    elif userscore == 0:
        return "You have a Blackjack! You win!"
    elif compscore == 0:
        return "Computer have a blackjack! you lose."
    elif userscore > 21:
        return "You went over 21. You lose."
    elif compscore > 21:
        return "Computer went over 21. You win! "
    # if nobody has a blackjack (both scores aren't 0)
    elif userscore > compscore:
        return "You win!"
    else:
        return "You lost!"


def play():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(dealcard())
        computer_cards.append(dealcard())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # if theres a blackjack or the user's score is too high, we don't need to continue to the next iteration
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hitme = input(
                "\nType 'y' to get another cards or press enter to continue "
            ).lower()
            if hitme == "y":
                user_cards.append(dealcard())
            else:
                is_game_over = True

    # when we get here, all the cards have been dealt to the user. and now we need to check the computer's cards and compare them against each other.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealcard())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


if __name__ == "__main__":
    while (
        input(
            "\nDo you want to play a game of Blackjack?\nType 'y' to proceed: "
        ).lower()
        == "y"
    ):
        os.system("cls")
        play()
    print("Goodbye!")
