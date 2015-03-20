import random
from cpu_algorithm_base import CpuAlgorithmBase


class CpuAlgorithmRandomMoves(CpuAlgorithmBase):
    def get_move_coordinates(self):
        while True:
            x = random.randrange(self.tick_tack_toe.size)
            y = random.randrange(self.tick_tack_toe.size)

            if self.tick_tack_toe.is_empty(x, y):
                return x, y
