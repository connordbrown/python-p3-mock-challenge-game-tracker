#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    game = Game("Skribbl.io")
    player_1 = Player('Saaammmm')
    player_2 = Player('ActuallyTopher')
    Result(player_1, game, 2000)
    Result(player_1, game, 1)
    Result(player_2, game, 1900)
    Result(player_2, game, 10)

    ipdb.set_trace()