from abc import ABCMeta, abstractmethod

from utils import logger_injector


class PlayerNotFullyInitializedError(Exception):
    pass


@logger_injector
class PlayerBase:
    """Base class for any player controller"""

    __metaclass__ = ABCMeta

    def __init__(self, marker):
        self._marker = marker
        self._board = None

    @property
    def marker(self):
        return self._marker

    def move(self):
        self.logger.info("Player {} .move() called".format(self.marker))

        if self._board:
            index = self._make_move()

            if isinstance(index, int):
                self.logger.debug("index({}) is index int".format(index))
                return index, None
            else:
                self.logger.debug("index({}) is x, y tuple".format(index))
                return index

        else:
            self.logger.error("Player {} .move() called without initializing board first".format(self.marker))
            raise PlayerNotFullyInitializedError("Player must have board set before calling `make_move`.")

    @abstractmethod
    def _make_move(self):
        """This method must either return `index` or tuple of `x` and `y` integer values."""
        pass

    def inform(self, message):
        """This method is called by game loop to inform user what has happened.
        Implementation of real player controller may need this.
        The messages used are stored in `constants.Messages`"""
        pass

    def name(self):
        return self.marker
