import random
import os
from cpu_algorithm_random_moves import CpuAlgorithmRandomMoves
from utils import logger_injector


class Marker:
    NONE = ' '
    X = 'x'
    O = 'o'


@logger_injector
class TickTackToe(object):
    def __init__(self, cpu_logic=CpuAlgorithmRandomMoves, size=3):
        self._player_marker = Marker.X if random.random() > 0.5 else Marker.O
        self._enemy_marker = Marker.X if self._player_marker == Marker.O else Marker.O
        self._starts_game = self._player_marker if random.random() > 0.5 else self._enemy_marker

        self._size = size
        self._map = self._create_map()
        self._cpu = cpu_logic(self)

    @property
    def size(self):
        return self._size

    @property
    def player_marker(self):
        return self._player_marker

    @property
    def enemy_marker(self):
        return self._enemy_marker

    def _create_map(self):
        self.logger.info("Creating map of size={}".format(self._size))
        return {(x, y): Marker.NONE for x in xrange(self._size) for y in xrange(self._size)}

    def put_marker(self, x, y):
        if not self.is_empty(x, y):
            return False

        self._map[(x, y)] = self._player_marker
        return True

    def has_winner(self):
        # TODO / FIXME : Implement this!
        return False

    def enemy_move(self):
        x, y = self._cpu.get_move_coordinates()
        self._map[(x, y)] = self._enemy_marker

    def is_empty(self, x, y):
        return self._map[(x, y)] == Marker.NONE

    def format_map(self):
        # TODO / FIXME : remove "None" from the output ...
        newline = os.linesep + '-' * (self._size * 2 - 1) + os.linesep
        print newline.join(('|'.join(self._map[(x, y)] for x in xrange(self._size)) for y in xrange(self._size)))

    def possible_coordinate(self, value):
        return value >= 0 and value < self._size


t = TickTackToe()


def get_input(t):
    """This will be changed/refactored probably."""
    print "pass x"
    x = input()
    while not t.possible_coordinate(x):
        print "wrong x, pass x again"
        x = input()

    print "pass y"
    y = input()
    while not t.possible_coordinate(y):
        print "wrong y, pass y again"
        y = input()

    if not t.put_marker(x, y):
        print "This field is already taken, pass again!"
        get_input(t)


while True:
    get_input(t)

    if t.has_winner():
        break

    t.enemy_move()
    if t.has_winner():
        break

    print "Map:"
    print t.format_map()
