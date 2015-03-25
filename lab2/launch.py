"""Launcher for TickTackToe game and tests.

Usage:
  launch game simulation [<size=3>]
  launch game [<size=3>]
  launch test
  launch -h | --help

Options:
  -h --help                     Show this screen.
  game [<size=3>]               Launches TickTackToe Player vs CPU game on map of passed size (default=3).
  game simulation [<size=3>]    Launches TickTackToe CPU vs CPU game on map of passed size (default=3).
  test                          Launches unit tests.
"""

from __future__ import print_function
import os
import sys
import unittest

from docopt import docopt


args = docopt(__doc__)

SRC_DIR = 'src'
TEST_DIR = 'tests'

# appending SRC path into PYTHONPATH
# so tests will be able to import stuff from src properly
sys.path.append(SRC_DIR)

if not os.path.exists(SRC_DIR):
    print("Can't find directory with sources: {}".format(SRC_DIR))
    sys.exit()

if args['test']:
    if not os.path.exists(TEST_DIR):
        print("Can't find directory with tests: {}".format(TEST_DIR))
        sys.exit()

    testsuite = unittest.TestLoader().discover(TEST_DIR)
    unittest.TextTestRunner(verbosity=1).run(testsuite)

if args['game']:
    from src.tick_tack_toe import TickTackToe
    from src.board import Board
    from src.player_cpu_random_moves import PlayerCpuRandomMoves
    from src.player_keyboard_input import PlayerKeyboardInput

    size = 3
    size_kw = '<size=3>'
    if args[size_kw]:
        try:
            size = int(args[size_kw])
        except ValueError:
            print("Error: Size must be odd number greater than or equal to 3.")

    p1_cls = PlayerCpuRandomMoves if args['simulation'] else PlayerKeyboardInput
    p1 = p1_cls(marker='x')
    p2 = PlayerCpuRandomMoves(marker='o')
    b = Board(size=size, players_markers=[p1.marker, p2.marker], empty_marker=' ')

    game = TickTackToe(players=(p1, p2), board=b)
    game.game_loop()
    print(game.get_result())
