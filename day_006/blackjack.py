from os import system
from time import sleep
import random


def clear(): return system("clear")


# Welcome player to the game
clear()
print("""
______ _            _      ___            _    
| ___ \ |          | |    |_  |          | |   
| |_/ / | __ _  ___| | __   | | __ _  ___| | __
| ___ \ |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
| |_/ / | (_| | (__|   </\__/ / (_| | (__|   < 
\____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\
                                               
                                               
""")
print("Welcome to BlackJack Game!!!")
sleep(3)

playing = True
while playing:
    # Initialize the game
    clear()
    player_bet = int(
        input("Please input your initial bet chip that you have. : "))

    # Initialize each round
    while player_bet > 0:

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

        def deduct_chip(init, chip):
            return init - chip

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

        def bet_pool(num_bet):
            return num_bet * 2

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
                    for card in dealer_hand:
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

            if has_a and (accumulate_score + 10) <= 21:
                accumulate_score += 10

            return accumulate_score

        # Define function to show both dealer and player hand and score

        def show_both_hand():
            print(f"The card on player hand is : {show_hand(False)}")
            print(f"The card on dealer hand is : {show_hand(True)}")
            print("---Dealer must stand on 17 or above---")

        # Define function to let player choose to hit or stand

        def hit_or_stand():
            choice = input(
                f"Do you want to hit another card(h) or stand(s)? : ").lower()
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

        player_is_bust = False
        player_going = True
        reset_card()

        clear()
        bet = place_bet()
        player_bet = deduct_chip(player_bet, bet)

        deal()

        player_score = count_score(player_hand)
        dealer_score = count_score(dealer_hand)
        # Determine if player value is bust or not

        # Make the player and dealer can be able to continue hitting another card
        while player_going and not player_is_bust:
            show_player_chip()
            print(f"The bet pool now is ${bet_pool(bet)}")
            print("---------")
            show_both_hand()
            player_score = count_score(player_hand)
            print(f"\nYour current score is {player_score}.\n")
            if player_score == 21 and len(player_hand) == 2:
                clear()
                print(show_hand(False))
                print("\nLucky!! You got BlackJack.")
                sleep(3)
                player_going = False
            elif player_score == 21:
                player_going = False
            elif player_score > 21:
                player_is_bust = True
            else:
                player_going = hit_or_stand()
                if player_going:
                    player_hit()

        if not player_going:
            clear()
            reveal = True
            show_both_hand()
            dealer_score = count_score(dealer_hand)
            print(f"\nYour current score is {player_score}.")
            print(f"Dealer current score is {dealer_score}.")
            sleep(3)
            while dealer_score < 17:
                clear()
                print("Dealer hit a card!")
                sleep(2)
                clear()
                dealer_hit()
                dealer_score = count_score(dealer_hand)
                if dealer_score > 21:
                    print(show_hand(True))
                    print("\nDealer's Bust!!")
                    sleep(3)
                else:
                    show_both_hand()
                    print(f"\nYour current score is {player_score}.")
                    print(f"Dealer current score is {dealer_score}.")
                    sleep(3)

        if player_is_bust:
            clear()
            print(show_hand(False))
            print("\nBust!!\nYou lose.")
            sleep(3)
        elif dealer_score > 21:
            clear()
            print("You win!!\n")
            print(f"You received ${bet_pool(bet)} of chips.")
            player_bet += bet_pool(bet)
            sleep(3)
        elif (player_score > dealer_score) and not player_is_bust:
            clear()
            print("You win!!\n")
            print(f"You received ${bet_pool(bet)} of chips.")
            player_bet += bet_pool(bet)
            sleep(3)
        elif dealer_score > player_score:
            clear()
            print("You lose!!\n")
            sleep(2)
        elif player_score == dealer_score:
            clear()
            print("Draw!!\n")
            print(f"You received ${int(bet_pool(bet)/2)} of returned chips.")
            player_bet += int(bet_pool(bet)/2)
            sleep(3)

    clear()
    answer = input("Do you want to reset the game? ( Y or N) : ").lower()
    if answer == "n":
        clear()
        print("Thank you for playing!")
        playing = False
        sleep(2)
    elif answer == "y":
        clear()
        print("Okay! let's go another round.")
        sleep(2)
