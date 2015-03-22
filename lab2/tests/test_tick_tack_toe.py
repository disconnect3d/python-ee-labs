import unittest

import mock

from lab2.src.tick_tack_toe import TickTackToe


class TestTickTackToe(unittest.TestCase):
    def setUp(self):
        self.p1 = mock.MagicMock()
        self.p2 = mock.MagicMock()
        self.board = mock.MagicMock()
        self.board.empty_marker = ' '

        self.game = TickTackToe([self.p1, self.p2], self.board)
        self.game._min_moves_to_win = 3

    def test_is_game_over_false__moves_done_below_minimal_moves_to_win(self):
        self.game._moves_done = 1

        self.assertFalse(self.game.is_game_over())

    def test_is_game_over_true__have_winner(self):
        self.game._moves_done = 4
        self.game._check_winner = lambda: 'x'

        self.assertTrue(self.game.is_game_over())

    def test_is_game_over_true__is_tie(self):
        self.game._moves_done = 4
        self.game._check_winner = lambda: self.board.empty_marker
        self.game._is_tie = lambda: True

        self.assertTrue(self.game.is_game_over())

    def test_is_game_over_false__game_not_end(self):
        self.game._moves_done = 5
        self.game._check_winner = lambda: self.board.empty_marker
        self.game._is_tie = lambda: False

        self.assertFalse(self.game.is_game_over())


if __name__ == '__main__':
    unittest.main()
