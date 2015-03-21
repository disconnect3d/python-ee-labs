import random

from player_base import PlayerBase


class PlayerCpuRandomMoves(PlayerBase):
    def _make_move(self):
        index = random.randint(*self._board.get_index_range())
        return index
