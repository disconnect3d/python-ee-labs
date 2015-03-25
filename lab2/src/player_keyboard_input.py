from __future__ import print_function
from player_base import PlayerBase


class PlayerKeyboardInput(PlayerBase):
    def _make_move(self):
        return self._get_keyboard_input()

    def _get_keyboard_input(self):
        index = raw_input()

        while True:
            try:
                return int(index)
            except ValueError:
                index = raw_input(
                    "Wrong input, game board:\n{}\n"
                    "Pass field index (starting from 0 at top left corner):\n"
                        .format(self._board.formatted())
                )

    def inform(self, msg):
        print(msg)
