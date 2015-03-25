import unittest

import mock

from player_cpu_random_moves import PlayerCpuRandomMoves


class TestCpuRandomMoves(unittest.TestCase):
    def setUp(self):
        self.player = PlayerCpuRandomMoves('x')

    @mock.patch('random.randint', return_value=10)
    def test_make_move(self, patch):
        self.player._board = mock.MagicMock()
        self.player._board.get_index_range.return_value = [0, 12]
        self.assertEqual(self.player._make_move(), 10)


if __name__ == '__main__':
    unittest.main()
