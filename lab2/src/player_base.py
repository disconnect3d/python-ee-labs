from abc import ABCMeta, abstractmethod


class PlayerNotFullyInitializedError(Exception):
    pass


class PlayerBase:
    """Base class for any player controller"""

    __metaclass__ = ABCMeta

    def __init__(self, marker):
        self.marker = marker
        self._board_initialized = False
        self._board = None

    def move(self):
        if self._board:
            index = self._make_move()

            if isinstance(index, int):
                return index, None
            else:
                return index

        else:
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
