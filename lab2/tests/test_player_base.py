import unittest

from player_base import PlayerBase, PlayerNotFullyInitializedError


class TestPlayer(PlayerBase):
    def _make_move(self):
        pass


class TestPlayerBase(unittest.TestCase):
    def setUp(self):
        self.player = TestPlayer('x')
        self.player._board = [' ' for i in range(3)]

    def test_move_board_not_initialized(self):
        self.player._board = None
        self.assertRaises(PlayerNotFullyInitializedError, self.player.move)

    def test_move_xy(self):
        self.player._make_move = lambda: (1, 2)
        self.assertEqual(self.player.move(), (1, 2))

    def test_move_index(self):
        self.player._make_move = lambda: 1
        self.assertEqual(self.player.move(), (1, None))


if __name__ == '__main__':
    unittest.main()
