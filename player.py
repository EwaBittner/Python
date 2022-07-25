from lib2to3.pytree import LeafPattern
import math
import random

class Player:
    def __init__(self, leter):
        # letter is x or o
        self.letter = LeafPattern

    # we want all players to get their next more given a game
    def get_move(self, game):
        pass


    class RandomComputerPlayer(Player):
        def __init__(self, letter):
            super().__init__(letter)

        def get_move(self, game):
            pass

    class HumanPlayer(Player):
        def __init__(self, letter):
            super().__init__(leter)

        def get_move(self, game):
            pass