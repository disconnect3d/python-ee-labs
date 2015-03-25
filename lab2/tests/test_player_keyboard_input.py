import unittest

import mock

import player_keyboard_input

PlayerKeyboardInput = player_keyboard_input.PlayerKeyboardInput


class TestPlayerKeyboardInput(unittest.TestCase):
    def setUp(self):
        self.player = PlayerKeyboardInput('x')
        self.player._board = mock.MagicMock()

    def test_make_move_proper_input(self):
        player_keyboard_input.raw_input = lambda: '3'
        self.assertEqual(self.player._make_move(), 3)

    def test_make_move_wrong_input(self):
        self.first = True

        def mock_raw_input(msg=None):
            if self.first:
                self.first = False
                return 'asd'
            else:
                return '4'

        player_keyboard_input.raw_input = mock_raw_input
        self.assertEqual(self.player._make_move(), 4)


if __name__ == '__main__':
    unittest.main()
