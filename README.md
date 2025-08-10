# Five-Card Draw Poker Game

A simple command-line **Five-Card Draw Poker** game implemented in Python.

## Features

- Deals 5 cards to player and opponent from a shuffled deck
- Allows the player to choose which cards to exchange
- Looks for poker hands based on rules from [Wikipedia - Poker](https://en.wikipedia.org/wiki/List_of_poker_hands)
- Handles tiebreakers with kicker logic
- Compares hands and declares the winner

## How to Play

1. Run the script.
2. You will be dealt 5 cards.
3. Choose how many cards you want to exchange (0-4).
4. Select the cards to replace by their numbers.
5. The opponent’s cards are dealt.
6. The game evaluates and displays the winner.

## How to Run

py poker_game.py

## Main functions

create_deck(): Creates and shuffles the deck.

draw_cards(): Draws cards from the deck.

how_many_points(): Evaluates hand strength and gives points.

kicker(): Resolves ties.

game(): Main game loop.

