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
player_bet = 10000
dealer_bet = 10000


def place_bet():
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


# Initialize the game
reset_card()

clear()
bet = place_bet()

deal()

print(player_hand)
print(dealer_hand)
print(card_deck)
