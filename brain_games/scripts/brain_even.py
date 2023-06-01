#!/usr/bin/env python3

from brain_games.engine import game_engine
from brain_games.games_logic import brain_even_logic


def main():
    game_engine.game(brain_even_logic)


if __name__ == '__main__':
    main()
