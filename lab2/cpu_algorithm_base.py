from abc import ABCMeta, abstractmethod


class CpuAlgorithmBase:
    __metaclass__ = ABCMeta

    def __init__(self, tick_tack_toe):
        self.tick_tack_toe = tick_tack_toe

    @abstractmethod
    def get_move_coordinates(self):
        pass
