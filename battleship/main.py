#!/usr/bin/env python

from utils import Battleship

def start_game():
    print("Welcome to the game")
    print("Instructions")
    print(""""
    
    ***    In this game you are going to play against the computer.
    ***    If you want to play you should write 'yes' once the program has started.
    ***    You have to introduce your username to play.
    ***    To make a shot you should write first the number of the row and second the number of the column.
    ***    The coordinates must be integers between 0 and 9.
    ***    The winner is the player that shut down the opponent's fleet.
    ***    Each fleet is made of 10 ships of 4 different types.

    """)

    start = input("Play? (yes/no) ")

    if start.lower() == 'yes':
        battle = Battleship()
        if battle.result:
            print("You won")
        else:
            print("The computer won")


if __name__ == "__main__":
    
    start_game()


