#!/usr/bin/env python3

from brain_games.engine import game_engine
from brain_games.games_conditions import brain_even_conditions


def main():
    game_engine.game(brain_even_conditions)


if __name__ == '__main__':
    main()
