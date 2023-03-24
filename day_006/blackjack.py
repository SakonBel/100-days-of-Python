from os import system
from time import sleep
import random


def clear(): return system("clear")


# Welcome player to the game
clear()
print("Welcome to BlackJack Game!")
sleep(1)


# Define card and initial deck function
card_symbols = ["♠", "♥", "♦", "♣"]
card_numbers = ["2", "3", "4", "5", "6",
                "7", "8", "9", "10", "J", "Q", "K", "A"]

card_deck = []


def reset_card():
    for symbol in card_symbols:
        for number in card_numbers:
            card_deck.append(number + symbol)


# Define initial bet pool of player and dealer

def show_player_chip():
    print(f"You balance is : {player_bet}")


def place_bet():
    show_player_chip()
    placing = input("Please place your bet. (Maximum is $500) : $")
    clear()
    try:
        int_bet = int(placing)
        if int_bet < 0:
            print("You can't place bet with that number right?")
            sleep(2)
            clear()
            place_bet()
        if int_bet > 500:
            print("The bet limited is at $500!")
            sleep(2)
            clear()
            place_bet()
        else:
            return int_bet
    except ValueError:
        print("Oops, That's not an invalid bet!")
        sleep(2)
        clear()
        place_bet()


def show_bet_pool(num_bet):
    print(f"The bet pool now is ${num_bet * 2}")


player_hand = []
dealer_hand = []


def player_hit():
    player_hand.append(card_deck.pop(
        card_deck.index(random.choice(card_deck))))


def dealer_hit():
    dealer_hand.append(card_deck.pop(
        card_deck.index(random.choice(card_deck))))


def deal():
    dealer_hit()
    dealer_hit()
    player_hit()
    player_hit()


# Set show hand function and reveal hand for dealer
reveal = False


def show_hand(dealer):
    p_hand = ""
    if not dealer:
        for card in player_hand:
            p_hand += ("[" + card + "]")
    else:
        if not reveal:
            p_hand += f"[{dealer_hand[0]}][??]"
        else:
            for card in player_hand:
                p_hand += ("[" + card + "]")

    return p_hand


# Set rule to count score


def count_score(hand):
    accumulate_score = 0
    has_a = False
    for card in hand:
        score = card[0]
        t_score = card[1]
        int_score = 0
        try:
            if t_score == "0":
                int_score = int(score + t_score)
                accumulate_score += int_score
            else:
                int_score = int(score)
                accumulate_score += int_score
        except ValueError:
            if score == "J" or score == "Q" or score == "K":
                int_score = 10
                accumulate_score += int_score
            elif score == "A":
                has_a = True
                int_score = 1
                accumulate_score += int_score

    if has_a and accumulate_score <= 21:
        accumulate_score += 10

    return accumulate_score


# Define function to show both dealer and player hand and score


def show_both_hand():
    print("\n---------\n")
    print(f"The card on player hand is : {show_hand(False)}")
    print(f"The card on dealer hand is : {show_hand(True)}")

# Define function to let player choose to hit or stand


def hit_or_stand():
    choice = input(
        f"\nDo you want to hit another card(h) or stand(s)? : ").lower()
    if choice == "h":
        clear()
        return True
    elif choice == "s":
        clear()
        return False
    else:
        clear()
        print("You input an invalid choice")
        sleep(2)
        hit_or_stand()


# Determine if player value is blackjack or not
is_blackjack = False
player_is_bust = False

# Initialize the game
player_bet = input("Please input your initial bet chip that you have. : ")
reset_card()

clear()
bet = place_bet()

deal()

player_score = count_score(player_hand)
dealer_score = count_score(dealer_hand)
player_going = True


# Make the player and dealer can be able to continue hitting another card
while player_going and not is_blackjack and not player_is_bust:
    show_player_chip()
    show_bet_pool(bet)
    show_both_hand()
    player_score = count_score(player_hand)
    print(f"Your current score is {player_score}.\n")
    if player_score == 21 and len(player_hand) == 2:
        print("BlackJack!!")
        is_blackjack = True
    elif player_score > 21:
        player_is_bust = True
    else:
        player_going = hit_or_stand()
        player_hit()


if player_is_bust:
    clear()
    show_both_hand
    print("\nBust!!\nYou lose.")
